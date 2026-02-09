import time


def create_new_pokemon():
    # DUMMY FUNCTION -> Will never exit
    while True:
        pass


def attack_pokemon(poke_list):
    # DUMMY FUNCTION -> Will never exit
    while True:
        pass


def welcome():
    print("Welcome to the game")


def main():
    game = True
    pokemon_storage = []

    welcome()
    while game:
        choice = input(
            "Please select\n1: Create new pokemon\n2: Attack a pokemon\nQ: Quit Game\n"
        )

        if choice == "1":
            print("Create Pokemon")
            new_pokemon = create_new_pokemon()
            pokemon_storage.append(new_pokemon)
        elif choice == "2":
            print("Attack Pokemon")
            attack_pokemon(pokemon_storage)
        elif choice in ("q", "Q"):
            print("Bye")
            game = False
        else:
            print("Invalid option")

        time.sleep(0.1)


if __name__ == "__main__":
    main()
