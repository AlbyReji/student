from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.


# class Studentdb(models.Model):

#     ADMISSION_CHOICES = [
#         ('1st', '1st'),
#         ('2nd', '2nd'),
#         ('3rd', '3rd'),
#         ('4th', '4th'),
#         ('5th', '5th'),
#         ('6th', '6th'),
#         ('7th', '7th'),
#         ('8th', '8th'),
#         ('9th', '9th'),
#         ('10th', '10th'),

    
#     ]
    
#     admission_number = models.CharField(max_length=20, unique=True)
#     name = models.CharField(max_length=50)
#     email = models.EmailField(max_length=100)
#     age = models.IntegerField(validators=[MaxValueValidator(17)])
#     class_level = models.CharField(max_length=3, choices=ADMISSION_CHOICES)
#     description = models.TextField()
#     image = models.ImageField(upload_to='image/',null = True ,blank = True)
#     marklist = models.FileField(upload_to='marklist/',null = True ,blank = True)

#     def __str__(self):
#         return self.name
class Student(models.Model):

    ADMISSION_CHOICES = [
        ('1st', '1st'),
        ('2nd', '2nd'),
        ('3rd', '3rd'),
        ('4th', '4th'),
        ('5th', '5th'),
        ('6th', '6th'),
        ('7th', '7th'),
        ('8th', '8th'),
        ('9th', '9th'),
        ('10th', '10th'),

    
    ]
    
    admission_number = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    age = models.IntegerField(validators=[MaxValueValidator(17)])
    class_level = models.CharField(max_length=10, choices=ADMISSION_CHOICES)
    description = models.TextField()
    image = models.ImageField(upload_to='image/')
    marklist = models.FileField(upload_to='marklist/')

    def __str__(self):
        return self.name


