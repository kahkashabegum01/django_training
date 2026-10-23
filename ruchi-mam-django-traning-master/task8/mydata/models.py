from django.db import models

# Create your models here.


# Create your models here.
class user(models.Model):
    username = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.username


class student(models.Model):
    s_id=models.IntegerField()
    sname=models.CharField()
    sbranch=models.CharField()

    def __str__(self):
            return self.sbranch




