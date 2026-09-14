import os
import chromadb

DB_DIR = "chroma_db"                     
DATA_DIR = "python-3.14-docs-text"       

client = chromadb.PersistentClient(path=DB_DIR)

collection = client.get_or_create_collection(
    name="python_docs",
    metadata={"hnsw:space": "cosine"}
)

docs = []
ids = []

print("Loading documents...")

for filename in os.listdir(DATA_DIR):
    path = os.path.join(DATA_DIR, filename)
    if not filename.endswith(".txt"):
        continue

    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    docs.append(text)
    ids.append(filename)

print("Total docs:", len(docs))

collection.add(
    documents=docs,
    ids=ids
)

print("DONE: Collection created and documents added.")
