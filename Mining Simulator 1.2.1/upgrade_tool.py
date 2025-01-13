from random import randint
from time import sleep

from player import Player
from tool import LEVEL2_PREFIXES, LEVEL3_PREFIXES, Tool
from utilities import fastprint, format_number, slowprint

def upgrade_tool(player: Player, tool: Tool) -> None:
    if tool.level == 3:  
        slowprint("\n<Blacksmith> This is already at the maximum level...")
        return

    upgrade_cost = tool.price * 2

    if player.money < upgrade_cost:
        slowprint("\n<Blacksmith> You don\'t have enough money to upgrade this tool..." )
        slowprint(f"\n<Blacksmith> You need at least £{format_number(upgrade_cost)}.")
        return

    slowprint(f"\n<Blacksmith> This tool is at level {tool.level}")
    slowprint(f"\n<Blacksmith> Do you want me to upgrade it for £{format_number(upgrade_cost)}?")

    print()
    fastprint("Yes")
    fastprint("No")

    user_input = input("> ").lower()

    if user_input != "yes":
        slowprint("\n<Blacksmith> Fine.")
        return

    slowprint("\n<Blacksmith> Okay I\'ll get on with it.")
    player.money -= upgrade_cost
    sleep(.5)
    for _ in range(randint(2, 4)):
        print("...")
        sleep(1)
    tool.level += 1
    if tool.level == 2:
        prefix = LEVEL2_PREFIXES
        tool.strength *= 2
        tool.price *= 2
    else:
        prefix = LEVEL3_PREFIXES
        tool.strength *= 1.5
        tool.price *= 2
    tool.strength = int(tool.strength)
    tool.name = f"{prefix[tool.tool_type]} {tool.original_name}"

    slowprint("\n<Blacksmith> Ok done.")
    if tool.tool_type == 'nanobot':
        slowprint("\n<Blacksmith> Here are your nanobots.")
    else:
        slowprint(f"\n<Blacksmith> Here is your {tool.name}.")