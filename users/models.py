from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save()
        img_ = Image.open(self.img.path)
        if img_.height > 300 or img_.width > 300:
            output_size = (300, 300)
            img_.thumbnail(output_size, Image.ANTIALIAS)
            img_.save(self.img.path)