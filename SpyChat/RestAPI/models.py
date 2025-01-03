from django.db import models

# Create your models here.
class Picture(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='photos/')