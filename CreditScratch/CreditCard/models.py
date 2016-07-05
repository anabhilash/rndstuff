from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class CardDetails(models.Model):
    nickName = models.CharField(max_length=20)
    nameOnCard = models.CharField(max_length=10)
    expireDate = models.DateField()
    type = models.CharField(max_length=10)
    cardNumber = models.CharField(max_length=16,blank=False)
    user=models.ForeignKey(User)