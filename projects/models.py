import uuid

from django.contrib.auth.models import User
from django.db import models
from users.models import Profile


class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    featured_image = models.ImageField(upload_to='projects/images/', default='default.jpg', null=True, blank=True)
    tags = models.ManyToManyField('Tag', related_name='projects', blank=True)
    demo_url = models.CharField(null=True, blank=True)
    source_code_url = models.CharField(null=True, blank=True)
    vote_total = models.IntegerField(default=0, null=True, blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Projects"
        ordering = ['-title']

    def __str__(self):
        return self.title


class Review(models.Model):
    VOTE_CHOICES = (
        ('up', 'Upvote'),
        ('down', 'Downvote'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='reviews')
    # author
    review = models.TextField()
    value = models.CharField(max_length=255, choices=VOTE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "Reviews"

    def __str__(self):
        return f'Review on {self.project.title}'


class Tag(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Tags"

    def __str__(self):
        return self.name
