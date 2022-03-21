from django.db import models
from django.contrib.auth.models import User
#from ckeditor.fields import RichTextField


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, upload_to='profile_pics')
    #bio = RichTextField(blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} Profile'