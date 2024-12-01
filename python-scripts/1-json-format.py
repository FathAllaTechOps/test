import re

# Read the input JSON
with open('language_setup.json', 'r') as f:
    data = f.read()

# Add quotes around array elements
data = re.sub(r'(\[[^\]]+\])', lambda match: '[' + ', '.join(f'"{item.strip()}"' for item in match.group(0)[1:-1].split(',')) + ']', data)

# Add quotes around keys and values
data = re.sub(r'([a-zA-Z0-9_]+):', r'"\1":', data)  # Fix keys
data = re.sub(r': ([a-zA-Z0-9_]+)', r': "\1"', data)  # Fix values

# Write the corrected JSON to a new file
with open('formatted_language_setup.json', 'w') as f:
    f.write(data)

print("Fixed JSON written to 'formatted_language_setup.json'.")
