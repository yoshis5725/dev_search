from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from users.models import Profile


####### SIGNALS ########
# This signal is triggered when a User instance is created
# and creates a corresponding Profile instance.
# The signal is connected to the post_save signal of the User model.
# The create_profile function is called when a User instance is saved.
# The function checks if the instance was created and then creates a Profile instance
# with the same username, email, first name, and last name as the User instance.

# The delete_user function is triggered when a Profile instance is deleted.
# It deletes the associated User instance.
# The post_delete signal is connected to the Profile model.
# The delete_user function is called when a Profile instance is deleted.
# The function retrieves the User instance associated with the Profile instance
# and deletes it.

###################################################
# These are connected through the apps.py file
# in the users app, where the signals are registered.
###################################################


def create_profile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            first_name=user.first_name,
            last_name=user.last_name,
        )


def delete_user(sender, instance, **kwargs):
    user = instance.user
    user.delete()
    print('User deleted')

post_save.connect(create_profile, sender=User)
post_delete.connect(delete_user, sender=Profile)