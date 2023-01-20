from django.db import models

# Create your models here.
class Std(models.Model):
    std=models.CharField(max_length=100,primary_key=True)

class Details(models.Model):
    std=models.ForeignKey(Std,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    url=models.URLField()

class Records(models.Model):
    name=models.ForeignKey(Details,on_delete=models.CASCADE)
    date=models.DateField()
