from __future__ import unicode_literals

from django.db import models
from ..login.models import User

class CourseManage(models.Manager):
        pass

class Course(models.Model):
    name= models.CharField(max_length=80)
    description = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ManyToManyField(User)
