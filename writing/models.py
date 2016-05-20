from django.db import models

class Writing(models.Model):
    content = models.TextField()
    title = models.CharField(max_length=255)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.title
