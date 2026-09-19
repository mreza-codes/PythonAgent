from rag import get_context

def retrieval(query):
    return get_context(query)

def keyword_search(keywords):
    with open("data/python_docs_chunks.txt", "r", encoding="utf-8") as f:
        chunks = f.read().split("\n\n")  # هر چانک جداست

    results = []

    for kw in keywords.split():
        for chunk in chunks:
            if kw.lower() in chunk.lower():
                results.append(chunk.strip())

    if not results:
        return "No relevant text found."

    return "\n\n---\n\n".join(results)

