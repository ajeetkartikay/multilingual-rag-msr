\# Multilingual Retrieval-Augmented Question Answering (RAG)



A research-focused multilingual question answering system that enables cross-lingual semantic retrieval over a large QA corpus and produces language-adaptive answers using extractive grounding and lightweight translation.



---



\## Abstract



This repository presents a multilingual Retrieval-Augmented Question Answering (RAG) pipeline designed for cross-lingual and low-resource natural language processing scenarios. The system ingests a large-scale multilingual QA dataset, encodes documents using state-of-the-art multilingual sentence embeddings, and indexes them with FAISS to enable efficient semantic retrieval across languages. Given a user query in any supported language, the system retrieves the most relevant contexts independent of language boundaries.



Instead of relying on computationally expensive generative models, the pipeline performs extractive answer selection from retrieved documents, ensuring factual grounding and reproducibility. An optional translation layer enables the output to be rendered in multiple target languages, making the system accessible to users in diverse linguistic settings. The architecture emphasizes modularity, scalability, and resource efficiency while maintaining research relevance.



---



\## Motivation



Multilingual question answering remains a central challenge in modern NLP, particularly in low-resource settings where annotated data and large-scale generative models are not readily available. Many existing QA and RAG systems are either monolingual or dependent on high-compute generative architectures, limiting their accessibility, reproducibility, and deployment on standard hardware.



This project is motivated by the need for:

\- Language-agnostic semantic retrieval across diverse linguistic communities

\- Faithful, evidence-grounded answers rather than unconstrained generation

\- Resource-efficient system design that operates without specialized hardware

\- Practical multilingual access to knowledge for underrepresented languages



By integrating cross-lingual embeddings, vector-based retrieval, extractive answer selection, and lightweight translation, this system provides a robust and reproducible alternative to heavy generative RAG pipelines, while retaining core research value in multilingual representation learning and cross-lingual information access.



---



\## Model Selection and Resource Considerations



During development, multiple multilingual generation models were evaluated for integration into the RAG pipeline, including mT5 and mBART. While these architectures provide strong multilingual generation capabilities, their memory requirements exceeded the available system resources on standard CPU-based environments, particularly in Windows settings without extended virtual memory or GPU acceleration.



To ensure that the system remains fully executable, reproducible, and accessible on commodity hardware, the final implementation adopts a lightweight extractive QA approach. Answers are selected directly from retrieved documents to preserve factual grounding and eliminate hallucination risks. A lightweight translation layer is then applied to render the extracted answer in multiple target languages.



This design choice reflects a conscious engineering trade-off: prioritizing reproducibility, transparency, and low-resource deployability over heavy generative modeling. The system architecture remains modular, allowing generative components to be reintroduced seamlessly in higher-resource environments without altering the retrieval backbone.



This approach aligns with real-world research and deployment scenarios where computational constraints are a primary consideration.



---



\## System Architecture and Pipeline



The system is designed as a modular, end-to-end multilingual Retrieval-Augmented Question Answering (RAG) pipeline. Each component is independently replaceable, enabling experimentation with alternative models, datasets, or deployment configurations.



\### 1. Data Ingestion

A multilingual QA dataset is ingested and preprocessed into a unified document format. Each entry consists of:

\- Question

\- Context (source document)

\- Ground-truth answer spans



This structured representation allows both semantic indexing and faithful extractive answer selection.



\### 2. Multilingual Embedding

All document contexts are encoded using a multilingual sentence embedding model. This step maps text from different languages into a shared semantic vector space, enabling cross-lingual similarity comparison.



\### 3. Vector Indexing (FAISS)

The encoded document vectors are indexed using FAISS for efficient approximate nearest-neighbor search. This allows scalable semantic retrieval over tens of thousands of multilingual documents with low latency.



\### 4. Cross-Lingual Retrieval

Given a user query in any supported language, the same multilingual embedding model encodes the query into the shared vector space. FAISS is then used to retrieve the top-k most semantically similar documents, independent of language.



\### 5. Extractive Answer Selection

Rather than generating free-form text, the system selects the answer directly from the retrieved document using dataset-provided ground-truth spans. This ensures:

\- Faithful grounding

\- Elimination of hallucinated responses

\- Deterministic and reproducible outputs



\### 6. Language-Adaptive Output

A lightweight translation layer optionally converts the extracted answer into multiple target languages (e.g., English, Hindi, Kannada, Malayalam). This allows users to query the system in one language and receive answers in another, supporting multilingual accessibility.



\### Design Principles

\- \*\*Modularity:\*\* Each stage (embedding, retrieval, answering, translation) can be independently replaced or extended.

\- \*\*Resource Efficiency:\*\* The system is designed to run on CPU-only environments without large memory requirements.

\- \*\*Reproducibility:\*\* All outputs are grounded in retrieved documents, enabling transparent evaluation.

\- \*\*Cross-Lingual Generalization:\*\* Retrieval and answering are language-agnostic by design.



This architecture provides a practical research framework for multilingual information access while remaining lightweight and deployable in constrained environments.



---



---



\## Installation and Reproducibility



This project is designed to be fully reproducible on CPU-only environments.



\### Prerequisites

\- Python 3.9 or higher

\- Git



\### Clone the Repository

git clone https://github.com/ajeetkartikay/multilingual-rag-msr.git

cd multilingual-rag-msr



\### Create Virtual Environment (Recommended)

python -m venv venv

venv\\Scripts\\activate



\### Install Dependencies

pip install -r requirements.txt



\### Data Preparation

The system uses a multilingual QA dataset that must be downloaded and preprocessed locally.



1\. Download and preprocess the dataset:

python src/load\_dataset.py

python src/preprocess.py



2\. Build the FAISS index:

python src/build\_index.py



\### Running the System

To run the multilingual QA pipeline:

python src/rag\_answer.py



You will be prompted to enter a natural language question. The system will:

1\. Retrieve relevant multilingual documents using semantic search.

2\. Select a grounded answer from the dataset.

3\. Optionally translate the answer into multiple target languages.



---



\## Reproducibility Notes

\- The `data/` directory is excluded from version control due to size constraints.

\- All results are deterministic and grounded in retrieved documents.

\- Generative components can be integrated in higher-resource environments without modifying the retrieval backbone.



\## Results and Example Outputs



The system demonstrates accurate cross-lingual retrieval and faithful answer grounding across multiple languages.



\### Example 1: Cross-Lingual Retrieval



\*\*Input Query (English):\*\*

What is the capital of India?

\*\*Retrieved Answer (Source Language):\*\*

نيودلهي



\*\*Translated Outputs:\*\*

\- \*\*English:\*\* New Delhi

\- \*\*Hindi:\*\* नई दिल्ली

\- \*\*Kannada:\*\* ನವ ದೆಹಲಿ

\- \*\*Malayalam:\*\* ന്യൂ ഡെൽഹി



This example illustrates that the system retrieves semantically relevant documents regardless of their original language and adapts the final output to multiple target languages.



---



\### Example 2: Language-Agnostic Question Answering



\*\*Input Query (Hindi):\*\*

भारत की राजधानी क्या है?

\*\*Output:\*\*

नई दिल्ली

The system encodes the Hindi query into the shared multilingual embedding space, retrieves the appropriate context from the dataset (possibly in another language), and returns a grounded answer.



---



\## Use Cases



\- \*\*Multilingual Information Access:\*\* Enables users to retrieve factual answers from multilingual corpora without requiring language-specific indexing.

\- \*\*Low-Resource Language Support:\*\* Provides practical QA functionality for languages with limited annotated data.

\- \*\*Research Prototyping:\*\* Serves as a modular testbed for experimenting with multilingual embeddings, retrieval strategies, and lightweight answer generation.

\- \*\*Educational Applications:\*\* Demonstrates cross-lingual NLP concepts in a reproducible, CPU-friendly environment.



---



\## Limitations



\- The system relies on the coverage of the underlying dataset; questions outside the dataset scope cannot be answered.

\- Extractive answering limits responses to available ground-truth spans.

\- Translation quality depends on the external translation backend and may vary across languages.



Despite these limitations, the system provides a strong, reproducible baseline for multilingual retrieval-augmented question answering in resource-constrained settings.



---



\## Project Structure

multilingual-rag-msr/

│

├── src/

│ ├── load\_dataset.py # Dataset download and ingestion

│ ├── preprocess.py # Data cleaning and formatting

│ ├── build\_index.py # Multilingual embedding and FAISS indexing

│ ├── retrieve.py # Semantic retrieval module

│ └── rag\_answer.py # End-to-end QA pipeline with translation

│

├── requirements.txt # Python dependencies

├── README.md # Project documentation

└── .gitignore # Excludes data, virtual environments, and caches



---



\## License



This project is released for research and educational use. If you plan to use this codebase in academic work, experiments, or derivative projects, please provide appropriate attribution.



---



\## How to Cite



If you use this project in research or academic work, please cite it as:



@software{multilingual\_rag\_qa,

author = {Ajeet Kartikay},

title = {Multilingual Retrieval-Augmented Question Answering},

year = {2026},

url = {https://github.com/ajeetkartikay/multilingual-rag-msr}



}



---



\## Acknowledgments



This project builds upon open-source research in multilingual representation learning, semantic retrieval, and information access, including:



\- FAISS for efficient vector search

\- Sentence-Transformers for multilingual embeddings

\- Hugging Face Datasets and Transformers ecosystems



The system design is inspired by contemporary research in retrieval-augmented NLP and cross-lingual information retrieval.





