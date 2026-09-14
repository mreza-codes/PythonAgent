import os

BASE_DIR = "python-3.14-docs-text"
OUTPUT_FILE = "python_docs_merged.txt"

def read_all_text_files(base_dir):
    merged_text = ""

    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith(".txt"):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        merged_text += f"\n\n=== FILE: {file_path} ===\n\n"
                        merged_text += f.read()
                except:
                    print(f"Could not read: {file_path}")

    return merged_text

if __name__ == "__main__":
    text = read_all_text_files(BASE_DIR)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as out:
        out.write(text)

    print("DONE — merged file created:", OUTPUT_FILE)
