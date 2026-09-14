# Python AI Agent (with Optional RAG Support)

A lightweight Python AI Agent built with **PyQt6**, designed for fast local execution and optional **Retrieval-Augmented Generation (RAG)**.  
This project includes a complete data‑processing pipeline for building a local vector database using **ChromaDB**, allowing the agent to answer questions using Python documentation or any custom dataset.

---

## 📸 Screenshot

Below is a preview of the application's interface:

![Screenshot](./screenshot.png)

---

## 📚 Project Features

### 🔹 PyQt6 Desktop Application  
A clean and responsive UI built with PyQt6, packaged as a simple `.pyw` launcher so it runs without opening a console window.

### 🔹 Optional RAG System  
Includes a full pipeline for:

- Merging raw documentation  
- Chunking text  
- Generating embeddings  
- Building a ChromaDB vector database  
- Querying the database inside the agent

### 🔹 Local & Fast  
Designed to work with local LLM runtimes (e.g., Bionic) for fast inference without external API dependencies.

---

## 📁 Repository Structure

```
python-agent/
│
├── main.py
├── main.pyw
├── agent.py
├── rag.py
├── config.py
├── ui_main.py
├── icon.ico
├── screenshot.png
│
├── data/
│   ├── python_docs_merged.txt
│   ├── python_docs_chunks.txt
│   ├── python-3.14-docs-text/   # Raw documentation files
│   ├── chunk_docs.py
│   ├── merge_docs.py
│   ├── build_embeddings.py
│   ├── build_vector_db.py
│   └── check_collections.py
│
└── README.md
```

---

## 📥 Download Python Documentation (Raw Source)

Instead of uploading large text files directly, you can download the official Python documentation archive here:

🔗 **Python 3.14 Text Documentation**  
https://docs.python.org/3/archives/python-3.14-docs-text.zip

Extract the archive into:

```
data/python-3.14-docs-text/
```

Then run the data‑processing scripts to rebuild the vector database.

---

## 🔧 Building the Vector Database

After placing the documentation files inside `data/python-3.14-docs-text/`, run the following scripts in order:

### 1️⃣ Merge raw docs  
```
python data/merge_docs.py
```

### 2️⃣ Chunk merged text  
```
python data/chunk_docs.py
```

### 3️⃣ Generate embeddings  
```
python data/build_embeddings.py
```

### 4️⃣ Build ChromaDB vector database  
```
python data/build_vector_db.py
```

This will create a local vector database that the agent can use for RAG‑based answering.

---

## 🚀 Running the Application

Use the `.pyw` launcher to run the app **without opening a console window**:

```
main.pyw
```

Or run normally:

```
python main.py
```

---

## 🧹 Notes

- The folder `chroma_db/` is **not included** in the repository because it is generated locally.
- Users can rebuild the database using the provided scripts.
- No external APIs are required unless you choose to integrate them.

---

## 📄 License

This project is open‑source and free to use for learning, experimentation, and personal development.



این پروژه یک دستیار هوشمند است که با ظاهر ساده و روان اجرا می‌شود و هدف آن کمک به کاربر در انجام کارهای متنی و پاسخ‌گویی دقیق است. این برنامه توانایی تحلیل و درک نوشته‌ها را دارد و می‌تواند متن‌های بزرگ را پردازش کرده و از آن‌ها برداشت‌های معنایی بسازد.

این دستیار امکان استفاده از مجموعه‌ای بزرگ از نوشته‌های آموزشی را فراهم می‌کند تا کاربر بتواند یک پایگاه داده‌ی محلی ایجاد کند. این پایگاه داده به برنامه کمک می‌کند تا پاسخ‌های دقیق‌تر و مرتبط‌تری ارائه دهد و در پرسش و پاسخ‌های آموزشی عملکرد بهتری داشته باشد.

هدف اصلی این پروژه ساخت یک ابزار کاربردی، سبک و قابل اعتماد است که بتواند در یادگیری، جست‌وجو و کار با متن‌های آموزشی همراه کاربر باشد.
