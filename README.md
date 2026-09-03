# AI Chatbot Backend

Flask-based REST API backend service for AI Chatbot / Skillbot Academy integration with OpenAI API.

## Features
- Flask REST API with `/generate` endpoint
- Environment variable configuration (`python-dotenv`)
- Integration with OpenAI API for text completions

## Quick Start

### 1. Installation
```bash
python -m venv chatbot_venv
# On Windows:
.\chatbot_venv\Scripts\activate
# On Linux/Mac:
source chatbot_venv/bin/activate

pip install -r requirements.txt
```

### 2. Configuration
Copy `config.env.example` to `config.env` and set your OpenAI API Key:
```env
OPENAI_API_KEY=your_openai_api_key_here
```

### 3. Running the Backend
```bash
python server.py
```
The server will run on `http://127.0.0.1:5000`.

### 4. Testing
```bash
python test_request.py
```
