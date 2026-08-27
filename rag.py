import argparse
from rag.loader import load_documents
from rag.chunker import chunk_documents
from rag.embedder import embed_texts, get_tokenizer, MODEL_NAME
from rag.store import build_index, save_index, load_index, load_piece_map
from rag.retriever import retrieve
from rag.prompt import build_prompt
from rag.generator import generate_answer
from dense_chunking import build_piece_embeddings

def ingest(folder="data/docs", pattern="*.txt", index_dir="index", chunk_size=150, overlap=30,
           multi_vector=True):
    """multi_vector=True (default): fixes a measured problem, not a
    hypothetical one - the real all-MiniLM-L6-v2 tokenizer was run against
    this project's actual 150-word/30-overlap chunks and 40.3% (1,871 of
    4,644) exceeded its 256-token limit, meaning the encoder was silently
    working from a truncated prefix of those chunks - the exact failure
    mode the SSRN paper's Section 5.2 documents for its own baseline.
    Shrinking chunk_size can't reliably fix this on its own (measured
    density ranges from ~1 to ~7 tokens/word depending on how much
    YAML/CLI-flag/dotted-field-path content a chunk has - see
    dense_chunking.py's module docstring), so instead every chunk gets
    split into as many token-limit-safe pieces as it actually needs
    (usually 1, sometimes more), each piece gets its own embedding, and
    retrieval max-pools piece scores back to the chunk level
    (rag/retriever.py). The chunk_size/overlap you pass, and the resulting
    chunks.json, are completely unchanged by this - only vectors.faiss
    gains extra rows. Pass multi_vector=False to opt out and get the
    original 1-row-per-chunk behavior (faster to build, but chunks over
    256 tokens will be silently truncated by the encoder again)."""
    docs = load_documents(folder=folder, pattern=pattern)
    chunks = chunk_documents(docs, chunk_size=chunk_size, overlap=overlap)

    piece_to_chunk = None
    if multi_vector:
        tokenizer = get_tokenizer()
        print(f"Embedding with multi-vector splitting (real {MODEL_NAME} tokenizer) - "
              f"chunk boundaries unchanged, only the embedding step is affected...")
        piece_matrix, piece_to_chunk = build_piece_embeddings(chunks, embed_texts, tokenizer=tokenizer)
        index = build_index(piece_matrix)
        n_pieces = piece_matrix.shape[0]
        print(f"  {len(chunks)} chunks -> {n_pieces} embedded pieces "
              f"({n_pieces - len(chunks)} chunks needed more than 1 piece)")
    else:
        vectors = embed_texts([c["text"] for c in chunks])
        index = build_index(vectors)
        n_pieces = len(chunks)

    meta = {
        "chunk_size": chunk_size, "overlap": overlap,
        "embedding_model": MODEL_NAME, "source_folder": folder, "source_pattern": pattern,
        "n_documents": len(docs), "n_chunks": len(chunks),
        "multi_vector_embedding": multi_vector, "n_embedded_pieces": n_pieces,
    }
    save_index(index, chunks, out_dir=index_dir, meta=meta, piece_to_chunk=piece_to_chunk)
    print(f"Indexed {len(chunks)} chunks from {len(docs)} documents into {index_dir}/ "
          f"(chunk_size={chunk_size}, overlap={overlap}, multi_vector={multi_vector}).")
    print(f"Wrote {index_dir}/index_meta.json - check this before comparing against any "
          f"other index or a previously-frozen baseline run.")

def ask(query, top_k=4, index_dir="index"):
    index, chunks = load_index(index_dir)
    piece_to_chunk = load_piece_map(index_dir)
    results = retrieve(query, index, chunks, embed_texts, top_k, piece_to_chunk=piece_to_chunk)
    system_prompt, user_prompt = build_prompt(query, results)
    answer = generate_answer(system_prompt, user_prompt)
    print(answer)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)

    ingest_p = sub.add_parser("ingest")
    ingest_p.add_argument("--folder", default="data/docs")
    ingest_p.add_argument("--pattern", default="*.txt",
                           help='e.g. "**/*.md" for a nested markdown corpus')
    ingest_p.add_argument("--index-dir", default="index")
    ingest_p.add_argument("--chunk-size", type=int, default=150,
                           help="Words per chunk. Default (150) matches the actual "
                                "already-frozen B1/B2 baseline - override explicitly if you "
                                "mean to build a differently-chunked index, and note it "
                                "won't be directly comparable to B1/B2 results built at a "
                                "different setting.")
    ingest_p.add_argument("--chunk-overlap", type=int, default=30, dest="overlap",
                           help="Word overlap between consecutive chunks. Default (30) "
                                "matches the actual already-frozen B1/B2 baseline.")
    ingest_p.add_argument("--single-vector-per-chunk", action="store_true",
                           help="Opt out of the multi-vector embedding fix and go back to "
                                "exactly 1 embedding per chunk (original behavior). Faster to "
                                "build, but any chunk over 256 real tokens will be silently "
                                "truncated by the encoder - measured at 40.3%% of chunks in "
                                "this corpus at the default chunk_size/overlap. Only use this "
                                "if you specifically need to reproduce numbers from before the "
                                "fix, or don't have network access to load the tokenizer.")

    ask_p = sub.add_parser("ask")
    ask_p.add_argument("query")
    ask_p.add_argument("--index-dir", default="index")

    args = parser.parse_args()

    if args.command == "ingest":
        ingest(folder=args.folder, pattern=args.pattern, index_dir=args.index_dir,
               chunk_size=args.chunk_size, overlap=args.overlap,
               multi_vector=not args.single_vector_per_chunk)
    elif args.command == "ask":
        ask(args.query, index_dir=args.index_dir)
