import pickle
import numpy as np

def load_model(model_path):
    with open(model_path, 'rb') as f:
        return pickle.load(f)

def flatten_design_parameters(design):
    """Flattens the design parameters into a list with the correct number of features."""
    flat_params = [
        design['parameters']['dimensions']['length'],
        design['parameters']['dimensions']['width'],
        design['parameters']['dimensions']['height'],
        design['parameters']['load'],
        design['parameters']['safety_factor']  # Ensure this matches the training data
    ]
    return flat_params


def evaluate_performance(design):
    model = load_model('models/performance_model.pkl')
    flat_params = np.array(flatten_design_parameters(design)).reshape(1, -1)
    return model.predict(flat_params)[0]

def evaluate_safety(design):
    model = load_model('models/safety_model.pkl')
    flat_params = np.array(flatten_design_parameters(design)).reshape(1, -1)
    return model.predict(flat_params)[0]

def evaluate_efficiency(design):
    model = load_model('models/efficiency_model.pkl')
    flat_params = np.array(flatten_design_parameters(design)).reshape(1, -1)
    return model.predict(flat_params)[0]
