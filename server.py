from flask import Flask, request, jsonify
import requests
import os
from dotenv import load_dotenv

# Load environment variables from config.env file
load_dotenv()

app = Flask(__name__)

# Home route to check if the server is running
@app.route('/')
def home():
    return "Hello, this is the AI Chatbot Backend!"

# Create an API route to handle GPT requests
@app.route('/generate', methods=['POST'])
def generate_response():
    data = request.json
    user_prompt = data.get('prompt')

    if not user_prompt:
        return jsonify({"error": "No prompt provided"}), 400

    # Sending request to OpenAI API (or replace with your GPT API)
    response = requests.post(
        'https://api.openai.com/v1/engines/davinci/completions',
        headers={
            'Authorization': f'Bearer {os.getenv("OPENAI_API_KEY")}'
        },
        json={
            'prompt': user_prompt,
            'max_tokens': 150,
            'temperature': 0.7,
        }
    )

    # Check for errors in the response
    if response.status_code != 200:
        return jsonify({"error": "Failed to connect to GPT API"}), 500

    # Get the GPT response and return it
    gpt_response = response.json()['choices'][0]['text']
    return jsonify({"response": gpt_response})

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
@app.route('/generate', methods=['POST'])
def generate_response():
    data = request.json
    user_prompt = data.get('prompt')

    if not user_prompt:
        return jsonify({"error": "No prompt provided"}), 400

    # Return a test response instead of calling the OpenAI API
    return jsonify({"response": f"Received prompt: {user_prompt}"}), 200
print(f"Loaded API Key: {os.getenv('config')}")
import os
import openai

# Retrieve API key from system environment variables
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("API key not found. Please set the OPENAI_API_KEY environment variable.")

# Set the API key for OpenAI
openai.api_key = api_key

# Now you can make API calls
response = openai.Completion.create(
  engine="davinci",
  prompt="Tell me a joke",
  max_tokens=50
)

print(response.choices[0].text.strip())
