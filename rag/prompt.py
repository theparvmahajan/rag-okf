SYSTEM_PROMPT = (
    "You are a support assistant for Kubernetes documentation. "
    "Answer ONLY using the CONTEXT below. "
    "If the answer is not contained in the context, say you don't know "
    "instead of guessing. "
    "Cite the source file for every claim using the format "
    "[source: path/to/file.md]."
)
def build_prompt(query, retrieved_chunks):
    blocks = []
    for r in retrieved_chunks:
        blocks.append(f"[source: {r['source']}]\n{r['text']}")
    context = "\n\n---\n\n".join(blocks)
 
    user_prompt = f"CONTEXT:\n{context}\n\nQUESTION:\n{query}"
    return SYSTEM_PROMPT, user_prompt