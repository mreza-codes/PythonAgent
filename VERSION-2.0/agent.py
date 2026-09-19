import json
import re
from model_client import ask_model
from rag import get_context
from memory_store import MemoryStore
from tools import retrieval, keyword_search


# Parse model output into structured fields
def parse_model_output(output):
    thought_match = re.search(r"Thought:(.*)", output)
    action_match = re.search(r"Action:(.*)", output)
    input_match = re.search(r"Action Input:(.*)", output)
    final_match = re.search(r"Final Answer:(.*)", output)

    thought = thought_match.group(1).strip() if thought_match else None
    action = action_match.group(1).strip() if action_match else None
    action_input = input_match.group(1).strip() if input_match else None
    final_answer = final_match.group(1).strip() if final_match else None

    # Convert JSON input to Python dict
    if action_input:
        try:
            action_input = json.loads(action_input)
        except:
            action_input = None

    return thought, action, action_input, final_answer



class Agent:
    def __init__(self):
        self.memory = MemoryStore()


    # Execute the selected tool
    def execute_action(self, action, action_input):
        # Try to ensure action_input is a dict
        if isinstance(action_input, str):
            try:
                action_input = json.loads(action_input)
            except:
                return "Invalid action input. Expected JSON."

        if not isinstance(action_input, dict):
            return "Invalid action input. Expected JSON object."

        if action == "retrieval":
            query = action_input.get("query", "")
            return retrieval(query)

        elif action == "keyword_search":
            keywords = action_input.get("keywords", "")
            return keyword_search(keywords)

        elif action == "final_answer":
            return None

        else:
            return f"Unknown action: {action}"




    # Main agent loop
    def ask(self, question):
        self.memory.add("history", {"user": question})

        # Initial retrieval
        context = get_context(question)
        self.memory.add("retrievals", context)

        # Initial thought
        thought = f"Retrieved {len(context.split())} words of context."
        self.memory.add("thoughts", thought)

        # First prompt
        prompt = self.build_prompt(question, context)

        # Agent Loop (max 5 steps)
        for step in range(5):
            output = ask_model(prompt)
            thought, action, action_input, final_answer = parse_model_output(output)

            # Save thought
            if thought:
                self.memory.add("thoughts", thought)

            # If final answer → stop
            if final_answer:
                self.memory.add("history", {"assistant": final_answer})
                return final_answer

            # Execute tool
            observation = self.execute_action(action, action_input)

            # Save observation
            self.memory.add("observations", observation)

            # Build next prompt
            prompt = self.build_prompt(question, observation)

        return "I don't know."




    # Build prompt for each loop step
    def build_prompt(self, question, observation):
        return f"""
You are an Agentic RAG system designed to answer Python questions step-by-step.

User Question:
{question}

Latest Observation:
{observation}

You MUST follow this exact format:

Thought: <explain your reasoning, break the question into parts, decide what to do next>
Action: <one of ["retrieval", "keyword_search", "final_answer"]>
Action Input: <valid JSON object>

Rules:
- Always break complex questions into smaller parts inside Thought.
- Thought MUST explain why you choose the next action.
- Action MUST be one of the allowed actions.
- Action Input MUST be valid JSON.
- Use retrieval for semantic search.
- Use keyword_search for exact lookup.
- If you have enough information, use final_answer.
- Never hallucinate.
- Never skip the required format.

If you are ready to answer the user, output:

Final Answer: <your complete answer>
"""







