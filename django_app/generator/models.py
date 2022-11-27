from django.db import models

# Create your models here.
class Template(models.Model):
    intro = models.TextField()
    chapitres = models.TextField()
    conclusion = models.TextField()