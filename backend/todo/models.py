from django.db.models.signals import post_save
from django.db import models
from django.utils import timezone
from django.contrib import auth
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
def one_week_hence():
    return timezone.now() + timezone.timedelta(days=7)


# class User(models.Model):
#     user = models.OneToManyField(User, on_delete=models.CASCADE, primary_key=True,)

class UserProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    # def __str__(self):
    #     # return self.user.username
    #      return self.user.sername.get() 


class Todo(models.Model):
    #user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True,)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, default="")
    title = models.CharField(max_length=100)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now)
    #created_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(default=one_week_hence,  blank=True, null=True)

    def _str_(self):
        return self.title
    
    def __str__(self):
        return self.user.username
    




