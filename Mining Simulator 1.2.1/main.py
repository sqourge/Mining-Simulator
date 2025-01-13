# Python 3.8
from crypto_menu import crypto_menu
from mine import mine
from player import Player
from print_ores import print_ores
from research import research
from sell_ores import sell_ores
from shop import shop
from upgrade_tool import upgrade_tool
from utilities import fastprint, format_number, slowprint


def main() -> None:
    slowprint("###########################################################################")
    print("###########################################################################")
    print("###########################################################################")
    print("######################  WELCOME TO MINING SIMULATOR  ######################")
    print("###########################################################################")
    print("###########################################################################")
    print("###########################################################################")

    slowprint("\nWhat is your name?")
    p1 = Player(input("> ").title())
    p1.clear_ore_bag()

    slowprint(f"\nHello {p1.name}!")

    while True:
        slowprint(f"\nBalance: £{format_number(p1.money)}")
        print()

        if "Sell Ores" in p1.possible_actions:
            p1.possible_actions.remove("Sell Ores")
        if sum(p1.ore_bag.values()) > 0:
            p1.possible_actions.append("Sell Ores")

        for action in p1.possible_actions:
            fastprint(f"{action}")
        fastprint("\nWhat do you want to do?")

        while True:
            user_input = input("> ").lower()

            if user_input not in [action.lower() for action in p1.possible_actions]:
                continue

            if user_input == "shop":
                shop(p1)
            elif user_input == "inventory":
                p1.inventory()
            elif user_input == "upgrade tool":
                upgrade_tool(p1, p1.equipped_tool)
            elif user_input == "research":
                research(p1)
            elif user_input == "mine":
                mine(p1)
            elif user_input == "sell ores" and "Sell Ores" in p1.possible_actions:
                sell_ores(p1)
            elif user_input == "print ores" and "Print Ores" in p1.possible_actions:
                print_ores(p1)
            elif user_input == "crypto" and "Crypto" in p1.possible_actions:
                crypto_menu(p1)

            break

if __name__ == "__main__":
    main()