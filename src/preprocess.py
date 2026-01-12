import json
import os

RAW_PATH = "data/raw/tydi_full.json"
OUTPUT_PATH = "data/processed/documents.jsonl"

def extract_documents():
    """
    Convert TyDi QA dataset into retrieval-ready documents.
    Each document will contain:
    - context passage
    - question
    - answer
    - language (if available later)
    """
    print("Loading raw dataset...")
    data = []
    with open(RAW_PATH, "r", encoding="utf-8") as f:
        for line in f:
            data.append(json.loads(line))

    documents = []
    for item in data:
        context = item.get("context", "").strip()
        question = item.get("question", "").strip()
        answers = item.get("answers", [])

        if context and question:
            doc = {
                "context": context,
                "question": question,
                "answers": answers
            }
            documents.append(doc)

    os.makedirs("../data/processed", exist_ok=True)

    with open(OUTPUT_PATH, "w", encoding="utf-8") as out:
        for doc in documents:
            out.write(json.dumps(doc, ensure_ascii=False) + "\n")

    print(f"Saved {len(documents)} documents to {OUTPUT_PATH}")

if __name__ == "__main__":
    extract_documents()
