from pprint import pprint

from django.core.management import BaseCommand

from Pokedex.models import Pokemon
import requests

NUMBER_OF_POKEMON = 905
API_ENDPOINT = f"https://pokeapi.co/api/v2"


class Command(BaseCommand):
    help = 'Update Pokemon Database'

    def handle(self, *args, **options):
        for id_pokemon in range(1, NUMBER_OF_POKEMON+1):
            response_json = requests.get(f"{API_ENDPOINT}/pokemon/{id_pokemon}/", verify=False).json()

            pokemon_id = response_json.get('id')
            pokemon_name = response_json.get('name')
            pokemon_type_list = [pokemon_type['type']['name'] for pokemon_type in response_json.get("types")]
            if len(Pokemon.objects.filter(nom=pokemon_name)) == 0:
                Pokemon.objects.create(pokemon_id=pokemon_id,
                                       nom=pokemon_name,
                                       type=pokemon_type_list,
                                       img_link=f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{pokemon_id}.png")
                print(f"Pokemon : {pokemon_name} add to Database Successfully")

        self.stdout.write('Database Updated Successfully')
