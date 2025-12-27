# program.py

from collections.abc import Callable
from .system_commands import SystemCommand
from .ui import handle_user_input
from .toolboxes.dice import DiceToolbox
from .toolboxes.cards import CardsToolbox
from .toolboxes.calculator import CalculatorToolbox
from .toolboxes.journal import JournalToolbox
import time

MenuAction = Callable[[], SystemCommand | None]

class Program:
    def __init__(self) -> None:
        self._start_time = time.time()
        self._dice = DiceToolbox()
        self._cards = CardsToolbox()
        self._calc = CalculatorToolbox()
        self._journal = JournalToolbox()

        self._menu_actions: dict[str, tuple[str, MenuAction]] = {
            "1": ("Dice", self._dice.run),
            "2": ("Cards", self._cards.run),
            "3": ("Calculator", self._calc.run),
            "4": ("Journal", self._journal.run),
        }

    def run(self) -> None:
        while True:
            print("\n=== playbox Menu ===")
            for key, (label, _func) in self._menu_actions.items():
                print(f"{key}. {label}")
            print("q. Quit")

            choice = handle_user_input("Choose an option: ", list(self._menu_actions.keys()), allow_back=False)

            if choice is SystemCommand.QUIT:
                self._handle_quit()
                return

            if isinstance(choice, SystemCommand):
                print("Internal error: unexpected command.")
                continue

            _label, func = self._menu_actions[choice]
            result = func()

            if result is SystemCommand.QUIT:
                self._handle_quit()
                return

    def _handle_quit(self) -> None:
        end_time = time.time()
        elapsed_seconds = end_time - self._start_time
        elapsed_minutes = elapsed_seconds / 60

        print("Saving progress... (not really, but maybe later)")
        print(f"You have been using this program for {elapsed_minutes:.1f} minutes.")
        print("Goodbye!")
