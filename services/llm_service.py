import json

import requests
import time

OLLAMA_URL = "http://localhost:11434"
OLLAMA_MODEL = "llama3"

def get_answer_from_ollama(prompt: str) -> str:
    payload = {
        "model": OLLAMA_MODEL,
        "prompt": prompt,
        "stream": True
    }

    try:
        response = requests.post(OLLAMA_URL, json=payload, stream=True, timeout=60)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        return f"Error communicating with Ollama: {e}"

    final_response = ""
    start_time = time.time()

    try:
        for line in response.iter_lines(decode_unicode=True):
            if time.time() - start_time > 60:
                return "Error: Max wait time of 1 minute exceeded."

            if line:
                try:
                    data = json.loads(line.strip())
                    final_response += data.get("response", "")
                    if data.get("done", False):
                        break
                except ValueError as ve:
                    return f"Error parsing JSON: {ve} - Raw Line: {line}"
    except Exception as ex:
        return f"Streaming error: {ex}"

    return final_response or "No response received from model."
