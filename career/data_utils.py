import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def load_career_skills():
    path = os.path.join(BASE_DIR, "ml_models", "career_skills.json")

    with open(path, "r") as f:
        return json.load(f)