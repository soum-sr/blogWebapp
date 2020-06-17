from django.db.models.signals import post_save
from django.contrib.auth.models import User # Sender
from django.dispatch import receiver # Receiver
from .models import Profile


# create a profile when a user is created
@receiver(post_save, sender = User) # The receiver receives a post_save signal from the User
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)



@receiver(post_save, sender = User) 
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

