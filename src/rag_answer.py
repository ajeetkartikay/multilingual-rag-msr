import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from deep_translator import GoogleTranslator

INDEX_PATH = "data/index/faiss.index"
META_PATH = "data/index/metadata.json"
MODEL_NAME = "google/byt5-small"
  # Multilingual text-to-text model


def load_retriever():
    print("Loading FAISS index...")
    index = faiss.read_index(INDEX_PATH)

    print("Loading metadata...")
    with open(META_PATH, "r", encoding="utf-8") as f:
        metadata = json.load(f)

    print("Loading embedding model...")
    embedder = SentenceTransformer("sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")

    return index, metadata, embedder

def load_generator():
    print("Loading multilingual generation model...")
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)
    return tokenizer, model

def retrieve_context(query, k=5):
    index, metadata, embedder = load_retriever()

    print(f"Encoding query: {query}")
    query_vec = embedder.encode([query])
    query_vec = np.array(query_vec).astype("float32")

    print("Searching index...")
    distances, indices = index.search(query_vec, k)

    contexts = []
    for idx in indices[0]:
        doc = metadata[idx]
        contexts.append(doc["context"])

    return contexts, indices

def generate_answer(query, contexts, metadata, indices):
    """
    Extractive answer: returns the dataset's ground-truth answers
    from the top retrieved document.
    """
    top_idx = indices[0][0]
    doc = metadata[top_idx]

    answers = doc.get("answers", [])
    if isinstance(answers, dict) and "text" in answers:
        return answers["text"][0]
    elif isinstance(answers, list) and len(answers) > 0:
        return answers[0]
    else:
        return "Answer not found in retrieved context."
def translate_answer(text, target_lang="hi"):
    """
    Translate extracted answer into target language.
    target_lang: 'hi' = Hindi, 'kn' = Kannada, 'ml' = Malayalam, 'en' = English
    """
    try:
        translated = GoogleTranslator(source='auto', target=target_lang).translate(text)
        return translated
    except Exception as e:
        print("Translation failed:", e)
        return text

if __name__ == "__main__":
    user_query = input("Enter your question: ")
    contexts, indices = retrieve_context(user_query)
    answer = generate_answer(user_query, contexts, load_retriever()[1], indices)
    
    print("\n=== FINAL ANSWER (Original) ===")
    print(answer)

    # Translate into multiple languages at once
    languages = {
        "en": "English",
        "hi": "Hindi",
        "kn": "Kannada",
        "ml": "Malayalam"
    }

    for code, name in languages.items():
        translated = translate_answer(answer, code)
        print(f"\n=== FINAL ANSWER ({name}) ===")
        print(translated)