def get_required_skills(career):
    career_skills = {
        "Data Scientist": ["python", "statistics", "machine learning", "data analysis"],
        "ML Engineer": ["python", "machine learning", "deep learning", "pytorch"],
        "Backend Developer": ["java", "api", "databases", "system design"],
        "UI Designer": ["ui", "ux", "figma", "creativity"],
        "Cybersecurity Analyst": ["networking", "security", "ethical hacking"],
        "Software Engineer": ["c++", "dsa", "problem solving"],
        "Data Analyst": ["python", "excel", "data visualization"],
        "DevOps Engineer": ["aws", "docker", "ci cd"]
    }

    return career_skills.get(career, [])

def compare_skills(user_skills, required_skills):
    user_skills = [skill.strip().lower() for skill in user_skills.split(",")]
    missing = [skill for skill in required_skills if skill not in user_skills]

    return missing
