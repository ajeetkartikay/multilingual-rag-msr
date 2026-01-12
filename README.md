\# 🌍 Multilingual Retrieval-Augmented Question Answering (RAG)



> A research-focused multilingual QA system enabling \*\*cross-lingual semantic retrieval\*\* and \*\*language-adaptive, grounded answers\*\* using extractive reasoning and lightweight translation.



🔍 Cross-lingual Retrieval • 📚 Faithful (Non-Hallucinatory) Answers • ⚡ CPU-Friendly \& Reproducible



---



\## ✨ Abstract



This repository presents a \*\*multilingual Retrieval-Augmented Question Answering (RAG)\*\* pipeline designed for \*\*cross-lingual and low-resource NLP scenarios\*\*. The system ingests a large-scale multilingual QA dataset, encodes documents using \*\*state-of-the-art multilingual sentence embeddings\*\*, and indexes them with \*\*FAISS\*\* to enable efficient semantic retrieval across languages.



Rather than relying on computationally expensive generative models, the pipeline performs \*\*extractive answer selection\*\* from retrieved documents, ensuring \*\*factual grounding and reproducibility\*\*. An optional translation layer renders outputs in multiple target languages, making the system accessible to users in diverse linguistic contexts. The architecture emphasizes \*\*modularity, scalability, and resource efficiency\*\* while maintaining research relevance.



---



\## 🎯 Motivation



Multilingual question answering remains a core challenge in modern NLP, particularly in \*\*low-resource environments\*\* where annotated data and large-scale generative models are limited. Many existing QA and RAG systems are either monolingual or dependent on high-compute architectures, restricting \*\*accessibility, reproducibility, and deployment on standard hardware\*\*.



This project is motivated by the need for:



\- \*\*Language-agnostic semantic retrieval\*\* across diverse linguistic communities  

\- \*\*Faithful, evidence-grounded answers\*\* rather than unconstrained generation  

\- \*\*Resource-efficient system design\*\* that operates without specialized hardware  

\- \*\*Practical multilingual access to knowledge\*\* for underrepresented languages  



By integrating cross-lingual embeddings, vector-based retrieval, extractive answer selection, and lightweight translation, this system offers a \*\*robust, reproducible alternative\*\* to heavy generative RAG pipelines while retaining strong research value in multilingual representation learning.



---



\## 🧠 Model Selection \& Resource Considerations



During development, multilingual generation models such as \*\*mT5\*\* and \*\*mBART\*\* were evaluated. While these architectures provide strong generation capabilities, their \*\*memory requirements exceeded available system resources\*\* in CPU-based environments.



To ensure \*\*full executability, reproducibility, and accessibility on commodity hardware\*\*, the final design adopts a \*\*lightweight extractive QA approach\*\*:



\- Answers are selected directly from retrieved documents to preserve factual grounding  

\- A translation layer enables multi-language output without heavy generative inference  



This design prioritizes \*\*reproducibility, transparency, and low-resource deployability\*\*, while remaining modular enough to reintroduce generative models in higher-resource environments.



---



\## 🔧 System Architecture \& Pipeline



\*\*Query → Multilingual Embedding → FAISS Retrieval → Extractive Answer → Optional Translation\*\*



\### 1️⃣ Data Ingestion

\- Multilingual QA dataset is ingested and preprocessed  

\- Each entry contains: \*\*Question, Context, Ground-Truth Answer Spans\*\*



\### 2️⃣ Multilingual Embedding

\- Documents are encoded into a \*\*shared semantic vector space\*\* using multilingual sentence embeddings  

\- Enables cross-lingual similarity comparison



\### 3️⃣ Vector Indexing (FAISS)

\- Embeddings are indexed using \*\*FAISS\*\* for fast approximate nearest-neighbor search  

\- Supports scalable retrieval over large corpora



\### 4️⃣ Cross-Lingual Retrieval

\- User queries in any language are embedded into the same vector space  

\- Top-k semantically similar documents are retrieved independent of language



\### 5️⃣ Extractive Answer Selection

\- Answers are selected directly from retrieved documents  

\- Ensures:

&nbsp; - Faithful grounding  

&nbsp; - No hallucination  

&nbsp; - Deterministic outputs  



\### 6️⃣ Language-Adaptive Output

\- Optional translation into \*\*English, Hindi, Kannada, Malayalam\*\*  

\- Enables querying in one language and answering in another



\*\*Design Principles\*\*

\- \*\*Modularity:\*\* Each stage is independently replaceable  

\- \*\*Resource Efficiency:\*\* CPU-only execution  

\- \*\*Reproducibility:\*\* Grounded, deterministic outputs  

\- \*\*Cross-Lingual Generalization:\*\* Language-agnostic retrieval  



---



\## ⚙️ Installation \& Usage



\### Install Dependencies

```bash

pip install -r requirements.txt

```



\### Data Preparation

```bash

python src/load\_dataset.py

python src/preprocess.py

```



\### Build FAISS Index

```bash

python src/build\_index.py

```



\### Run the System

```bash

python src/rag\_answer.py

```



\### Pipeline Behavior

\- Retrieves relevant multilingual documents  

\- Selects a grounded extractive answer  

\- Optionally translates into target languages  



---



\## 📊 Results \& Example Outputs



\### Example 1: Cross-Lingual Retrieval



\*\*Input (English):\*\*

```

What is the capital of India?

```



\*\*Retrieved Answer (Source Language):\*\*

```

نيودلهي

```



\*\*Translated Outputs:\*\*

\- \*\*English:\*\* New Delhi  

\- \*\*Hindi:\*\* नई दिल्ली  

\- \*\*Kannada:\*\* ನವ ದೆಹಲಿ  

\- \*\*Malayalam:\*\* ന്യൂ ഡെൽഹി  



---



\### Example 2: Language-Agnostic QA



\*\*Input (Hindi):\*\*

```

भारत की राजधानी क्या है?

```



\*\*Output:\*\*

```

नई दिल्ली

```



✔ Correct answer retrieved independent of source language.



---



\## 🚀 Use Cases



\- \*\*Multilingual Information Access\*\* – Language-agnostic QA over diverse corpora  

\- \*\*Low-Resource NLP\*\* – Practical QA without large generative models  

\- \*\*Research Prototyping\*\* – Modular testbed for embeddings, retrieval, and QA  

\- \*\*Education\*\* – Demonstrates cross-lingual NLP in a reproducible setup  



---



\## ⚠️ Limitations



\- Limited to dataset coverage  

\- Extractive answers restrict response flexibility  

\- Translation quality depends on backend  



Despite these limitations, the system provides a strong, reproducible baseline for multilingual RAG in constrained environments.



---



\## 📁 Project Structure



```

multilingual-rag-msr/

│

├── src/

│   ├── load\_dataset.py        # Dataset ingestion

│   ├── preprocess.py          # Data cleaning

│   ├── build\_index.py         # Embedding + FAISS indexing

│   ├── retrieve.py            # Semantic retrieval

│   └── rag\_answer.py          # End-to-end QA + translation

│

├── requirements.txt

├── README.md

└── .gitignore

```



---



\## 📜 License



Released for research and educational use. Attribution is requested for academic or derivative work.



---



\## 📖 How to Cite



```bibtex

@software{multilingual\_rag\_qa,

&nbsp; author = {Ajeet Kartikay},

&nbsp; title = {Multilingual Retrieval-Augmented Question Answering},

&nbsp; year = {2026},

&nbsp; url = {https://github.com/ajeetkartikay/multilingual-rag-msr}

}

```



---



\## 🙏 Acknowledgments



This project builds upon open-source research in multilingual representation learning and semantic retrieval, including:



\- \*\*FAISS\*\* for efficient vector search  

\- \*\*Sentence-Transformers\*\* for multilingual embeddings  

\- \*\*Hugging Face Datasets \& Transformers\*\* ecosystems  



