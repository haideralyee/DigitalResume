
from django.shortcuts import render
from .models import Introduction, Project, Skill, Education

def home(request):
    introduction=Introduction.objects.first()
    projects = Project.objects.all()
    skills = Skill.objects.all()
    education = Education.objects.all()
    return render(request, 'portfolio/home.html', {'introduction':introduction,'projects': projects, 'skills': skills, 'education': education})
