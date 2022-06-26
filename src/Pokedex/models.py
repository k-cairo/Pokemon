from django.db import models


class Pokemon(models.Model):
    pokemon_id = models.IntegerField()
    nom = models.CharField(max_length=100)
    img_link = models.URLField(blank=True)
    type = models.JSONField()
