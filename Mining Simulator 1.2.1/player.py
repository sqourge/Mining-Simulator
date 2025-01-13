from ore import ORES
from researchoption import ResearchOption
from tool import (
    Tool, 
    WOODEN_PICKAXE, 
    STONE_PICKAXE, 
    COPPER_PICKAXE, 
    IRON_PICKAXE, 
    STEEL_PICKAXE, 
    TITANIUM_PICKAXE, 
    EMERALD_PICKAXE, 
    RUBY_PICKAXE, 
    DIAMOND_PICKAXE
)
from utilities import fastprint, format_number, slowprint

class Player:

    def __init__(self, name: str):
        self.name = name
        self.money: int = 0
        self.possible_actions = [
            "Shop", "Inventory", "Upgrade Tool", "Research", "Mine"
        ]
        self.equipped_tool = WOODEN_PICKAXE
        self.ore_bag: dict = {}
        self.purchasable_tools = [ # Will change based on research and tools bought before
            WOODEN_PICKAXE, STONE_PICKAXE, COPPER_PICKAXE, IRON_PICKAXE,
            STEEL_PICKAXE, TITANIUM_PICKAXE, EMERALD_PICKAXE, RUBY_PICKAXE, DIAMOND_PICKAXE
        ]
        self.research_completed = []
        self.current_research = None
        self.currently_printing = None
        self.gpu_slots = []

    def equip(self, tool: Tool) -> None:
        self.equipped_tool = tool

    def complete_research(self, research_option: ResearchOption) -> None:
        self.research_completed.append(research_option)
        if len(research_option.tools_unlocked) > 0:
            self.purchasable_tools.extend(research_option.tools_unlocked)
        if len(research_option.actions_unlocked) > 0:
            self.possible_actions.append(research_option.actions_unlocked)

    def clear_ore_bag(self) -> None:
        self.ore_bag = {ore: 0 for ore in ORES}

    def inventory(self) -> None:
        slowprint(f"\n{self.name}\'s Inventory:")
        slowprint(f"\n{self.equipped_tool.name} (£{format_number(self.equipped_tool.price)})")

        for ore, amount in self.ore_bag.items():
            if amount > 0:
                total_value = ore.value * amount
                fastprint(f"{format_number(amount)} x {ore.name} (£{format_number(total_value)})")