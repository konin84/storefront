from django.db import models
from datetime import timezone, date, datetime


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Categories'


class Photo(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    images = models.ImageField(null=False, upload_to='gallery/gallery')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description
