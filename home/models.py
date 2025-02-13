# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Account(models.Model):

    #__Account_FIELDS__
    account_id = models.IntegerField(null=True, blank=True)
    account_name = models.CharField(max_length=255, null=True, blank=True)
    enable = models.BooleanField()

    #__Account_FIELDS__END

    class Meta:
        verbose_name        = _("Account")
        verbose_name_plural = _("Account")


class Influencer(models.Model):

    #__Influencer_FIELDS__
    influencer_id = models.IntegerField(null=True, blank=True)
    influncer_id = models.TextField(max_length=255, null=True, blank=True)

    #__Influencer_FIELDS__END

    class Meta:
        verbose_name        = _("Influencer")
        verbose_name_plural = _("Influencer")



#__MODELS__END
