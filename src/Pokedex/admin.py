from django.contrib import admin
from .models import Pokemon


@admin.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):
    list_display = ('pokemon_id', "nom", "type")
    list_filter = ('type', )
