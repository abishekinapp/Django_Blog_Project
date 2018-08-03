# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User


from django.db import models
from django.db.models.signals import post_save


#from django.utils import timezone

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    description = models.TextField(max_length=100)
    city = models.TextField(max_length=100)
    website = models.URLField()
    #phone = models.IntegerField()

def create_profile(sender,**arg):
    if arg['created']:
        user_profile = UserProfile.objects.create(user=arg['instance'])
post_save.connect (create_profile, sender=User)
