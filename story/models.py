
# Create your models here.
from django.db import models

class Line(models.Model):
    text = models.CharField(max_length=255)

