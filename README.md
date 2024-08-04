# ai-ollama-py

## Project Description
ai-ollama-py is a Flask server built with Python 3.10 that processes JSON payloads containing `context` and `prompt` strings. The server interacts with Ollama on port 11434 and exposes three endpoints:

- `/api/admin_engine`
- `/api/arc_engine`
- `/api/api_engine`

### Sample JSON Payload
The server expects a JSON payload in the following format:

```json
  {
    "context": "your context here",
    "prompt": "your prompt here"
  }
```


## Prerequisites

1. **Python 3.10**:
   Ensure you have Python 3.10 installed. You can download it from the [official Python website](https://www.python.org/downloads/release/python-3100/).

2. **Ollama**:
   Ollama is a dependency for this project. It's recommended to run Ollama on a machine with a GPU for better performance, but there is also a Dockerized option.

## Setup

### Ollama Installation

1. **Download Ollama**:
   ```bash
   curl -fsSL https://ollama.com/install.sh | sh
   ```

2. **Run Ollama**:
   After installation, start the Ollama server by running the following command in your terminal:
   ```bash
   ollama serve
   ```

3. **Pull Llama3**:
    ```bash 
    ollama pull llama3
    ```
   *Pulling llama3 for the first time may take a few minutes  

****Please note that ollama runs best on a machine with a dedicated GPU, you may run this on a CPU only machine but expect slower response times**

### Install Python Requirements
1. Use python 3.10
2. Run  
    ```bash
    python -m pip install -r requirements.txt
   ```
### Run The Server  
```bash
  python main.py  
   ```
query example
```bash
curl -X POST -H "Content-Type: application/json" -d '{"context": "block ui","prompt": "How can i create a volume using the ui"}' http://0.0.0.0:8087/api/admin_engine  
```

### Contact ###  
 [Tomer Gafsou](mailto:tomer.gafsou@dell.com)
 

## LOCAL TO BE REMOVED
```shell
export INGEST_DIR=/home/danduh/dev/mist-portal-nrwl/apps/portal-e2e/
python3 main.py
----
OLLAMA_HOST=0.0.0.0 ollama serve
```

```json

{
  "model": "gpt-4-turbo",
  "temperature": 0.1,
  "messages": [
    {
      "role": "system",
      "content": ""
    },
    {
      "role": "user",
      "content": "Create Page Object class with name . \n INPUT>>:  <<INPUT  \n undefined"
    }
  ]
}

```