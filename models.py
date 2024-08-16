from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    USER_TYPE_CHOICES = [
        ('Patient', 'Patient'),
        ('Doctor', 'Doctor'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
    address_line1 = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)
    
    def __str__(self):
        return self.user.username
