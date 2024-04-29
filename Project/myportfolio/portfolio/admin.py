# portfolio/admin.py
from django.contrib import admin
from .models import Project, Skill, Education, Introduction

admin.site.register(Project)
admin.site.register(Skill)
admin.site.register(Education)
admin.site.register(Introduction)

