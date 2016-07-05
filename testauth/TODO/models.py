from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class TodoList(models.Model):
    name = models.CharField(max_length=50)
    created = models.DateField(default=timezone.now())
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.name


class TodoItem(models.Model):
    description = models.CharField(max_length=700)
    created = models.DateField(default=timezone.now())
    duedate = models.DateField(default=timezone.now())
    completed = models.BooleanField(default=False)
    li = models.ForeignKey(TodoList)

    def __unicode__(self):
        return self.description
