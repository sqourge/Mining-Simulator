from random import randint
from time import time

from player import Player
from utilities import *

def print_ores(player: Player) -> None:

    if player.currently_printing is None:

        if sum(player.ore_bag.values()) == 0:
            slowprint("\n<Ore Printer> YOU DO NOT HAVE ANY ORES.")
            slowprint("\n<Ore Printer> COME BACK LATER.")
            return

        print()
        ores_in_bag_names: dict = {}
        for ore, amount in player.ore_bag.items():
            if amount > 0:
                fastprint(ore.name)
                ores_in_bag_names[ore.name.lower()] = ore

        slowprint("Cancel")
        slowprint("\n<Ore Printer> ENTER ORE INTO MACHINE TO BEGIN PRINTING.")
        while True:
            user_input = input("> ").lower()

            if user_input == "cancel":
                slowprint("\n<Ore Printer> GOODBYE.")
                return

            elif user_input in ores_in_bag_names:
                player.currently_printing = ores_in_bag_names[user_input]
                player.ore_bag[player.currently_printing] -= 1
                player.currently_printing.print_start_time = time()
                slowprint(f"\n<Ore Printer> PRINTING {player.currently_printing.name.upper()}...")
                slowprint("\n<Ore Printer> COME BACK LATER.")
                return

            else:
                continue

    else:
        ore = player.currently_printing
        total_print_time = time() - ore.print_start_time
        total_attempts = round(total_print_time * (10_000 + player.equipped_tool.strength))
        ore_printed_amount = 0
        for _ in range(total_attempts):
            if randint(1, ore.rarity) == 1:
                ore_printed_amount += 1
        player.ore_bag[ore] += ore_printed_amount

        if ore_printed_amount == 0:
            slowprint("\n<Ore Printer> SORRY, NO ORES PRINTED.")
        else:
            slowprint(f"\n<Ore Printer> PRINTED {format_number(ore_printed_amount)} X {ore.name}".upper())

        slowprint(f"\n<Ore Printer> KEEP PRINTING {ore.name.upper()}?")
        print()
        slowprint("Yes")
        slowprint("No")
        user_input = input("> ").lower()
        if user_input == "yes":
            player.currently_printing.print_start_time = time()
            slowprint(f"\n<Ore Printer> STILL PRINTING {player.currently_printing.name.upper()}...")
            slowprint("\n<Ore Printer> COME BACK LATER.")
        elif user_input == "no":
            player.currently_printing = None
            player.ore_bag[ore] += 1
            slowprint("\n<Ore Printer> ORE RETURNED.")
            slowprint("\n<Ore Printer> GOODBYE")
        else:
            player.currently_printing = None
            player.ore_bag[ore] += 1
            slowprint("\n<Ore Printer> INVALID RESPONSE.")
            slowprint("\n<Ore Printer> ORE RETURNED.")
            slowprint("\n<Ore Printer> GOODBYE")