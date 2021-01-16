import os


class colors():
    RESET = '\033[0m'

    WHITE = '\033[37m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    MAGENTA = '\033[95m'
    BLUE = '\033[96m'

    BG_BLUE = '\033[46m'
    BG_WHITE = '\033[47m'
    BG_RED = '\033[101m'
    BG_GREEN = '\033[102m'
    BG_YELLOW = '\033[103m'
    BG_MAGENTA = '\033[105m'


def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')
