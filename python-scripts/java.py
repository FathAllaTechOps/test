import json
import subprocess
import os

# Read the stack details from stack.json
with open('stack.json', 'r') as f:
    stack_data = json.load(f)

# Extract project details from stack.json
project_name = os.environ.get('PROJECT_NAME')
project_description = os.environ.get('PROJECT_DESCRIPTION')

# Extract technology and libraries
technology = "java"  # Based on your input, we know it's Java
libraries = stack_data.get("libraries", [])

# Define core options (Java specific options)
core_options = {
    "includeExampleApp": True,
    "javaVersion": stack_data.get("javaVersion", 17),
    "packageName": stack_data.get("packageName", "com.example.vhub.java")
}

# Prepare the payload
payload = {
    "projectDetails": {
        "name": project_name,
        "description": project_description
    },
    "coreOptions": core_options,
    "libraries": libraries,
    "technology": technology
}

# API Endpoint for Java
url = f"https://bridge.production.services.oneportal.vodafone.com/bridge/api/{technology}"

# Execute curl command
curl_command = [
    "curl", "-X", "POST", "--output", f"{technology}.zip",
    url, "-H", "Content-Type: application/json",
    "-d", json.dumps(payload)
]

print(f"Executing: {' '.join(curl_command)}")
subprocess.run(curl_command)
