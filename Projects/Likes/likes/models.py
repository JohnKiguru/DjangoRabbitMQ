from django.db import models

# Create your models here.
class Quote(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    title = models.CharField(max_length=200)


    def __str__(self):
        return self.title
class QuoteUser(models.Model):
    user_id = models.IntegerField( blank=True)
    quote_id = models.IntegerField(unique=True, blank=True)

    def __str__(self):
        return f"User id {str(self.user_id)} Product id {str(self.quote_id)}"
