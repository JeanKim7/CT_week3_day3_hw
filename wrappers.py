import requests

class Pokemon:

    def

class PokemonAPI:
    """A class that represents the data from a website"""    
    base_url = "https://pokeapi.co/api/v2/"
    
    def __get_pokemon(self, pokemon_species):    
        request_url = f"{self.base_url}pokemon/{pokemon_species}"
        response = requests.get(request_url)
        if response.ok:
            data = response.json()
            return data
        else:
            print(response.json)
            return None
        
    def get_pokemon_info(self, pokemon_spec):
        pokemon_info = self.__get_pokemon(self, pokemon_spec)
        if pokemon_info:
            pokemon_name = pokemon_spec
            pokemon_weight = pokemon_info['weight']
            pokemon_height = pokemon_info['height']
            # Create an instance of a pokemon
