from django.db import models

# Create your models here.

class StudentModel(models.Model):
    stu_name=models.CharField(max_length=30)
    stu_city=models.CharField(max_length=30)
#student=models.Manager()

def __str__(self):
    return self.stu_name