from django.shortcuts import render
from .forms import CareerForm
from .ml_utils import predict_career

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

            """user_data = {
                'skills' : skills,
                'interests' : interests,
                'subjects' : subjects,
                'work_style' : work_style,
            }"""

            return render(request, 'career/result.html', {
                'predictions' : predictions[:3],
                'data' : {
                    'skills' : skills,
                    'interests' : interests,
                    'subjects' : subjects,
                    'work_style' : work_style,
                }
            })
        
    return render(request, 'career/analyze.html', {'form' : form})