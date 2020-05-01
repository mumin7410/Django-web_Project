from django.db import models

# Create your models here.
class post(models.Model):
    name = models.CharField(max_length=200)
    desp = models.TextField()

class card(models.Model):
    image = models.ImageField(blank=True, null=True)
    message = models.CharField(max_length=300)
    topic = models.CharField(max_length=50)
