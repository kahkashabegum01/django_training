from django.db import models


# Create your models here.
class user(models.Model):
    username = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.username


