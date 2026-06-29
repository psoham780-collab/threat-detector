import pickle
import os


BASE_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../..")
)


with open(os.path.join(BASE_DIR, "url_model.pkl"), "rb") as f:
    model = pickle.load(f)


with open(os.path.join(BASE_DIR, "vectorizer.pkl"), "rb") as f:
    vectorizer = pickle.load(f)



def predict_url(url):

    data = vectorizer.transform([url])

    prediction = model.predict(data)[0]

    probability = model.predict_proba(data)[0]


    if prediction == 1:
        return {
            "risk": "Malicious",
            "score": int(probability[1] * 100),
            "message": "AI detected suspicious URL"
        }


    else:
        return {
            "risk": "Safe",
            "score": int(probability[0] * 100),
            "message": "URL looks safe"
        }