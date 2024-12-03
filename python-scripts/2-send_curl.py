import json
import subprocess
import os

# Read the project name and description from the environment variables
project_name = os.environ.get('PROJECT_NAME')
project_description = os.environ.get('PROJECT_DESCRIPTION')

print(f"Project Name: {project_name}")
print(f"Project Description: {project_description}")
# Read the stack details from stack.json
with open('stack.json', 'r') as f:
    stack_data = json.load(f)

# Extract the technology and libraries from the stack data
technology = stack_data.get("technology")
libraries = stack_data.get("libraries")

# Define the URL based on the technology (e.g., react, nodejs, etc.)
url = f"https://bridge.production.services.oneportal.vodafone.com/bridge/api/{technology.lower()}"

# Build the payload for the request
payload = {
    "projectDetails": {
        "name": project_name,
        "description": project_description
    },
    "coreOptions": {
        "includeExampleApp": True,
        "monoRepoOption": "STANDARD_APP",
        "djrEnabled": False,
        "djrApiUrl": "https://api.example.com"
    },
    "libraries": libraries,
    "technology": technology.lower()
}

# Prepare the curl command
curl_command = [
    "curl", "-X", "POST", "--output", f"{technology.lower()}.zip",
    url, "-H", "Content-Type: application/json",
    "-d", json.dumps(payload)
]

# Print the curl command for debugging/logging
print(f"Executing curl command: {' '.join(curl_command)}")

# Execute the curl command
subprocess.run(curl_command)
