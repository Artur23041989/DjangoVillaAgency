from django.db import models

# Create your models here.

class Properties(models.Model):
    details = models.TextField(null=True, blank=True)
    category = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    image = models.ImageField(null=True, blank=True, upload_to='properties/')
    bedrooms = models.PositiveIntegerField(null=True, blank=True)
    bathrooms = models.PositiveIntegerField(null=True, blank=True)
    area = models.CharField(max_length=50, null=True, blank=True)
    floor = models.PositiveIntegerField(null=True, blank=True)
    parking = models.PositiveIntegerField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.details