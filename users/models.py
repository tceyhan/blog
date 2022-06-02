from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    portfolio = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    username =models.EmailField("Email Address", unique=True)
    REQUIRED_FIELDS =[] 
    # emaili sormasın diye boş bıraktık

class UserProfile(models.Model):
    bio = models.TextField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', default='default.jpg')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username
   
    
