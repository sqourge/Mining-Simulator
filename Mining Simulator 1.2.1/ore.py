class Ore:
    def __init__(self, name: str, value: int, rarity: int, hardness: int):
        self.name = name
        self.value = value
        self.rarity = rarity
        self.hardness = hardness
        # Also started_printing: float, it is set to 0 after starting to print or resetting by collecting ore
        
# Name, value, rarity, hardness
COAL = Ore('Coal', 1, 1, 1)  # Wooden Pickaxe
IRON = Ore('Iron', 3, 5, 3)  # Stone Pickaxe
SILVER = Ore('Silver', 15, 10, 5)  # Copper Pickaxe
GOLD = Ore('Gold', 50, 30, 5)
PLATINUM = Ore('Platinum', 30, 40, 10)  # Iron Pickaxe
EMERALD = Ore('Emerald', 50, 45, 15)  # Steel Pickaxe
SAPPHIRE = Ore('Sapphire', 25, 20, 25)  # Titanium Pickaxe
RUBY = Ore('Ruby', 45, 40, 25)
DIAMOND = Ore('Diamond', 150, 100, 30)  # Emerald Pickaxe
RED_DIAMOND = Ore('Red Diamond', 20_000, 10_000, 20)  # 100x rarer than Diamonds
PURPLE_DIAMOND = Ore('Purple Diamond', 25_000_000, 10_000_000, 20)  # 1000x rarer than Red Diamonds
SOLAR_CRYSTAL = Ore('Solar Crystal', 150_000_000_000, 50_000_000_000, 75) # 500x rarer than Purple Diamonds
# Solar Crystal would take 48.23 days on average to mine with Level 3 NB-3x Nanobots


ORES = (
    COAL, IRON, SILVER, GOLD, PLATINUM, EMERALD, SAPPHIRE, RUBY, DIAMOND,
    RED_DIAMOND, PURPLE_DIAMOND, SOLAR_CRYSTAL
)
