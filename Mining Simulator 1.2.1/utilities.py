from time import sleep

def slowprint(text: str) -> None:
    sleep(.3)
    print(text)
    sleep(.3)


def fastprint(text: str) -> None:
    sleep(.2)
    print(text)


def format_number(number: int) -> str:
    SUFFIXES = {
        1e27: "Oc",  # Please don't make more money than this
        1e24: "Sp",
        1e21: "Sx",
        1e18: "Qt",
        1e15: "Qd",
        1e12: "T",
        1e9: "B",
        1e6: "M",
        1e3: "k"
    }

    for limit, suffix in SUFFIXES.items():
        if number >= limit:
            result = number / limit
            if round(result) == round(result, 2):
                return f"{round(result)}{suffix}"
            else:
                return f"{round(result, 2)}{suffix}"

    return number


def format_time(seconds: int) -> str:
    seconds = int(seconds)
    minutes = seconds // 60
    seconds = seconds % 60
    if seconds == 0:
        return 'less than a second'
    if minutes > 0:
        return f'{minutes}m {seconds}s'
    else:
        return f'{seconds}s'