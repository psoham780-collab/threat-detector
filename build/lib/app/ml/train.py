import pandas as pd
import pickle
import os

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer


# Project root se dataset ka path
BASE_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../..")
)

DATASET_PATH = os.path.join(
    BASE_DIR,
    "dataset",
    "urls.csv"
)


# Load dataset
data = pd.read_csv(DATASET_PATH)


# Input & output
X = data["url"]
y = data["label"]


# Convert URL text into numbers
vectorizer = TfidfVectorizer(
    analyzer="char",
    ngram_range=(2,5),
    max_features=5000
)

X = vectorizer.fit_transform(X)


# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# AI Model
model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)


# Train
model.fit(
    X_train,
    y_train
)


# Accuracy
accuracy = model.score(
    X_test,
    y_test
)

print("Model Accuracy:", accuracy)


# Save location
MODEL_PATH = os.path.join(
    BASE_DIR,
    "url_model.pkl"
)

VECTORIZER_PATH = os.path.join(
    BASE_DIR,
    "vectorizer.pkl"
)


# Save model
with open(MODEL_PATH, "wb") as f:
    pickle.dump(model, f)


# Save vectorizer
with open(VECTORIZER_PATH, "wb") as f:
    pickle.dump(vectorizer, f)


print("AI Model Saved Successfully 🚀")
print("Files created:")
print("url_model.pkl")
print("vectorizer.pkl")