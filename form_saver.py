# Handles saving or printing the results
import json
import yaml
import os

def save_results(results, file_path=None):
    # Print the results to the terminal
    print("\nThank you for filling the form! Here are your filled form results:")
    print(json.dumps(results, indent=2))  # Pretty-printing the results in JSON format

    # Optionally save to file if the user requests it
    if file_path:
        _, file_extension = os.path.splitext(file_path)  # Get the file extension
        with open(file_path, 'w') as f:
            if file_extension == '.json':
                json.dump(results, f, indent=2)  # Save as JSON
            elif file_extension in ['.yaml', '.yml']:
                yaml.dump(results, f)  # Save as YAML
            else:
                raise ValueError("Unsupported file format for saving.")  # Handle unsupported formats
        print(f"Results saved to {file_path}")  # Confirmation message
