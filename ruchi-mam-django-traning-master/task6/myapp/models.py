from django.db import models


# Create your models here.
class product(models.Model):
    pid=models.IntegerField()
    pname=models.CharField()
    prize=models.FloatField()
    offer=models.FloatField()

    def __str__(self):
        return self.pname
