# Gen-AI-Dashboard

This project demonstrates a full pipeline for generating answers to user questions using an open-source LLM (Ollama), converting text to speech with Coqui TTS, and serving both text and audio via a FastAPI backend.

## Table of Contents

* [Prerequisites](#prerequisites)
* [Environment Setup](#environment-setup)
* [Installing Dependencies](#installing-dependencies)
* [Ollama Setup](#ollama-setup)
* [Project Structure](#project-structure)
* [Running the Application](#running-the-application)
* [API Endpoints](#api-endpoints)
* [Testing with cURL](#testing-with-curl)
* [Next Steps](#next-steps)

## Prerequisites

* macOS with Python 3.10 (or 3.11) installed
* Ollama CLI installed and a model pulled (e.g., `llama3`)
* Git for version control

## Environment Setup

1. **Install Python 3.10 (or 3.11)**

   * Download from [python.org](https://www.python.org/downloads/)
   * Verify:

     ```bash
     python3.10 --version
     ```

2. **Create a Virtual Environment**

   ```bash
   python3.10 -m venv venv
   source venv/bin/activate
   pip install --upgrade pip
   ```

## Installing Dependencies

With the virtual environment activated, install required packages:

```bash
pip install fastapi uvicorn requests TTS
```

This installs:

* **FastAPI**: Web framework
* **Uvicorn**: ASGI server for FastAPI
* **requests**: HTTP client for Python
* **TTS**: Coqui TTS for text-to-speech

## Ollama Setup

1. **Install Ollama CLI** (via Homebrew or direct download)

   ```bash
   brew install ollama
   ```

2. **Pull and run the `llama3` model**

   ```bash
   ollama pull llama3
   ollama run llama3
   ```

   * The server listens on `http://127.0.0.1:11434`

## Project Structure

```
Gen-AI-Dashboard/
├── main.py           # FastAPI application
├── services/
│   ├── llm_service.py  # Interacts with Ollama and streams responses
│   └── tts_service.py  # Converts text to speech using Coqui TTS
├── audio_outputs/    # Directory for generated audio files
├── venv/             # Python virtual environment
└── README.md         # Project documentation
```

## Running the Application

Start the local FastAPI server:

```bash
uvicorn main:app --reload
```

The API documentation is available at `http://127.0.0.1:8000/docs`.

## API Endpoints

* **POST** `/generate-answer`

  * Request body: `{ "question": "<your question>" }`
  * Response:

    ```json
    {
      "question": "<your question>",
      "answer": "<generated text answer>",
      "audio_url": "/audio/<uuid>.wav"
    }
    ```

* **GET** `/audio/{filename}`

  * Serves the generated `.wav` audio file

## Testing with cURL

```bash
curl -X POST http://127.0.0.1:8000/generate-answer \
     -H "Content-Type: application/json" \
     -d '{"question":"What is Generative AI?"}'
```

## Next Steps

* Implement automatic cleanup of old audio files
* Integrate video generation based on answer text
* Add frontend UI (React or Streamlit) to interact with the API
* Enhance LLM service to support additional models and error handling


IDE used - PyCharm CE
