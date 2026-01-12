import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

INDEX_PATH = "data/index/faiss.index"
META_PATH = "data/index/metadata.json"

def load_index():
    print("Loading FAISS index...")
    index = faiss.read_index(INDEX_PATH)

    print("Loading metadata...")
    with open(META_PATH, "r", encoding="utf-8") as f:
        metadata = json.load(f)

    return index, metadata

def retrieve(query, k=5):
    index, metadata = load_index()

    print("Loading multilingual embedding model...")
    model = SentenceTransformer("sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")

    print(f"Encoding query: {query}")
    query_vec = model.encode([query])
    query_vec = np.array(query_vec).astype("float32")

    print("Searching index...")
    distances, indices = index.search(query_vec, k)

    print("\nTop Results:\n")
    for i, idx in enumerate(indices[0]):
        doc = metadata[idx]
        print(f"Result {i+1}:")
        print("Question:", doc["question"])
        print("Context:", doc["context"][:300], "...")
        print("Answers:", doc["answers"])
        print("-" * 50)

if __name__ == "__main__":
    user_query = input("Enter your query: ")
    retrieve(user_query)
