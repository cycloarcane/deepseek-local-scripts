import os
import json
import requests
import subprocess
from datetime import datetime
import re

# Configuration using environment variables
API_ENDPOINT = os.getenv("LOCAL_LLM_API", "http://127.0.0.1:5000/v1/chat/completions")
GITHUB_REPO_PATH = os.path.expanduser(os.getenv("GITHUB_REPO_PATH", "~/Documents/deepseek-local-scripts"))
SCRIPTS_DIR = os.getenv("SCRIPTS_DIR", "terminal_art")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN", "")

# Validate required environment variables
required_vars = ["LOCAL_LLM_API", "GITHUB_REPO_PATH", "GITHUB_TOKEN"]
for var in required_vars:
    if not os.getenv(var):
        raise ValueError(f"Environment variable {var} is not set.")

def generate_terminal_art():
    prompt = "Generate a Python script that creates fun terminal ASCII art. Focus on colorful and dynamic elements. Output only the code, no explanations."
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "mode": "instruct"
    }
    try:
        response = requests.post(API_ENDPOINT, headers=headers, json=data)
        response.raise_for_status()
        response_json = response.json()
        if "choices" not in response_json or len(response_json["choices"]) == 0:
            print("No content found in API response.")
            return None
        content = response_json["choices"][0]["message"]["content"]
        # Use regex to extract Python code blocks
        script_content = re.findall(r'```python(.*?)```', content, re.DOTALL)
        if script_content:
            script_content = script_content[0].strip()
        else:
            script_content = content.strip()  # fallback if no code block found
        return script_content
    except requests.exceptions.RequestException as e:
        print(f"Error making API request: {e}")
        return None
    except (KeyError, IndexError) as e:
        print(f"Error processing API response: {e}")
        return None

def save_script(script_content):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    script_name = f"terminal_art_{timestamp}.py"
    script_path = os.path.join(GITHUB_REPO_PATH, SCRIPTS_DIR, script_name)
    try:
        with open(script_path, "w") as f:
            f.write(script_content)
        print(f"Script saved to: {script_path}")
        return script_path
    except Exception as e:
        print(f"Error saving script: {e}")
        return None

def push_to_github(script_path):
    try:
        os.chdir(GITHUB_REPO_PATH)
        # Use subprocess for better control and error handling
        subprocess.run(["git", "add", script_path], check=True)
        commit_message = f"Add new terminal art script {os.path.basename(script_path)}"
        subprocess.run(["git", "commit", "-m", commit_message], check=True)
        subprocess.run(["git", "push", "origin", "main"], check=True)
        print("Script pushed to GitHub successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error pushing to GitHub: {e}")
    except Exception as e:
        print(f"Error during Git operations: {e}")

def main():
    scripts_dir = os.path.join(GITHUB_REPO_PATH, SCRIPTS_DIR)
    os.makedirs(scripts_dir, exist_ok=True)
    print(f"Scripts will be saved to: {scripts_dir}")

    script_content = generate_terminal_art()
    if script_content:
        script_path = save_script(script_content)
        if script_path:
            push_to_github(script_path)

if __name__ == "__main__":
    main()