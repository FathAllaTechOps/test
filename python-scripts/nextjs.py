import json
import subprocess
import os

# Read the stack details from stack.json
with open('stack.json', 'r') as f:
    stack_data = json.load(f)

# Extract project details from stack.json
project_name = stack_data.get("project_name")
project_description = stack_data.get("project_description")

# Extract technology and libraries
technology = "nextjs"  # Based on your input, we know it's Next.js
libraries = stack_data.get("libraries", [])

# Define core options (Next.js specific options)
core_options = {
    "includeExampleApp": True,
    "appExample": True,
    "projectDescription": project_description,
    "projectName": project_name
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

# API Endpoint for Next.js
url = f"https://bridge.production.services.oneportal.vodafone.com/bridge/api/{technology}"

# Execute curl command
curl_command = [
    "curl", "-X", "POST", "--output", f"{technology}.zip",
    url, "-H", "Content-Type: application/json",
    "-d", json.dumps(payload)
]

print(f"Executing: {' '.join(curl_command)}")
subprocess.run(curl_command)
