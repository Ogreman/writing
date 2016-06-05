from django.db import models

class Writing(models.Model):
    
    content = models.TextField()
    title = models.CharField(max_length=255)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['id']

    def word_count(self):
        return len(self.content.split())


class View(models.Model):

    writing = models.ForeignKey('Writing')
    created = models.DateTimeField('date created', auto_now_add=True)

    def __str__(self):
        return u'{} at {}'.format(
            self.writing,
            self.created)


class Message(models.Model):

    content = models.TextField('message')
    created = models.DateTimeField('date created', auto_now_add=True)
    email = models.EmailField(blank=True)

    def __str__(self):
        return '{} message at {}'.format(
            'Contactable' if self.email else 'Anonymous',
            self.created)
