from random import randint

from player import Player
from researchoption import ROBOTS
from utilities import fastprint, format_number, slowprint

def shop(player: Player) -> None:
    tools = player.purchasable_tools
    tool_names = {
        tool.name.lower(): tool
        for tool in tools if tool.breaking_power > player.equipped_tool.breaking_power
    }

    if len(tool_names) == 0:
        slowprint("\n<Shopkeeper> Sorry man all my tools are sold! Come back later!")
        slowprint("\n<Shopkeeper> Go research something while you\'re at it")
        return

    slowprint(f"\n<Shopkeeper> Yo {player.name} my favourite customer!")
    slowprint("\n<Shopkeeper> What do you want to buy?\n")

    for tool in tool_names.values():
        fastprint(f"{tool.name} - £{format_number(tool.price)}")

    fastprint("Nothing\n")

    user_input = input("> ").lower()

    if user_input == "nothing":
        slowprint("\n<Shopkeeper> Bye.")
        return

    elif user_input not in tool_names:

        slowprint("\n<Shopkeeper> I don\'t have any of that...")
        slowprint("\n<Shopkeeper> Who do you think you are?")

    else:
        tool = tool_names[user_input]
        if player.money >= tool.price:  # The player has enough money
            slowprint(
                f"\nYou bought the {tool.name} for £{format_number(tool.price)}!")
            if randint(1, 5) == 5:
                slowprint("\n<Shopkeeper> I will DEFINITELY spend this money on something legal...")
            else:
                if ROBOTS in player.research_completed:
                    slowprint("\n<Shopkeeper> Rah I can feed my nanobots now!")
                else:
                    slowprint("\n<Shopkeeper> Rah I can feed my family now!")
            player.money -= tool.price
            player.equip(tool)
        else:  # The player does not have enough money
            slowprint("\n<Shopkeeper> You can\'t even afford that...")
            slowprint("\n<Shopkeeper> Sorry.")