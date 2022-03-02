from django.db import models


# Create your models here.
class Coach(models.Model):

    class Meta:
        verbose_name_plural = 'Coaches'

    name = models.CharField(max_length=254)
    position = models.CharField(max_length=254, default="", blank=True)
    rank = models.CharField(max_length=254)
    awards = models.CharField(max_length=254, default="", blank=True)
    bio = models.TextField()
    classes = models.CharField(max_length=254,default="", blank=True)
    image_url = models.URLField(max_length=1024, default="", blank=True)
    image = models.ImageField(default="", blank=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name
