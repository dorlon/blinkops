# Handles importing the form (JSON/YAML)
import json
import yaml
import os

def load_form(file_path):
    # Check if the file exists before attempting to open it
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    _, file_extension = os.path.splitext(file_path)  # Get the file extension
    with open(file_path, 'r') as f:
        if file_extension == '.json':
            return json.load(f)  # Load JSON file
        elif file_extension in ['.yaml', '.yml']:
            return yaml.safe_load(f)  # Load YAML file
        else:
            raise ValueError("Unsupported file format. Only JSON and YAML are supported.")  # Handle unsupported formats
