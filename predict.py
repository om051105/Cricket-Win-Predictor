import sys
import pickle
import pandas as pd

# Load Model
with open("cricket_model.pkl", "rb") as f:
    model = pickle.load(f)

# Get Teams from PHP
team1 = sys.argv[1]
team2 = sys.argv[2]

#
