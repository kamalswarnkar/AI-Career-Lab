import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import joblib

df = pd.read_csv("dataset.csv") # data set loaded

df['text'] = df['skills'] + " " + df['interests'] + " " + df['personality'] # features are combined

X = df['text'] # feature
y = df['career'] # label

vectorizer = TfidfVectorizer() 
X_vec = vectorizer.fit_transform(X) # vectorization

X_train, X_test, y_train, y_test = train_test_split(X_vec, y, test_size=0.2, random_state=42) # spliting done

models = {
    "RandomForest" : RandomForestClassifier(),
    "LogisticRegression" : LogisticRegression(max_iter=200),
    "SVM" : SVC(probability=True)
}

results = []

best_model = None
best_score = 0

for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    acc = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, average="weighted", zero_division=0)
    recall = recall_score(y_test, y_pred, average="weighted", zero_division=0)
    f1 = f1_score(y_test, y_pred, average="weighted", zero_division=0)

    results.append({
        "Model" : name,
        "Accuracy" : acc,
        "Precision" : precision,
        "Recall" : recall,
        "F1 Score" : f1
    })

    if acc > best_score:
        best_score = acc
        best_model = model


joblib.dump(best_model, "../ml_models/career_model.pkl")
joblib.dump(vectorizer, "../ml_models/vectorizer.pkl")

df_results = pd.DataFrame(results)
df_results.to_csv("../ml_models/model_comparison.csv", index=False)

print("Model Comparison saved successfully")
print(df_results)