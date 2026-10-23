from django.db import models


class student(models.Model):
    sid = models.CharField(max_length=50)
    sname = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)

    def __str__(self):
        return self.sname