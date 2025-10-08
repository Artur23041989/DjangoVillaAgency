from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100, default="Агент по недвижимости")
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    photo = models.ImageField(null=True, blank=True, upload_to='agents_photos/', default='profiles/user-default.png')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name