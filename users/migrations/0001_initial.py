# Generated by Django 5.2.1 on 2025-05-11 12:30

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Profile",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("first_name", models.CharField(blank=True, max_length=30, null=True)),
                ("last_name", models.CharField(blank=True, max_length=30, null=True)),
                ("email", models.EmailField(blank=True, max_length=255, null=True)),
                (
                    "short_intro",
                    models.CharField(blank=True, max_length=600, null=True),
                ),
                ("bio", models.TextField(blank=True, null=True)),
                (
                    "profile_pic",
                    models.ImageField(
                        blank=True,
                        default="images/user-default.png",
                        null=True,
                        upload_to="profile_pics/",
                    ),
                ),
                (
                    "social_github",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "social_linkedin",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "social_website",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "social_twitter",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "user",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
