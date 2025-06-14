import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
import json
import joblib

# Step 1: Load & prepare data
data = []
with open("ml_logs.jsonl", "r") as f:
    for line in f:
        data.append(json.loads(line))

df = pd.DataFrame(data)

# Step 2: Use event_type + description as features
df["features"] = df["event_type"] + " " + df["description"]

# Step 3: Vectorize text features
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df["features"])

y = df["label"]

# Step 4: Train ML model
clf = RandomForestClassifier(n_estimators=100)
clf.fit(X, y)

# Step 5: Save model and vectorizer
joblib.dump(clf, "threat_model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print("✅ ML model and vectorizer saved")
