import os

INPUT_FILE = "python_docs_merged.txt"
OUTPUT_FILE = "python_docs_chunks.txt"

CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200

def chunk_text(text, chunk_size=CHUNK_SIZE, overlap=CHUNK_OVERLAP):
    chunks = []
    start = 0
    text_length = len(text)

    while start < text_length:
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        start = end - overlap  # move back for overlap

    return chunks

if __name__ == "__main__":
    # Read merged file
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        full_text = f.read()

    # Chunking
    chunks = chunk_text(full_text)

    # Save chunks into one file (optional)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as out:
        for i, chunk in enumerate(chunks):
            out.write(f"\n\n=== CHUNK {i} ===\n\n")
            out.write(chunk)

    print(f"Done! Total chunks created: {len(chunks)}")
    print("Saved to:", OUTPUT_FILE)
