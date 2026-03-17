import joblib
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODEL_PATH = os.path.join(BASE_DIR, "ml_models", "career_model.pkl")
VECTORIZER_PATH = os.path.join(BASE_DIR, "ml_models", "vectorizer.pkl")

def load_model():
    model = joblib.load(MODEL_PATH)
    vectorizer = joblib.load(VECTORIZER_PATH)

    return model, vectorizer

def predict_career(user_text):
    model, vectorizer = load_model()

    text_vector = vectorizer.transform([user_text])

    probs = model.predict_proba(text_vector)[0]
    classes = model.classes_

    results = sorted(zip(classes, probs), key=lambda x : x[1], reverse=True)

    return results