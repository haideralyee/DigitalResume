from django.db import models

class Introduction(models.Model):
    name = models.CharField(max_length=100)
    about = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    linkedin_url = models.URLField(blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)
    

    def __str__(self):
        return self.name

class Education(models.Model):
    institution = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    field_of_study = models.CharField(max_length=100)

    def __str__(self):
        return self.degree

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    github_link = models.URLField()

    def __str__(self):
        return self.title

class Skill(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
