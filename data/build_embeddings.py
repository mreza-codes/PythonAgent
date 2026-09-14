print("STEP 1")
import chromadb
print("STEP 2")
from sentence_transformers import SentenceTransformer
print("STEP 3")
import torch
print("STEP 4")

print("STEP 5")
client = chromadb.PersistentClient(path="chroma_db")
collection = client.get_collection("python_docs")
print("STEP 6")

print("STEP 7")
results = collection.get(include=["documents"])
docs = results["documents"]
ids = results["ids"]
print("STEP 8")

print("STEP 9")
device = "cuda" if torch.cuda.is_available() else "cpu"
print("Using device:", device)

print("STEP 10")
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2", device=device)

print("STEP 11")
embeddings = model.encode(docs, batch_size=64, convert_to_numpy=True)

print("STEP 12")
# --- حل مشکل batch size ---
MAX_BATCH = 5000
total = len(ids)

for i in range(0, total, MAX_BATCH):
    batch_ids = ids[i:i+MAX_BATCH]
    batch_emb = embeddings[i:i+MAX_BATCH]
    print(f"Updating batch {i} to {i+len(batch_ids)}")
    collection.update(ids=batch_ids, embeddings=batch_emb)

print("DONE")
