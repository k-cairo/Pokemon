from django.core.management import BaseCommand
from pprint import pprint

from Pokedex.models import Pokemon
import requests

NUMBER_OF_POKEMON = 898
API_ENDPOINT = f"https://pokeapi.co/api/v2"


def convert_type_in_french(pokemon_type_list):
    for pokemon_type in pokemon_type_list:
        pokemon_type.replace("bug", "insecte").replace("fairy", "fée").replace("humanshape", "forme humaine")\
            .replace("mineral", "roche").replace("plant", "plante").replace("water3", "eau").replace("ditto", "normal")\
            .replace("")


class Command(BaseCommand):
    help = 'Update cards and corners Datas'

    def handle(self, *args, **options):
        for id_pokemon in range(1, 2):
            response_json = requests.get(f"{API_ENDPOINT}/pokemon-species/{id_pokemon}/", verify=False).json()

            pokemon_id = response_json.get('id')
            pokemon_is_legendary = response_json.get('is_legendary')
            pokemon_is_mythical = response_json.get('is_mythical')
            pokemon_type_list = [pokemon_type['name'] for pokemon_type in response_json.get('egg_groups')]
            pokemon_name = response_json.get('name')

            pokemon_espece = ""
            generas_all_languages = response_json['genera']
            for genera in generas_all_languages:
                if genera['language']['name'] == "en":
                    pokemon_espece = genera['genus']

            if len(Pokemon.objects.filter(nom=pokemon_name)) == 0:
                Pokemon.objects.create(pokemon_id=pokemon_id,
                                       nom=pokemon_name,
                                       espece=pokemon_espece,
                                       type=pokemon_type_list,
                                       pokemon_legendaire=pokemon_is_legendary,
                                       pokemon_mythique=pokemon_is_mythical
                                       img_link=f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{pokemon_id}.png")
                print(f"Pokemon : {pokemon_name} add to Database Successfully")

        self.stdout.write('Database Updated Successfully')
