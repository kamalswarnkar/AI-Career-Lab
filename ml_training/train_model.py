import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

df = pd.read_csv("dataset.csv") # data set loaded

df['text'] = df['skills'] + " " + df['interests'] + " " + df['personality'] # features are combined

X = df['text'] # feature
y = df['career'] # label

vectorizer = TfidfVectorizer() 
X_vec = vectorizer.fit_transform(X) # vectorization

X_train, X_test, y_train, y_test = train_test_split(X_vec, y, test_size=0.2, random_state=42) # spliting done

model = RandomForestClassifier() # model = Random Forest
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred)) # Evaluation

joblib.dump(model, "../ml_models/career_model.pkl")
joblib.dump(vectorizer, "../ml_models/vectorizer.pkl")

print("Model and Vectorizer saved successfully")