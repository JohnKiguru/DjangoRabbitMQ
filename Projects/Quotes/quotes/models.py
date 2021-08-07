from django.db import models

# Create your models here.
class Quote(models.Model):
    title = models.CharField(max_length=200)

    likes = models.PositiveIntegerField(default=0)

    def __dir__(self):
        return self.title