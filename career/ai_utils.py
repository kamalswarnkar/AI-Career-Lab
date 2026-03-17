import re
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

    print("AI RAW OUTPUT:", content) # debugging

    json_match = re.search(r'\{.*\}', content, re.DOTALL)
    
    if json_match:
        try:
            return json.loads(json_match.group())
        except:
            pass

    return {
        "missing_skills" : [],
        "roadmap" : [],
        "suggestions" : ["AI parsing failed"]
    }

def generate_ai_skill_analysis(user_skills, base_skills, career):
    prompt = f"""
You are an expert career advisor.

Target Career: {career}

Base Required Skills:
{base_skills}

User Skills:
{user_skills}

Tasks:
1. Improve and expand base skills (add modern tools if needed)
2. Compare with user skills
3. Return missing skills

Return ONLY JSON:

{{
  "final_skills": ["..."],
  "missing_skills": ["..."]
}}

Rules:
- No explanation
- Only JSON
"""

    response = client.chat.completions.create(
        model="openai/gpt-4o-mini",  
        messages=[
            {"role": "user",
             "content": prompt}
        ]
    )

    content = response.choices[0].message.content

    print("AI RAW OUTPUT:", content) # debugging

    json_match = re.search(r'\{.*\}', content, re.DOTALL)

    if json_match:
        try:
            return json.loads(json_match.group())
        except:
            pass

    return {
        "final_skills": [],
        "missing_skills": []
    }