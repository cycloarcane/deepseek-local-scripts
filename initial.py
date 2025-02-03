import openai
import os
import requests
from datetime import datetime

# Configuration
GITHUB_REPO = "cycloarcane/deepseek-local-scripts"
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")  # Ensure this is set in environment variables
LLM_ENDPOINT = "http://127.0.0.1:5000/v1/"

# Initialize OpenAI client
openai.api_base = LLM_ENDPOINT
client = openai.Client()

def generate_random_script():
    try:
        # Generate the script using the LLM
        response = client.chat.completions.create(
            model="deepseek-ai_DeepSeek-R1-Distill-Qwen-32B",  # Adjust based on your local LLM
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Write a random Python script that demonstrates a useful feature."}
            ],
            temperature=0.7,
            max_tokens=500
        )

        content = response.choices[0].message['content']
        return content

    except Exception as e:
        print(f"Error generating script: {e}")
        return None

def save_script_to_file(script_content):
    try:
        # Create a filename based on current time to avoid duplicates
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"random_script_{timestamp}.py"

        with open(filename, 'w') as f:
            f.write(script_content)
        return filename

    except Exception as e:
        print(f"Error saving script: {e}")
        return None

def upload_to_github(filename):
    try:
        # Read the file content
        with open(filename, 'rb') as f:
            content = f.read()

        # Construct the API URL
        api_url = f"https://api.github.com/repos/{GITHUB_REPO}/contents/{filename}"

        # Prepare the data payload
        data = {
            "path": filename,
            "content": content.decode('utf-8'),
            "message": f"Upload random script {filename}",
            "branch": "main"
        }

        # Make the authenticated request
        headers = {
            "Authorization": f"token {GITHUB_TOKEN}",
            "Content-Type": "application/json"
        }

        response = requests.post(api_url, json=data, headers=headers)

        if response.status_code == 201:
            print(f"Successfully uploaded {filename} to GitHub.")
        else:
            print(f"Upload failed: {response.text}")

    except Exception as e:
        print(f"Error uploading to GitHub: {e}")

def main():
    script_content = generate_random_script()
    if script_content:
        filename = save_script_to_file(script_content)
        if filename:
            upload_to_github(filename)

if __name__ == "__main__":
    main()
