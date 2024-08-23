from src.design_feedback import DesignFeedbackSystem
from src.utils import save_feedback
import os

def main():
    # Initialize the Design Feedback System
    system = DesignFeedbackSystem()

    # Specify the design file to analyze
    design_file = 'data/sample_designs/design1.json'

    # Check if the design file exists
    if not os.path.exists(design_file):
        print(f"Design file {design_file} not found.")
        return

    # Analyze the design
    print(f"Analyzing design from {design_file}...")
    feedback = system.analyze_design(design_file)

    # Specify the output file path
    output_file = 'output/feedback.json'

    # Ensure the output directory exists
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    # Save the feedback to a file
    save_feedback(feedback, output_file)

    print(f"Feedback saved to {output_file}.")

if __name__ == "__main__":
    main()
