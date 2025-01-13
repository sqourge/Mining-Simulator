class Tool:
    def __init__(self, name: str, tool_type: str, price: int, strength: int):
        self.name = name
        self.original_name = name # Not including the prefix if given one
        self.tool_type = tool_type
        self.price = price
        self.strength = strength
        self.breaking_power = strength  # Same as strength but can't increase
        self.level = 1

# Name, price, strength
WOODEN_PICKAXE = Tool('Wooden Pickaxe', 'pickaxe', 1, 2)
STONE_PICKAXE = Tool('Stone Pickaxe', 'pickaxe', 10, 3)
COPPER_PICKAXE = Tool('Copper Pickaxe', 'pickaxe', 50, 5)
IRON_PICKAXE = Tool('Iron Pickaxe', 'pickaxe', 100, 10)
STEEL_PICKAXE = Tool('Steel Pickaxe', 'pickaxe', 200, 15)
TITANIUM_PICKAXE = Tool('Titanium Pickaxe', 'pickaxe', 350, 25)
EMERALD_PICKAXE = Tool('Emerald Pickaxe', 'pickaxe', 750, 30)
RUBY_PICKAXE = Tool('Ruby Pickaxe', 'pickaxe', 1500, 50)
DIAMOND_PICKAXE = Tool('Diamond Pickaxe', 'pickaxe', 2500, 75)

BASIC_DRILL = Tool('Basic Drill', 'drill', 5000, 150)
LASER_DRILL = Tool('Laser Drill', 'drill', 25_000, 250)
PLASMA_DRILL = Tool('Plasma Drill', 'drill', 50_000, 350)

NB1_NANOBOTS = Tool('NB-1 Nanobots', 'nanobot', 100_000, 1000)
NB2_NANOBOTS = Tool('NB-2 Nanobots', 'nanobot', 200_000, 1500)
NB3_NANOBOTS = Tool('NB-3 Nanobots', 'nanobot', 500_000, 2500)
NB3X_NANOBOTS = Tool('NB-3X Nanobots', 'nanobot', 1_000_000, 4000)

LEVEL2_PREFIXES = {
    'pickaxe': 'Refined',
    'drill': 'Fast',
    'nanobot': 'Advanced'
}

LEVEL3_PREFIXES = {
    'pickaxe': 'Legendary',
    'drill': 'Very Fast',
    'nanobot': 'Supercharged'
}