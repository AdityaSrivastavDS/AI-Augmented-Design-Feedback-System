import json

def load_design(design_path):
    with open(design_path, 'r') as f:
        return json.load(f)

def save_feedback(feedback, output_path):
    with open(output_path, 'w') as f:
        json.dump(feedback, f, indent=4)
