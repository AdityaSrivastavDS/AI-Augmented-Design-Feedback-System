from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeClassifier
import pandas as pd
import pickle
import os

# Load datasets
performance_data = pd.read_csv('Dataset Generation and Model Training//Datasets//performance_data.csv')
safety_data = pd.read_csv('Dataset Generation and Model Training//Datasets//safety_data.csv')
efficiency_data = pd.read_csv('Dataset Generation and Model Training//Datasets//efficiency_data.csv')

# Define the directory where you want to save the models
model_dir = 'E:/Aditya/Projects/AI_Augmented_Design_Feedback_System/models/'
os.makedirs(model_dir, exist_ok=True)  # Create the directory if it doesn't exist

# Performance Model Training
X_perf = performance_data.drop('performance_score', axis=1)
y_perf = performance_data['performance_score']
model_perf = LinearRegression()
model_perf.fit(X_perf, y_perf)
with open(os.path.join(model_dir, 'performance_model.pkl'), 'wb') as f:
    pickle.dump(model_perf, f)

# Safety Model Training
# Assuming the correct column name is 'safety_metric'
X_safety = safety_data.drop('safety_metric', axis=1)
y_safety = safety_data['safety_metric']
model_safety = DecisionTreeClassifier()
model_safety.fit(X_safety, y_safety)
with open(os.path.join(model_dir, 'safety_model.pkl'), 'wb') as f:
    pickle.dump(model_safety, f)

# Efficiency Model Training
X_eff = efficiency_data.drop('efficiency_score', axis=1)
y_eff = efficiency_data['efficiency_score']
model_eff = LinearRegression()
model_eff.fit(X_eff, y_eff)
with open(os.path.join(model_dir, 'efficiency_model.pkl'), 'wb') as f:
    pickle.dump(model_eff, f)

print(f"Models trained and saved in the '{model_dir}' directory.")
