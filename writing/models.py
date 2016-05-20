from django.db import models

# Create your models here.
class Writing(models.Model):
    content = models.TextField()
    
