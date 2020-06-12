from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # having one-to-one relation with User model
    image = models.ImageField(default='potato.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} profile'
    