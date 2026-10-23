from django.db import models

# Create your models here.
class client(models.Model):
    cid=models.IntegerField()
    cname=models.CharField()
    ccompany=models.CharField()

    def __str__(self):
        return self.cname
    
    
class customer(models.Model):
    names=models.CharField()
    mail=models.CharField()
    contact=models.IntegerField()

    def __str__(self):
         return self.names



class order (models.Model):
          oid=models.IntegerField()
          prize=models.FloatField()
    



