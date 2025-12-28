# ui.py

from collections.abc import Sequence
from .system_commands import SystemCommand

def info(msg: str) -> None:
    print(f"\n\033[36m{msg}\033[0m")    # cyan

def warning(msg: str) -> None:
    print(f"\033[31m{msg}\033[0m")      # red

def handle_user_input(prompt: str, valid_choices: Sequence[str], *, allow_back: bool = True) -> SystemCommand | str:
    while True:
        choice = input(prompt).strip().lower()

        if choice in ("q", "quit", "exit"):
            return SystemCommand.QUIT
        if allow_back and choice in ("b", "back"):
            return SystemCommand.BACK
        if choice in valid_choices:
            return choice

        print("Invalid choice, try again.")