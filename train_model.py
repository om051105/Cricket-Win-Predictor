import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import pickle

# Load Dataset
data = pd.read_csv("cricket_data.csv")

# Encode Categorical Variables
encoder = LabelEncoder()
data["team1"] = encoder.fit_transform(data["team1"])
data["team2"] = encoder.fit_transform(data["team2"])
data["venue"] = encoder.fit_transform(data["venue"])
data["toss_winner"] = encoder.fit_transform(data["toss_winner"])
data["weather"] = encoder.fit_transform(data["weather"])
data["winner"] = encoder.fit_transform(data["winner"])

# Select Features and Target
X = data[["team1", "team2", "team1_score", "team2_score", "venue", "toss_winner", "weather"]]
y = data["winner"]

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save Model and Encoder
with open("cricket_model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("label_encoder.pkl", "wb") as f:
    pickle.dump(encoder, f)

print("Model trained and saved successfully!")
