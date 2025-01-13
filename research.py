from time import time

from researchoption import research_available, ResearchOption
from utilities import slowprint, fastprint, format_number, format_time
from tool import BASIC_DRILL, LASER_DRILL, PLASMA_DRILL, NB1_NANOBOTS, NB2_NANOBOTS, NB3_NANOBOTS, NB3X_NANOBOTS

class Player:
    pass # This stops circular imports, it would go on forever and do nothing.

def research(player: Player) -> None:

    for available_research in player.research_completed:
        if available_research in research_available:
            research_available.remove(available_research)

    if len(research_available) == 0:
        slowprint("\n<Scientist> Nothing else to research...")
        return

    lowest_price = None
    for possible_research in research_available:
        if lowest_price is None or lowest_price > possible_research.price:
            lowest_price = possible_research.price

    if player.current_research is None:

        if player.money < lowest_price:
            slowprint("\n<Scientist> You don\'t have enough money to research anything!")
            slowprint(f"\n<Scientist> Come back when you have atleast £{format_number(lowest_price)}!")
            return

        slowprint("\n<Scientist> Hello!")
        slowprint("\n<Scientist> You have enough money to research!")
        print()
        for option in research_available:
            fastprint(f"{option.name.title()} - £{format_number(option.price)}")
        fastprint("Nothing")
        slowprint("\n<Scientist> What do you want to research?")
        user_input = input("> ").lower()

        if user_input == "nothing":
            print("\n<Scientist> Okay, bye then...")
            return

        research_available_names = {
            possible_research.name.lower(): possible_research
            for possible_research in research_available
        }

        if user_input not in research_available_names:
            print("\n<Scientist> Bye.")
            return

        option = research_available_names[user_input]

        if player.money < option.price:
            slowprint("\n<Scientist> You don\'t even have enough money for that?")
            return

        else:
            player.money -= option.price
            player.current_research = option
            player.current_research.start_time = time()
            slowprint(f"\n<Scientist> I\'m now researching {player.current_research.name} for you...")
            slowprint(f"\n<Scientist> Come back in {format_time(player.current_research.seconds_required)}")

    else:
        total_research_time = time() - player.current_research.start_time
        if total_research_time < player.current_research.seconds_required:
            slowprint(f"\n<Scientist> I\'m still researching {player.current_research.name}.")
            time_remaining = player.current_research.seconds_required - total_research_time
            slowprint(f"\n<Scientist> Come back in {format_time(time_remaining)}!")

        else:
            slowprint(f"\n<Scientist> I have finished researching {player.current_research.name}!")
            if len(player.current_research.tools_unlocked) > 0:
                slowprint("\nYou can now buy:\n")
                for tool in player.current_research.tools_unlocked:
                    fastprint(tool.name)
            player.complete_research(player.current_research)
            player.current_research = None