from django.db import models
# Create your models here.

class Game(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200)
    release_date = models.DateField()
    category = models.CharField(max_length=200)
    played = models.BooleanField(default=False)
    slug = models.CharField(max_length=250)

    class Meta:
        ordering = 'name', 