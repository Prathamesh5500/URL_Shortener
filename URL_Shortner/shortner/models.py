from django.db import models

# Create your models here.
class urlData(models.Model):
    url = models.URLField(max_length=200)
    full_short_url = models.URLField(max_length=100, unique=True, null=True)