
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from PIL import Image
from django.shortcuts import reverse


class User(AbstractUser):
	friends = models.ManyToManyField("User", blank=True)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jfif', upload_to='profile_pics')
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.user.username} Profile'

    '''def save(self):
        super().save()'''

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


    # def get_absolute_url(self):
    #     return reverse('home:profile_detail', kwargs={'pk': self.pk})


class Friend_Request(models.Model):
	from_user = models.ForeignKey(
		User, related_name='from_user', on_delete = models.CASCADE)
	to_user = models.ForeignKey(
		User, related_name='to_user', on_delete=models.CASCADE)




		
