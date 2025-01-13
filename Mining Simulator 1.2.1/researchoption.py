from tool import BASIC_DRILL, LASER_DRILL, PLASMA_DRILL, NB1_NANOBOTS, NB2_NANOBOTS, NB3_NANOBOTS, NB3X_NANOBOTS

class ResearchOption:
    def __init__(self, name: str, price: int, seconds_required: int, tools_unlocked: list, actions_unlocked: list):
        self.name = name
        self.price = price
        self.seconds_required = seconds_required
        self.tools_unlocked = tools_unlocked
        self.actions_unlocked = actions_unlocked
        # Also start_time: float, it is set to 0 after the research is begun

DRILLS = ResearchOption(
    "Drills", 5000, 15,
    (BASIC_DRILL, LASER_DRILL, PLASMA_DRILL), ()
)

ROBOTS = ResearchOption(
    "Robots", 50_000, 20,
    (NB1_NANOBOTS, NB2_NANOBOTS, NB3_NANOBOTS, NB3X_NANOBOTS), ()
)

ORE_PRINTING = ResearchOption("Ore Printing", 500_000, 25, (), "Print Ores")
CRYPTOCURRENCY = ResearchOption("Cryptocurrency", 1_000_000, 30, (), "Crypto")

research_available = [DRILLS, ROBOTS, ORE_PRINTING, CRYPTOCURRENCY]