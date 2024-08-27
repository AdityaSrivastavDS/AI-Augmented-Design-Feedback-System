import json
import numpy as np

def load_design(design_path):
    with open(design_path, 'r') as f:
        return json.load(f)

def save_feedback(feedback, output_path):
    # Function to convert numpy types to native Python types
    def convert_to_python_types(obj):
        if isinstance(obj, dict):
            return {k: convert_to_python_types(v) for k, v in obj.items()}
        elif isinstance(obj, list):
            return [convert_to_python_types(i) for i in obj]
        elif isinstance(obj, (np.int64, np.float64)):  # Add more types if needed
            return int(obj) if isinstance(obj, np.int64) else float(obj)
        return obj

    # Convert feedback to native Python types
    feedback = convert_to_python_types(feedback)

    # Save to JSON file
    with open(output_path, 'w') as f:
        json.dump(feedback, f, indent=4)
