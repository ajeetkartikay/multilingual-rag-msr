import json
import os
import faiss
from sentence_transformers import SentenceTransformer
import numpy as np

DATA_PATH = "data/processed/documents.jsonl"
INDEX_PATH = "data/index/faiss.index"
META_PATH = "data/index/metadata.json"

def build_faiss_index():
    print("Loading processed documents...")
    documents = []

    with open(DATA_PATH, "r", encoding="utf-8") as f:
        for line in f:
            documents.append(json.loads(line))

    texts = [doc["context"] for doc in documents]

    print("Loading multilingual embedding model...")
    model = SentenceTransformer("sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")

    print("Encoding documents...")
    embeddings = model.encode(texts, show_progress_bar=True, batch_size=32)
    embeddings = np.array(embeddings).astype("float32")

    dim = embeddings.shape[1]
    print(f"Embedding dimension: {dim}")

    print("Building FAISS index...")
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)

    os.makedirs("data/index", exist_ok=True)

    faiss.write_index(index, INDEX_PATH)

    with open(META_PATH, "w", encoding="utf-8") as f:
        json.dump(documents, f, ensure_ascii=False, indent=2)

    print(f"FAISS index saved to {INDEX_PATH}")
    print(f"Metadata saved to {META_PATH}")
    print(f"Total vectors indexed: {index.ntotal}")

if __name__ == "__main__":
    build_faiss_index()
