from buy_gpus import buy_gpus
from collect_crypto import collect_crypto
from player import Player
from utilities import fastprint, slowprint
from view_gpus import view_gpus

def crypto_menu(player: Player) -> None:
    POSSIBLE_CRYPTO_ACTIONS = ("Buy GPU", "Collect Crypto", "View GPUs", "Main Menu")

    while True:
        print()
        for action in POSSIBLE_CRYPTO_ACTIONS:
            fastprint(action)

        slowprint("\nWhat do you want to do?")
        while True:
            user_input = input("> ").lower()

            if user_input not in [action.lower() for action in POSSIBLE_CRYPTO_ACTIONS]:
                continue

            if user_input == "buy gpu":
                buy_gpus(player)
            elif user_input == "collect crypto":
                collect_crypto(player)
            elif user_input == "view gpus":
                view_gpus(player)
            elif user_input == "main menu":
                return
            break