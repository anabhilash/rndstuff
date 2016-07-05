from __future__ import unicode_literals

from django.db import models

# Create your models here.

class College(models.Model):
    name=models.CharField(max_length=60)
    acronym=models.CharField(max_length=20)
    location=models.CharField(max_length=30)
    contact=models.EmailField(max_length=29)

    def __str__(self):  # __unicode__ on Python 2
        return self.name

class Student(models.Model):
    name=models.CharField(max_length=60)
    email=models.EmailField(max_length=40)
    dbfolder=models.CharField(max_length=40)
    dropped=models.BooleanField()
    college=models.ForeignKey(College)

    def __str__(self):  # __unicode__ on Python 2
        return self.name

class Marks(models.Model):
    student=models.OneToOneField(Student)
    transform=models.IntegerField()
    from_custom_base26=models.IntegerField()
    get_pig_latin=models.IntegerField()
    top_chars=models.IntegerField()
    total=models.IntegerField()


class Teacher(models.Model):
    name=models.CharField(max_length=35)
    age=models.IntegerField()
    college=models.ForeignKey(College)