from time import sleep

from player import Player
from utilities import *

def view_gpus(player: Player) -> None:
    print()
    if len(player.gpu_slots) == 0:
        slowprint("\n<Craig> You don\'t have any GPUs yet.")
    else:
        slowprint("<Craig> Here are your GPUs:")
        for gpu in player.gpu_slots:
            fastprint(f"{gpu.name}")

    sleep(.5)