from django import forms

class CareerForm(forms.Form):
    skills = forms.CharField(
        label="Skills",
        widget=forms.TextInput(attrs={'placeholder': 'e.g. python, statistics'})
    )

    interests = forms.CharField(
        label="Interest",
        widget=forms.TextInput(attrs={'placeholder': 'e.g. AI, Research'})
    )

    subjects = forms.CharField(
        label="Favorite subjects",
        widget=forms.TextInput(attrs={'placeholder': 'e.g. math'})
    )

    work_style = forms.CharField(
        label="Preferred Work Style",
        widget=forms.TextInput(attrs={'placeholder': 'e.g. analytical'})
    )