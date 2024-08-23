import json
from .simulation import simulate_design
from .predictive_modeling import evaluate_performance, evaluate_safety, evaluate_efficiency

class DesignFeedbackSystem:
    def __init__(self):
        pass

    def analyze_design(self, design_path):
        with open(design_path, 'r') as f:
            design = json.load(f)

        simulation_results = simulate_design(design)
        performance_score = evaluate_performance(design)
        safety_score = evaluate_safety(design)
        efficiency_score = evaluate_efficiency(design)

        feedback = {
            "performance": performance_score,
            "safety": safety_score,
            "efficiency": efficiency_score,
            "simulation_results": simulation_results
        }

        return feedback
