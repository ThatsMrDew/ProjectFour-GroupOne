import sqlite3
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score


# Connect to SQLite database
conn = sqlite3.connect("../heart.db")
query = "SELECT * FROM heart_attack_risk"

# Load the query result into a DataFrame
df = pd.read_sql_query(query, conn)
conn.close()

# Define features and target variable
X = df.drop(columns=["Heart Attack Risk"])
y = df["Heart Attack Risk"]

# Split data into training (80%) and testing (20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale numerical features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Train XGBoost model
model = XGBClassifier(n_estimators=300, max_depth=6, learning_rate=0.05, random_state=42)
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluate model
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.2%}")

# Hyperparameter tuning using Grid Search
from sklearn.model_selection import GridSearchCV

param_grid = {
    'n_estimators': [50, 100, 150, 200, 300, 400, 500, 1000],
    'learning_rate': [0.05, 0.1, .2],
    'max_depth': [1, 2, 4, 5, 6],
    'subsample': [.2, .5, 0.8, 1.0],
    'colsample_bytree': [.3, .6, 0.8, 1.0]
}

grid_search = GridSearchCV(XGBClassifier(random_state=42), param_grid, cv=5, scoring="accuracy", n_jobs=-1)
grid_search.fit(X_train, y_train)

# Best model
best_model = grid_search.best_estimator_
y_pred_best = best_model.predict(X_test)

# Evaluate optimized model
accuracy_best = accuracy_score(y_test, y_pred_best)
print(f"Optimized Model Accuracy: {accuracy_best:.2%}")

print("Best Parameters:", grid_search.best_params_)