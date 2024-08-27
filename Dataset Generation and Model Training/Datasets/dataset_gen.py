import pandas as pd
import numpy as np

# Creating dummy datasets for performance, safety, and efficiency models

# Performance dataset
performance_data = pd.DataFrame({
    'material_strength': np.random.randint(100, 500, size=100),
    'load': np.random.randint(1000, 5000, size=100),
    'temperature_tolerance': np.random.randint(100, 500, size=100),
    'pressure': np.random.randint(50, 200, size=100),
    'vibration': np.random.uniform(0.1, 1.0, size=100),
    'performance_score': np.random.randint(50, 100, size=100)
})

# Safety dataset
safety_data = pd.DataFrame({
    'material_strength': np.random.randint(100, 500, size=100),
    'safety_factor': np.random.uniform(1.1, 2.0, size=100),
    'load': np.random.randint(1000, 5000, size=100),
    'temperature_tolerance': np.random.randint(100, 500, size=100),
    'safety_score': np.random.randint(50, 100, size=100)
})

# Efficiency dataset
efficiency_data = pd.DataFrame({
    'material_strength': np.random.randint(100, 500, size=100),
    'load': np.random.randint(1000, 5000, size=100),
    'temperature_tolerance': np.random.randint(100, 500, size=100),
    'efficiency_rating': np.random.uniform(0.5, 1.0, size=100),
    'efficiency_score': np.random.randint(50, 100, size=100)
})

# Define the path where you want to save the datasets
save_path = 'E:\\Aditya\\Projects\\AI_Augmented_Design_Feedback_System\\Dataset Generation and Model Training\\Datasets\\'

# Save datasets to CSV
performance_data.to_csv(save_path + 'performance_data.csv', index=False)
safety_data.to_csv(save_path + 'safety_data.csv', index=False)
efficiency_data.to_csv(save_path + 'efficiency_data.csv', index=False)

print(f"Datasets generated and saved as CSV files in {save_path}")
