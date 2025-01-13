from random import sample
from time import time

from graphicscard import GPUS
from player import Player
from utilities import fastprint, format_number, slowprint

MAX_GPU_SLOTS = 3

def buy_gpus(player: Player) -> None:
    slowprint(f"\n<Craig> Yo {player.name}!!!")
    slowprint("\n<Craig> Got some new GPUs today!")
    slowprint(f"\nBalance: £{format_number(player.money)}")
    gpu_names: dict = {}

    for gpu in sample(GPUS, 5):
        gpu_names[gpu.name.lower()] = gpu

    print()
    for gpu in gpu_names.values():
        fastprint(f"{gpu.name} - £{format_number(gpu.price)}")

    fastprint("Nothing")
    slowprint("\n<Craig> What you gonna buy?")

    user_input = input("> ").lower()

    if user_input == "nothing":
        slowprint("\n<Craig> Whatever.")
        return

    elif user_input not in [key.lower() for key in gpu_names]:
        slowprint("\n<Craig> You know what?")
        slowprint("\n<Craig> I don't have that.")
        return

    # GPU exists
    new_gpu = gpu_names[user_input]

    if player.money < gpu_names[user_input].price:
        slowprint("\n<Craig> You can\'t afford that?")
        slowprint("\n<Craig> Just don\'t be poor?")
        slowprint("\n<Craig> It\'s not that difficult!!!")
        return

    player.money -= new_gpu.price
    slowprint(f"\nYou bought the {new_gpu.name} for £{format_number(new_gpu.price)}")

    if len(player.gpu_slots) < MAX_GPU_SLOTS:
        new_gpu.started_mining = time()
        player.gpu_slots.append(new_gpu)
        slots_remaining = MAX_GPU_SLOTS - len(player.gpu_slots)
        if slots_remaining == 0:
            slowprint("Your GPU slots are now full.")
            slowprint("Next time you will have to replace one of your GPUs.")
        elif slots_remaining == 1:
            slowprint("Now you have 1 slot left")
        else:
            slowprint(f"Now you have {slots_remaining} slots left.")

        slowprint("\n<Craig> Yayyyyyy")

    else:
        slowprint("You have no more slots left.")
        print()
        for gpu in player.gpu_slots:
            fastprint(f"{gpu.name}")

        slowprint("\n<Craig> Which GPU do you want to replace?")
        gpu_names = {gpu.name.lower(): gpu for gpu in player.gpu_slots}

        while True:
            user_input = input("> ").lower()
            if user_input not in [gpu.name.lower() for gpu in player.gpu_slots]:
                continue
            else:
                old_gpu = gpu_names[user_input]
                player.gpu_slots.remove(old_gpu)
                new_gpu.started_mining = time()
                player.gpu_slots.append(new_gpu)
                slowprint("\n<Craig> Ok.")
                slowprint(f"\n<Craig> You can have £{format_number(old_gpu.price/2)} for the {old_gpu.name}.")
                break