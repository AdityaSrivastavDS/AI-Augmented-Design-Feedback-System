import json
from .simulation import simulate_design
from .predictive_modeling import evaluate_performance, evaluate_safety, evaluate_efficiency

import pandas as pd
import json
import joblib

class DesignFeedbackSystem:
    def __init__(self):
        # Load models
        self.performance_model = joblib.load('E:\\Aditya\\Projects\\AI_Augmented_Design_Feedback_System\\models\\performance_model.pkl')
        self.safety_model = joblib.load('E:\\Aditya\\Projects\\AI_Augmented_Design_Feedback_System\\models\\safety_model.pkl')
        self.efficiency_model = joblib.load('E:\\Aditya\\Projects\\AI_Augmented_Design_Feedback_System\\models\\efficiency_model.pkl')

    def analyze_design(self, design_file):
        # Load the JSON file
        with open(design_file, 'r') as f:
            design = json.load(f)

        # Transform JSON to DataFrame for each model
        performance_input = self.transform_json_to_dataframe_performance(design)
        safety_input = self.transform_json_to_dataframe_safety(design)
        efficiency_input = self.transform_json_to_dataframe_efficiency(design)
        
        # Make predictions
        performance_score = self.performance_model.predict(performance_input)[0]
        safety_score = self.safety_model.predict(safety_input)[0]
        efficiency_score = self.efficiency_model.predict(efficiency_input)[0]

        # Create feedback
        feedback = {
            'performance_score': performance_score,
            'safety_score': safety_score,
            'efficiency_score': efficiency_score
        }
        return feedback

    # Define separate methods for transforming input for each model
    def transform_json_to_dataframe_performance(self, design):
        data = {
            'material_strength': 300,  # Placeholder value
            'load': design['performance']['load'],
            'temperature_tolerance': design['performance']['temperature_tolerance'],
            'pressure': 100,  # Placeholder value
            'vibration': design['performance']['vibration']
        }
        return pd.DataFrame([data])

    def transform_json_to_dataframe_safety(self, design):
        data = {
            'material_strength': 300,  # Placeholder value
            'safety_factor': design['safety']['safety_factor'],
            'load': design['performance']['load'],
            'temperature_tolerance': design['performance']['temperature_tolerance']
        }
        return pd.DataFrame([data])

    def transform_json_to_dataframe_efficiency(self, design):
        data = {
            'material_strength': 300,  # Placeholder value
            'load': design['performance']['load'],
            'temperature_tolerance': design['performance']['temperature_tolerance'],
            'efficiency_rating': design['efficiency']['efficiency_rating']
        }
        return pd.DataFrame([data])

