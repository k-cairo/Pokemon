from django.shortcuts import render
from .models import Pokemon


def index(request):
    all_pokemons = Pokemon.objects.all()
    return render(request, "Pokedex/index.html", context={"pokemons": all_pokemons})
