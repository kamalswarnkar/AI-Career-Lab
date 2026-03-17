import os
import json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key = os.getenv("OPENROUTER_API_KEY"),
    base_url = "https://openrouter.ai/api/v1"
)

def generate_ai_analysis(skills, interests, career):
    prompt = f"""
You are an expert career advisor.

User Profile:
Skills: {skills}
Interests: {interests}
Target Career: {career}

Return ONLY valid JSON in this exact format:

{{
  "missing_skills": ["..."],
  "roadmap": ["..."],
  "suggestions": ["..."]
}}

Rules:
- No explanation
- No extra text
- Only JSON
"""
    
    response = client.chat.completions.create(
        model="openai/gpt-4o-mini",
        messages=[
            {"role" : "user",
             "content" : prompt}
        ]
    )

    content =  response.choices[0].message.content

    try:
        return json.loads(content)
    except:
        return {
            "missing_skills" : [],
            "roadmap" : [],
            "suggestions" : ["AI parsing failed"]
        }