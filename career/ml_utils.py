import joblib
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODEL_PATH = os.path.join(BASE_DIR, "ml_models", "career_model.pkl")
VECTORIZER_PATH = os.path.join(BASE_DIR, "ml_models", "vectorizer.pkl")

def load_model():
    if not os.path.exists(MODEL_PATH):
            print("Model file not found:", MODEL_PATH)
            return None, None

    if not os.path.exists(VECTORIZER_PATH):
        print("Vectorizer file not found:", VECTORIZER_PATH)
        return None, None

    model = joblib.load(MODEL_PATH)
    vectorizer = joblib.load(VECTORIZER_PATH)

    return model, vectorizer

def predict_career(user_text):
    model, vectorizer = load_model()

    if model is None or vectorizer is None:
         raise Exception("Model or Vectorizer not loaded properly")

    text_vector = vectorizer.transform([user_text])

    probs = model.predict_proba(text_vector)[0]
    classes = model.classes_

    results = sorted(zip(classes, probs), key=lambda x : x[1], reverse=True)

    return results