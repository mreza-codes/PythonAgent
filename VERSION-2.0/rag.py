import chromadb

client = chromadb.PersistentClient(path="data/chroma_db")
collection = client.get_collection("python_docs")

def get_context(query, top_k=5):
    results = collection.query(
        query_texts=[query],
        n_results=top_k,
        include=["documents"]
    )

    docs = results["documents"][0]
    return "\n\n".join(docs)
