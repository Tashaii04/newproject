from django.db import models

class Student(models.Model):
    name=models.CharField(max_length=40)
    age=models.IntegerField()
    email=models.EmailField(max_length=50)
