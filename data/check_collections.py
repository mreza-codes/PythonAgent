import chromadb

client = chromadb.PersistentClient(path="data/chroma_db")
print("Collections:", client.list_collections())
