from django.db import models

class Student(models.Model):
    name=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    age=models.IntegerField()
    email=models.EmailField(max_length=50)
    image=models.FileField(upload_to="mymedia")

