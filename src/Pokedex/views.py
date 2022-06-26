from django.shortcuts import render
from .models import Pokemon
import requests


def index(request):
    all_pokemons = Pokemon.objects.all()
    return render(request, "Pokedex/index.html", context={"pokemons": all_pokemons})


def details(request, pokemon):
    response_json = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}/").json()

    hp_stat = response_json['stats'][0]["base_stat"]
    attack_stat = response_json['stats'][1]["base_stat"]
    defense_stat = response_json['stats'][2]["base_stat"]
    special_attack_stat = response_json['stats'][3]["base_stat"]
    special_defense_stat = response_json['stats'][4]["base_stat"]
    height = response_json["height"] #decimeters
    weight = response_json["weight"] #hectograms

    target_query = Pokemon.objects.filter(nom=pokemon).get()

    return render(request, "Pokedex/details.html", context={"hp_stat": hp_stat,
                                                            "attack_stat": attack_stat,
                                                            "defense_stat": defense_stat,
                                                            "special_attack_stat": special_attack_stat,
                                                            "special_defense_stat": special_defense_stat,
                                                            "height": height,
                                                            "weight": weight,
                                                            "pokemon": target_query})
