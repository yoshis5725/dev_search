import uuid
from django.db import models


class Profile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, null=True, blank=True)
    username = models.CharField(max_length=150, null=True, blank=True)
    location = models.CharField(max_length=150, null=True, blank=True)
    first_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    short_intro = models.CharField(max_length=600, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics/', null=True, blank=True, default='user-default.png')
    social_github = models.CharField(max_length=255, null=True, blank=True)
    social_linkedin = models.CharField(max_length=255, null=True, blank=True)
    social_website = models.CharField(max_length=255, null=True, blank=True)
    social_twitter = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} Profile' if self.user else 'Profile without user'


class Skill(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
