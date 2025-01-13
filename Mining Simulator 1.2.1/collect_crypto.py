from time import time

from player import Player
from utilities import format_number, slowprint

CRYPTO_SELL_PRICE = 45_000

def collect_crypto(player: Player) -> None:
    if len(player.gpu_slots) == 0:
        slowprint("\n<Craig> You don\'t have anything to collect.")
        return

    crypto_collected: float = 0
    for gpu in player.gpu_slots:
        time_mining_crypto = time() - gpu.started_mining
        crypto_collected += time_mining_crypto * gpu.speed
        gpu.started_mining = time()
    slowprint(f"\n<Craig> You mined {format_number(crypto_collected)} BTC.")
    total_sell_price = int(crypto_collected * CRYPTO_SELL_PRICE)
    player.money += total_sell_price
    slowprint(f"\nSold to Craig for £{format_number(total_sell_price)}.")
    slowprint(f"\nBalance: £{format_number(player.money)}")