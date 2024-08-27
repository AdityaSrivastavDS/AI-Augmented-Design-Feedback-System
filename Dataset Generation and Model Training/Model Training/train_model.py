import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestRegressor
import pickle

# Load datasets
performance_data = pd.read_csv('E:\\Aditya\Projects\\AI_Augmented_Design_Feedback_System\\Dataset Generation and Model Training\\Datasets\\performance_data.csv')
safety_data = pd.read_csv('E:\\Aditya\Projects\\AI_Augmented_Design_Feedback_System\\Dataset Generation and Model Training\\Datasets\\safety_data.csv')
efficiency_data = pd.read_csv('E:\\Aditya\Projects\\AI_Augmented_Design_Feedback_System\\Dataset Generation and Model Training\\Datasets\\efficiency_data.csv')

# Performance model
X_performance = performance_data.drop('performance_score', axis=1)
y_performance = performance_data['performance_score']
performance_model = LinearRegression()
performance_model.fit(X_performance, y_performance)

# Safety model
X_safety = safety_data.drop('safety_score', axis=1)
y_safety = safety_data['safety_score']
safety_model = DecisionTreeClassifier()
safety_model.fit(X_safety, y_safety)

# Efficiency model
X_efficiency = efficiency_data.drop('efficiency_score', axis=1)
y_efficiency = efficiency_data['efficiency_score']
efficiency_model = RandomForestRegressor()
efficiency_model.fit(X_efficiency, y_efficiency)

# Define the path where you want to save the models
model_save_path = 'E:\\Aditya\\Projects\\AI_Augmented_Design_Feedback_System\\models\\'

# Save models to disk
with open(model_save_path + 'performance_model.pkl', 'wb') as f:
    pickle.dump(performance_model, f)
with open(model_save_path + 'safety_model.pkl', 'wb') as f:
    pickle.dump(safety_model, f)
with open(model_save_path + 'efficiency_model.pkl', 'wb') as f:
    pickle.dump(efficiency_model, f)

print(f"Models trained and saved to {model_save_path}")

