from pathlib import Path

DEFAULT_EXCLUDE_DIRS = ("okf_data", "okf_structure", "okf_relations")

def load_documents(folder="data/docs", pattern="*.txt", exclude_dirs=DEFAULT_EXCLUDE_DIRS):
    """Load every file under `folder` matching `pattern` into a uniform
    {doc_id, source, text} record.

    `pattern` supports pathlib's recursive globbing, e.g. "**/*.md" walks
    nested subfolders. `source` is the file's path *relative to `folder`*
    (not just its basename) so that files with the same name in different
    subfolders - e.g. many docs trees have a `_index.md` per folder - don't
    collide or overwrite each other's identity.

    `exclude_dirs`: any path component matching one of these is skipped
    entirely. Defaults to the OKF bundle directory names specifically -
    this used to be a real bug, not a hypothetical one: build_okf.py
    previously wrote its output *inside* corpus_processed/, and a
    recursive "**/*.md" ingest pattern silently picked up every OKF
    concept file as if it were a source document (425 real docs became
    3,636 "documents" ingested). build_okf.py now writes outside
    corpus_processed/ by default, which is the real fix - this filter is
    the belt-and-suspenders backstop for any layout where that's not true
    (an old extracted zip, a custom --out-dir, etc.). Pass exclude_dirs=()
    to disable if you're certain you want everything under `folder`.
    """
    documents = []
    root = Path(folder)
    paths = sorted(root.glob(pattern))
    if exclude_dirs:
        excluded = 0
        kept_paths = []
        for path in paths:
            rel_parts = path.relative_to(root).parts
            if any(part in exclude_dirs for part in rel_parts):
                excluded += 1
                continue
            kept_paths.append(path)
        if excluded:
            print(f"load_documents: skipped {excluded} file(s) under excluded dirs "
                  f"{exclude_dirs} (pass exclude_dirs=() to include them)")
        paths = kept_paths
    for doc_id, path in enumerate(paths):
        text = path.read_text(encoding="utf-8")
        documents.append({
            "doc_id": doc_id,
            "source": path.relative_to(root).as_posix(),
            "text": text.strip(),
        })
    return documents