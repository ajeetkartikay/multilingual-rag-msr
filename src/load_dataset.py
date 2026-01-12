from datasets import load_dataset
import os

def download_tydi():
    """
    Download TyDi QA dataset (secondary task).
    For now, we store the full dataset without language filtering.
    Language-specific filtering will be done in preprocessing.
    """
    print("Downloading TyDi QA dataset...")
    dataset = load_dataset("tydiqa", "secondary_task", split="train")

    os.makedirs("../data/raw", exist_ok=True)
    output_path = "../data/raw/tydi_full.json"

    dataset.to_json(output_path)
    print(f"Saved dataset to {output_path}")
    print(f"Total samples: {len(dataset)}")

if __name__ == "__main__":
    download_tydi()

