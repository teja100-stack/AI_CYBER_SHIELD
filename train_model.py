import pandas as pd
from sklearn.ensemble import IsolationForest

data = pd.DataFrame({
    "failed_logins": [0, 1, 2, 1, 3, 2, 0, 1, 2, 50],
    "data_transferred": [50, 80, 100, 60, 120, 90, 70, 100, 80, 1000],
    "unknown_device": [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
})

model = IsolationForest(contamination=0.1, random_state=42)

model.fit(data)

import joblib
joblib.dump(model, "cyber_threat_model.pkl")

print("AI model trained successfully!")