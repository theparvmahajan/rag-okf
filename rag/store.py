import faiss
import json
from pathlib import Path
 
def build_index(vectors):
    dim = vectors.shape[1]
    index = faiss.IndexFlatIP(dim)
    index.add(vectors.astype("float32"))
    return index
 
def save_index(index, chunks, out_dir="index", meta=None, piece_to_chunk=None):
    """`meta`: arbitrary dict recorded alongside the index - rag.py's
    ingest() writes chunk_size/overlap/embedding model/source folder here
    specifically so a later run can verify what actually built this index
    instead of assuming.

    `piece_to_chunk` (new): if the index holds multiple embedding rows per
    chunk (rag.py's default since the MiniLM-truncation fix - see
    dense_chunking.py), this is the row-index -> chunk-list-index mapping
    needed to aggregate piece-level FAISS hits back to chunk-level results.
    None means a classic 1-row-per-chunk index (either built before this
    fix, or built with --single-vector-per-chunk) - rag/retriever.py
    treats None as "use the old direct-lookup behavior", so old indexes
    keep working without being rebuilt, they just don't get the
    truncation fix until re-ingested."""
    Path(out_dir).mkdir(exist_ok=True)
    faiss.write_index(index, f"{out_dir}/vectors.faiss")
    with open(f"{out_dir}/chunks.json", "w") as f:
        json.dump(chunks, f)
    if meta is not None:
        with open(f"{out_dir}/index_meta.json", "w") as f:
            json.dump(meta, f, indent=2)
    if piece_to_chunk is not None:
        with open(f"{out_dir}/piece_to_chunk.json", "w") as f:
            json.dump(piece_to_chunk, f)
 
def load_index(out_dir="index"):
    index = faiss.read_index(f"{out_dir}/vectors.faiss")
    with open(f"{out_dir}/chunks.json") as f:
        chunks = json.load(f)
    return index, chunks

def load_index_meta(out_dir="index"):
    """Returns the dict written by save_index()'s `meta`, or None if this
    index predates that fix / was built without it - callers should treat
    None as "unverifiable, ask the person who built this index what
    chunk_size/overlap they used" rather than assuming any particular
    value."""
    meta_path = Path(out_dir) / "index_meta.json"
    if not meta_path.exists():
        return None
    return json.loads(meta_path.read_text(encoding="utf-8"))

def load_piece_map(out_dir="index"):
    """Returns the piece_to_chunk mapping written by save_index(), or None
    if this index has one embedding row per chunk (either an old index
    from before the multi-vector fix, or built with
    --single-vector-per-chunk). rag/retriever.py's retrieve() uses this
    return value directly - None routes to the original 1:1 lookup path,
    a list routes to the max-pool-aggregation path."""
    p = Path(out_dir) / "piece_to_chunk.json"
    if not p.exists():
        return None
    return json.loads(p.read_text(encoding="utf-8"))
