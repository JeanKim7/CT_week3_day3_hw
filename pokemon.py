from wrappers import PokemonAPI

def main():
    print("Welcome to the Pokedex! Enter the name of a pokemon and we will give you some information about it.")
    pokemon = PokemonAPI()
    berry = PokemonAPI()
    while True:
        input1 = input("What Pokemon would you like to learn about? ")
        print(pokemon.get_pokemon_info(input1))
        berry_input = input("Enter a berry name to get information on it: ")
        print(berry.get_berry_info(berry_input))
        continue_input = input("Enter anything to continue. Enter 'quit' to quit ")
        if continue_input == 'quit':
            break

main()
