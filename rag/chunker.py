def chunk_text(text, chunk_size=150, overlap=30):
    """Defaults match the actual already-frozen B1/B2 baseline (150-word
    chunks, 30-word overlap - confirmed directly, not inferred) - see
    rag.py's --chunk-size/--chunk-overlap for how to override, and
    rag/store.py's save_index() for how the chosen values get written into
    the index directory so a later evaluate.py run can verify what
    actually built the index it's pointing at, instead of silently
    assuming. (These defaults were briefly changed to 90/20 based on a
    misreading of the B1 description as "90-word chunks" - reverted once
    the actual index config was confirmed as 150/30. If you rebuilt an
    index with the 90/20 defaults in between, rebuild it again with these
    or pass --chunk-size 150 --chunk-overlap 30 explicitly.)"""
    words = text.split()
    chunks = []
    start = 0
    while start<len(words):
        end = start + chunk_size
        piece = " ".join(words[start:end])
        chunks.append(piece)
        if end>=len(words):
            break
        start += chunk_size - overlap
    return chunks

def chunk_documents(documents, chunk_size=150, overlap=30):
    chunks = []
    for doc in documents:
        pieces = chunk_text(doc["text"], chunk_size, overlap)
        for i, piece in enumerate(pieces):
            chunks.append({
                "chunk_id": len(chunks),
                "doc_id": doc["doc_id"],
                "source": doc["source"],
                "text": piece,
            })
    return chunks