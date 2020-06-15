from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # having one-to-one relation with User model
    image = models.ImageField(default='potato.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} profile'

    # Overwrite save method
    # This is a preexisting method
    def save(self):
        super().save()

        # load the image
        img = Image.open(self.image.path)
        # Resize the image

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
        img.save(self.image.path)
    