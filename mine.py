from random import randint
from time import time

from ore import ORES
from player import Player
from utilities import fastprint, format_number, slowprint

def mine(player: Player) -> None:
    mine_total_value: int = 0
    mine_start_time = time()
    slowprint("\nYou are mining...")
    slowprint("Write \'Stop\' to stop mining...")

    ores_mined = {
        ore: 0
        for ore in ORES if player.equipped_tool.breaking_power >= ore.hardness
    }

    while True:
        user_input = input("\n> ").lower()
        if user_input == "stop":
            print()
            mine_end_time = time()
            total_mining_time = mine_end_time - mine_start_time

            for _ in range(round(total_mining_time * player.equipped_tool.strength)):
                for key in ores_mined:
                    if randint(1, key.rarity) == 1:
                        ores_mined[key] += 1

            for ore, amount in ores_mined.items():
                if amount > 0:
                    fastprint(f"You mined {format_number(amount)} x {ore.name}")
                    player.ore_bag[ore] += amount
                    mine_total_value += amount * ore.value

            slowprint(f"Total value: £{format_number(mine_total_value)}")
            break