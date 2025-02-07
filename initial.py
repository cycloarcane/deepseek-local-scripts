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
    prompt = """As an expert script developer, think through creating a Python script 
that generates colorful and dynamic terminal ASCII art. 
First, outline your approach and considerations, then 
provide a descriptive title inside <script_title></script_title> tags, 
followed by the complete Python script code within 
```python triple backticks."""  
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
            return None, None  
        content = response_json["choices"][0]["message"]["content"]  

        # Extract script title  
        title_match = re.search(r'<script_title>(.*?)</script_title>', content, re.DOTALL)  
        script_title = title_match.group(1).strip() if title_match else None  

        # Extract Python code blocks  
        script_content = re.findall(r'```python(.*?)```', content, re.DOTALL)  
        if script_content:  
            script_content = script_content[0].strip()  
        else:  
            script_content = content.strip()  # fallback if no code block found  
        return script_content, script_title  
    except requests.exceptions.RequestException as e:  
        print(f"Error making API request: {e}")  
        return None, None  
    except (KeyError, IndexError) as e:  
        print(f"Error processing API response: {e}")  
        return None, None  

def save_script(script_content, script_title=None):  
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")  
    if script_title:  
        clean_title = re.sub(r'[^\w\-_.]', '', script_title.replace(' ', '_'))  
        script_name = f"{clean_title + timestamp}.py"  
    else:  
        script_name = f"{timestamp}.py"  
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

    script_content, script_title = generate_terminal_art()  
    if script_content:  
        script_path = save_script(script_content, script_title)  
        if script_path:  
            push_to_github(script_path)  

if __name__ == "__main__":  
    main()  