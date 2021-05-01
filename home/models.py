from django.db import models
from django.contrib.auth.models import User


class UserProfileInfo(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE)


    profile_portfolio = models.URLField(blank=True)


    profile_pic = models.ImageField(upload_to = 'profile_pic', blank=True)

    def __str__(self):
        return self.user.username
        