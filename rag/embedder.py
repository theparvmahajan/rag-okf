from sentence_transformers import SentenceTransformer
 
MODEL_NAME = "all-MiniLM-L6-v2"
_model = SentenceTransformer(MODEL_NAME)
 
def embed_texts(texts):
    vectors = _model.encode(
        texts,
        batch_size=32,
        show_progress_bar=True,
        normalize_embeddings=True,
        convert_to_numpy=True,
    )
    return vectors

def get_tokenizer():
    """The same WordPiece tokenizer embed_texts() uses internally, exposed
    for dense_chunking.split_for_embedding() so a chunk/concept can be
    split into pieces that are GUARANTEED (not just probably) safe for
    this specific model's 256-token limit - see dense_chunking.py's module
    docstring for why a word-count guess isn't reliable enough on its own
    for this corpus."""
    return _model.tokenizer