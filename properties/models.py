from django.db import models
from django.contrib.auth.models import User



class Property(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    image = models.ImageField(null=True, blank=True, upload_to='properties/%Y/%m/%d/', default='default.jpg')
    bedrooms = models.PositiveIntegerField(null=True, blank=True)
    bathrooms = models.PositiveIntegerField(null=True, blank=True)
    area = models.CharField(max_length=50, null=True, blank=True)
    floor = models.PositiveIntegerField(null=True, blank=True)
    parking = models.PositiveIntegerField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



class Review(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Пользователь'
    )
    review_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']  # новые отзывы сначала
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return f'Отзыв от {self.user.username} at {self.created_at.strftime("%d.%m.%Y %H:%M")}'
