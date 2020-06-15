from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

# Here each class will have its own table in the database
# Each attribute will be a field in the database
class Post(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    # Here on_delete ensures that if an user is deleted then all their posts will be 
    # deleted as well
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # It will assign the name of that object
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.pk})

    


 
