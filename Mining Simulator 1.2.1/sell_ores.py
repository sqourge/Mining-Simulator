from player import Player
from utilities import fastprint, format_number

def sell_ores(player: Player) -> None:

    money_gained = 0
    for ore, amount in player.ore_bag.items():
        if amount > 0:
            money_gained += ore.value * amount
    player.money += money_gained
    fastprint(f"\nYou sold all your ores for £{format_number(money_gained)}.")
    player.clear_ore_bag()