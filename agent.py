from model_client import ask_model
from rag import get_context

class Agent:
    def ask(self, question):
        context = get_context(question)

        prompt = f"""
You are a Python documentation assistant.

Answer the question ONLY using the context below.
If the answer is not in the context, say "I don't know".

### CONTEXT START
{context}
### CONTEXT END

### QUESTION
{question}

### ANSWER
"""

        return ask_model(prompt)
