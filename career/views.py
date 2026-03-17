from django.shortcuts import render
from .forms import CareerForm
from .ml_utils import predict_career
from .skill_analyzer import get_required_skills, compare_skills, generate_roadmap
from .ai_utils import generate_ai_analysis, generate_ai_skill_analysis
from .data_utils import load_career_skills

# Create your views here.
def home(request):
    return render(request, 'career/home.html')

def analyze(request):
    form = CareerForm()

    if request.method == "POST":
        form = CareerForm(request.POST)
        
        if form.is_valid():
            skills = form.cleaned_data['skills']
            interests = form.cleaned_data['interests']
            subjects = form.cleaned_data['subjects']
            work_style = form.cleaned_data['work_style']

            combined_text = f"{skills} {interests} {subjects} {work_style}"

            predictions = predict_career(combined_text)

            skills_data = load_career_skills()

            top_career = predictions[0][0]

            base_skills = skills_data.get(top_career, [])

            ai_data = generate_ai_analysis(skills, interests, top_career)
            ai_skill_data = generate_ai_skill_analysis(skills, base_skills, top_career)
            
            final_skills = ai_skill_data.get("final_skills", [])
            ai_missing = ai_skill_data.get("missing_skills", [])
            ai_roadmap = ai_data.get("roadmap", [])
            ai_suggestions = ai_data.get("suggestions", [])

            required_skills = get_required_skills(top_career)
            missing_skill = compare_skills(skills, required_skills)

            roadmap = generate_roadmap(top_career)

            user_skill_list = [s.strip().lower() for s in skills.split(",")]
            required_skill_list = [s.lower() for s in final_skills]
            matched = [s for s in required_skill_list if s in user_skill_list]

            if len(required_skill_list) > 0:
                match_score = int((len(matched) / len(required_skill_list)) * 100)
            else:
                match_score = 0

            """user_data = {
                'skills' : skills,
                'interests' : interests,
                'subjects' : subjects,
                'work_style' : work_style,
            }"""

            return render(request, 'career/result.html', {
                'predictions' : predictions[:3],
                'missing_skills' : missing_skill,
                'roadmap' : roadmap,

                'final_skills' : final_skills,
                'ai_missing' : ai_missing,
                'ai_roadmap' : ai_roadmap,
                'ai_suggestions' : ai_suggestions,

                'match_score' : match_score,

                'top_career' : top_career,
                'data' : {
                    'skills' : skills,
                    'interests' : interests,
                    'subjects' : subjects,
                    'work_style' : work_style,
                }
            })
        
    return render(request, 'career/analyze.html', {'form' : form})
