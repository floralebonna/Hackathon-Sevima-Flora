from django.db import models

# Create your models here.
class CompressImage(models.Model):
    orginal = models.ImageField(upload_to='original/')
    compres = models.ImageField(upload_to='compres/', null =True, blank=True)
