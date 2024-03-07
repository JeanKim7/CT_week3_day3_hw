import requests

class Pokemon:

    def __init__(self, name, height, weight, move1):
        self.name = name
        self.height = height
        self.weight = weight
        self.move1 = move1

    def __str__(self):
        return f"{self.name.title()} has a height of {self.height} and a weight of {self.weight}.\nIt also has a move of {self.move1}."

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
        pokemon_info = self.__get_pokemon(pokemon_spec)
        if pokemon_info:
            pokemon_name = pokemon_spec
            pokemon_height = pokemon_info['height']
            pokemon_weight = pokemon_info['weight']
            pokemon_move1 = pokemon_info['moves'][0]['move']['name']
            #Create an instance of a pokemon with above info
            pokemon_instance = Pokemon(pokemon_name, pokemon_height, pokemon_weight, pokemon_move1)
            return pokemon_instance
        else:
            return "No data on this pokemon"
