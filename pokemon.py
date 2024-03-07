from wrappers import PokemonAPI

def main():
    print("Welcome to the Pokedex! Enter the name of a pokemon and we will give you some information about it.")
    pokemon = PokemonAPI()
    while True:
        input1 = input("What Pokemon would you like to learn about? ")
        print(pokemon.get_pokemon_info(input1))
        continue_input = input("Enter anything to continue. Enter 'quit' to quit ")
        if continue_input == 'quit':
            break

main()
