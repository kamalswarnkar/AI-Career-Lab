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

def generate_roadmap(career):
    roadmaps = {
        "Data Scientist": [
            "Learn Python and Statistics",
            "Study Data Analysis and Visualization",
            "Learn Machine Learning",
            "Build Projects and Work on Real Data"
        ],
        "ML Engineer": [
            "Master Python and Data Structures",
            "Learn Machine Learning Algorithms",
            "Study Deep Learning and Frameworks (TensorFlow/PyTorch)",
            "Deploy ML Models and Build Projects"
        ],
        "Backend Developer": [
            "Learn Programming (Java/Python)",
            "Understand APIs and Databases",
            "Learn Frameworks (Django/Spring)",
            "Build Scalable Backend Systems"
        ],
        "UI Designer": [
            "Learn Design Principles",
            "Master UI/UX Tools (Figma)",
            "Work on Design Projects",
            "Build Portfolio"
        ],
        "Cybersecurity Analyst": [
            "Learn Networking Basics",
            "Study Security Concepts",
            "Practice Ethical Hacking",
            "Get Certifications (CEH, Security+)"
        ],
        "Software Engineer": [
            "Learn Programming (C++/Python)",
            "Master Data Structures & Algorithms",
            "Build Projects",
            "Prepare for Interviews"
        ],
        "Data Analyst": [
            "Learn Python or Excel",
            "Study Data Visualization",
            "Work on Real Datasets",
            "Build Dashboard Projects"
        ],
        "DevOps Engineer": [
            "Learn Linux and Networking",
            "Understand CI/CD",
            "Learn Docker and Kubernetes",
            "Work on Cloud (AWS/GCP)"
        ]
    }

    return roadmaps.get(career, [])