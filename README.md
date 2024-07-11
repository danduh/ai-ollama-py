# pfmp-sage

## Project Description
pfmp-sage is a Flask server built with Python 3.10 that processes JSON payloads containing `context` and `prompt` strings. The server interacts with Ollama on port 11434 and exposes three endpoints:

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

## Use with Continue plugin
1. Add the config file
```bash
vim ~/.continue/config.ts 
```
2. paste the following
```typescript
export function modifyConfig(config) {
  config.models.push({
    options: {
      title: "Sage",
      model: "customModel",
    },
    streamChat: async function* (prompt, options) {
       const requestBody = {
        prompt: prompt
      };

      // Make the API call
      const response = await fetch('http://0.0.0.0:8087/api/consolidated_engine', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          // Add other headers if needed
        },
        body: JSON.stringify(requestBody),
      });

      if (!response.ok) {
        throw new Error(`API call failed: ${response.statusText}`);
      }
      const reader = response.body.getReader();
      const decoder = new TextDecoder('utf-8');
      let done = false;

      while (!done) {
        const { value, done: readerDone } = await reader.read();
        done = readerDone;
        const chunk = decoder.decode(value, { stream: !done });
        // Yield each part of the completion as it is streamed
        yield chunk;
      }
    },
  });
  return config;
}
```
3. Restart your IDE
4. Choose the Sage model to work with Continue

### Contact ###  
 [Tomer Gafsou](mailto:tomer.gafsou@dell.com)