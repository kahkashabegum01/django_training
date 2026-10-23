from django.db import models
# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.username

class Test(models.Model):
    subject = models.CharField(max_length=100)
    total_questions = models.IntegerField()

class Question(models.Model):
    subject = models.CharField(max_length=100)
    question = models.CharField(max_length=500)
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)

    def __str__(self):
        return self.subject