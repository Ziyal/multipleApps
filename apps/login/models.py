from __future__ import unicode_literals
from django.db import models
import re
import bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):

    def regVal(self, postData):
        errors = []
        #checks for length in forms
        if len(postData['first_name']) < 2:
            errors.append("First name must be at least 2 characters long")
        if len(postData['last_name']) < 2:
            errors.append("Last name must be at least 2 characters long")
        if not len(postData['email']):
            errors.append("Email must not be blank")
        if len(postData['password']) < 8:
            errors.append("Password must be at least characters 8 long")
        if len(postData['password_cf']) < 8:
            errors.append("Password Confirmation must be at least 8 characters long")
        #checks that passwords match
        if not postData['password'] == postData['password_cf']:
            errors.append("Passwords must match")
        #checks for valid email
        if not EMAIL_REGEX.match(postData['email']):
            errors.append("Email is not valid")
        user = User.objects.filter(email=postData['email'])
        if user:
            errors.append("Email has already been used")

        if len(errors) > 0:
            print "You have errors. Boo!"
            return (False, errors)
        else:
            print "You have 0 errors. Hooray!"
            pw_hash = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
            user = User.objects.create(first_name=postData['first_name'], last_name=postData['last_name'], email=postData['email'], password=pw_hash)
            return (True, user)

    def logVal(self, postData):
        errors2 = []

        if not len(postData['email']):
            errors2.append("Email must not be blank")
        user = User.objects.get(email = postData['email'])
        if not user:
            errors2.append("Invalid email")
        if bcrypt.hashpw(postData['password'].encode(), user.password.encode()) != user.password or len(postData['password']) < 8:
            errors2.append("Incorrect password")

        if len(errors2) > 0:
            return (False, errors2)
        else:
            return (True, user)

# **********************************************
class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = UserManager()
