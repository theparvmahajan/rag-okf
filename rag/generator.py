from ollama import chat

DEFAULT_MODEL = "qwen3.5:4b"
DEFAULT_NUM_PREDICT = 2048  # generous headroom so a thinking-capable model
                              # isn't at risk of getting cut off mid-reasoning
                              # even if think=False doesn't fully suppress it


def generate_answer(
    system_prompt,
    user_prompt,
    model=DEFAULT_MODEL,
    return_usage=False,
    max_retries=3,
    num_predict=DEFAULT_NUM_PREDICT,
):
    """
    Generate an answer using local Qwen3.5 through Ollama.

    Qwen3.5 is a "thinking" model: by default Ollama routes its reasoning
    into a separate `message.thinking` field and only the final answer
    into `message.content`. If the model's default settings burn the
    whole output-token budget on reasoning before it reaches the final
    answer, `content` comes back empty even though generation "succeeds"
    (no exception, eval_count > 0, error is None) - this is what caused
    a chunk of empty answers in earlier eval runs despite everything else
    in the record looking normal. See
    https://github.com/ollama/ollama/issues/14793.

    Fixed with three layers:
      1. think=False passed as a *top-level* chat() argument (not inside
         `options` - Ollama's chat API honors it there; some other code
         paths silently ignore it inside options).
      2. A generous num_predict as a safety net in case think=False
         doesn't fully suppress reasoning on a given model/template build.
      3. Retries (up to max_retries): if content still comes back empty,
         retry with more room and an explicit "/no_think" suffix on the
         prompt - a documented workaround for template builds where the
         think toggle is ignored. If it's still empty after all retries,
         raise instead of silently returning "" so the failure is visible
         (evaluate.py already catches exceptions here and logs them to
         the "error" field - much easier to spot than a blank answer with
         no error).

    Keeps the same interface as the previous Gemini generator so the
    rest of the RAG pipeline does not need to change.
    """
    last_response = None
    last_thinking_len = 0

    for attempt in range(1, max_retries + 1):
        attempt_user_prompt = user_prompt if attempt == 1 else f"{user_prompt}\n\n/no_think"

        response = chat(
            model=model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": attempt_user_prompt},
            ],
            think=False,
            options={
                "temperature": 0,
                "num_predict": num_predict * attempt,
            },
        )
        last_response = response

        text = (response.message.content or "").strip()
        if text:
            break

        last_thinking_len = len((getattr(response.message, "thinking", None) or "").strip())
    else:
        text = ""

    if not text:
        raise RuntimeError(
            f"Empty answer from {model} after {max_retries} attempt(s) "
            f"(think=False set each time; last attempt used "
            f"num_predict={num_predict * max_retries}, "
            f"eval_count={getattr(last_response, 'eval_count', None)}, "
            f"thinking_chars={last_thinking_len}). The model is likely "
            f"still burning its token budget on reasoning despite "
            f"think=False - consider a model/build with reliable "
            f"thinking-toggle support, or raise num_predict further."
        )

    if not return_usage:
        return text

    # Ollama provides token counts in the response.
    usage = {
        "input_tokens": getattr(last_response, "prompt_eval_count", None),
        "output_tokens": getattr(last_response, "eval_count", None),
        "total_tokens": None,
    }

    if (
        usage["input_tokens"] is not None
        and usage["output_tokens"] is not None
    ):
        usage["total_tokens"] = (
            usage["input_tokens"] + usage["output_tokens"]
        )

    return text, usage
