import pandas as pd
import re
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import joblib
import os

df = pd.read_csv("dataset.csv")

df = df.fillna("")

df = df[(df['skills'] != "") | (df['interests'] != "") | (df['personality'] != "")]

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'\d+', '', text)  
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = re.sub(r'\s+', ' ', text).strip() 
    return text

df['skills'] = df['skills'].apply(clean_text)
df['interests'] = df['interests'].apply(clean_text)
df['personality'] = df['personality'].apply(clean_text)

df['text'] = df['skills'] + " " + df['interests'] + " " + df['personality']

X = df['text']
y = df['career']

vectorizer = TfidfVectorizer(
    max_features=5000,
    ngram_range=(1,2),  
    stop_words='english'
)

X_vec = vectorizer.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X_vec, y, test_size=0.2, random_state=42
)

models = {
    "RandomForest": RandomForestClassifier(n_estimators=100),
    "LogisticRegression": LogisticRegression(max_iter=300),
    "SVM": SVC(probability=True)
}

results = []
best_model = None
best_score = 0

for name, model in models.items():
    model.fit(X_train, y_train)

    y_train_pred = model.predict(X_train)
    y_test_pred = model.predict(X_test)

    test_acc = accuracy_score(y_test, y_test_pred)
    train_acc = accuracy_score(y_train, y_train_pred)
    precision = precision_score(y_test, y_test_pred, average="weighted", zero_division=0)
    recall = recall_score(y_test, y_test_pred, average="weighted", zero_division=0)
    f1 = f1_score(y_test, y_test_pred, average="weighted", zero_division=0)

    gap = abs(train_acc - test_acc)

    results.append({
        "Model": name,
        "Training Accuracy": train_acc,
        "Testin Accuracy": test_acc,
        "Gap": gap,
        "Precision": precision,
        "Recall": recall,
        "F1 Score": f1
    })

    score = test_acc - gap 

    if score > best_score:
        best_score = score
        best_model = model

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

model_path = os.path.join(BASE_DIR, "ml_models", "career_model.pkl")
vectorizer_path = os.path.join(BASE_DIR, "ml_models", "vectorizer.pkl")

joblib.dump(best_model, model_path)
joblib.dump(vectorizer, vectorizer_path)

df_results = pd.DataFrame(results)
df_results.to_csv("../ml_models/model_comparison.csv", index=False)

print("\n Model Comparison:")
print(df_results)