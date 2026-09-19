import requests
from config import BIONIC_URL, MODEL_NAME

def ask_model(prompt):
    payload = {
        "model": MODEL_NAME,
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(BIONIC_URL, json=payload)
    data = response.json()

    return data["choices"][0]["message"]["content"]
