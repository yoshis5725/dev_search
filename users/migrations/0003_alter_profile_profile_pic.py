# Generated by Django 5.2.1 on 2025-05-11 19:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0002_profile_username"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="profile_pic",
            field=models.ImageField(
                blank=True,
                default="user-default.png",
                null=True,
                upload_to="profile_pics/",
            ),
        ),
    ]
