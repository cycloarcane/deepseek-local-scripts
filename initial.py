import requests
import git
# Make a request to the LLM to generate a novel script
url = 'http://127.0.0.1:5000/v1/'
data = {
    "prompt": "Write a Python script that has never been written before."
}
response = requests.post(url, json=data)
script = response.text
# Create a Git repository and add the generated script to it
repo = git.Repo.init()
repo.git.add(A=".")
repo.git.commit(m="Initial commit")
# Add the generated script to the repository and commit
repo.git.add(A=".")
repo.git.commit(m="Added generated script")
# Push the changes to GitHub
origin = repo.create_remote('origin', 'https://github.com/cycloarcane/deepseek-local-scripts.git')
origin.push()
