import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
import joblib

# Load and prepare data
df = pd.read_csv("data/data.csv").drop(columns=["id", "Unnamed: 32"])
df['diagnosis'] = df['diagnosis'].map({'M': 1, 'B': 0})
X = df.drop(columns='diagnosis')
y = df['diagnosis']

# Scale features and train model
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

model = LogisticRegression(max_iter=1000)
model.fit(X_scaled, y)

# Save model and scaler
joblib.dump(model, "model/logistic_model.pkl")
joblib.dump(scaler, "model/scaler.pkl")

print("✅ Model and scaler saved!")