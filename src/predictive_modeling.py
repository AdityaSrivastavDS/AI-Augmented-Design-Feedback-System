import pickle
import numpy as np


def load_model(model_path):
    with open(model_path, 'rb') as f:
        return pickle.load(f)

def flatten_design_parameters_performance(design):
    return [
        design['parameters']['material'].get('density', 0),  # material_strength
        design['performance'].get('load', 0),
        design['performance'].get('temperature_tolerance', 0),
        design['performance'].get('vibration', 0)
    ]

def flatten_design_parameters_safety(design):
    return [
        design['parameters']['material'].get('density', 0),  # material_strength
        design['safety'].get('safety_factor', 0),
        design['performance'].get('load', 0),
        design['performance'].get('temperature_tolerance', 0)
    ]

def flatten_design_parameters_efficiency(design):
    return [
        design['parameters']['material'].get('density', 0),  # material_strength
        design['performance'].get('load', 0),
        design['performance'].get('temperature_tolerance', 0),
        design['efficiency'].get('efficiency_rating', 0)
    ]




def evaluate_performance(design):
    model = load_model('models/performance_model.pkl')
    flat_params = np.array(flatten_design_parameters_performance(design)).reshape(1, -1)
    return model.predict(flat_params)[0]

def evaluate_safety(design):
    model = load_model('models/safety_model.pkl')
    flat_params = np.array(flatten_design_parameters_safety(design)).reshape(1, -1)
    return model.predict(flat_params)[0]

def evaluate_efficiency(design):
    model = load_model('models/efficiency_model.pkl')
    flat_params = np.array(flatten_design_parameters_efficiency(design)).reshape(1, -1)
    return model.predict(flat_params)[0]
