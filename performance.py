from time import time
from colorama import Fore


def performance(func):
    def wrapper(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        finish_time = time()
        seconds = round(finish_time - start_time, 2)
        colored_seconds = f"{Fore.LIGHTMAGENTA_EX}{seconds}"
        print(
            f"{Fore.GREEN}The script has finished, and it took {colored_seconds} seconds"
        )
        return result

    return wrapper
