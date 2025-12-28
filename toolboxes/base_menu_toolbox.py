# base_menu_toolbox.py

from __future__ import  annotations

from collections.abc import Callable, Mapping
from ..system_commands import SystemCommand
from ..ui import handle_user_input, warning

Action = Callable [[], SystemCommand | None]
Actions = Mapping [str, tuple[str, Action]]

class BaseMenuToolbox:
    """Reusable submenu loop for toolboxes with numbered actions."""

    def __init__(self, title: str, actions: Actions) -> None:
        self._title = title
        self._actions: dict[str, tuple[str, Action]] = dict(actions)

    def run(self) -> SystemCommand | None:
        while True:
            self._print_menu()
            choice = handle_user_input(
                "Choose an option: ",
                list(self._actions.keys()),
                allow_back=True,
            )

            if choice is SystemCommand.QUIT:
                return SystemCommand.QUIT
            if choice is SystemCommand.BACK:
                return SystemCommand.BACK

            if isinstance(choice, SystemCommand):
                warning("Internal error: unexpected command.")
                continue

            _label, func = self._actions[choice]
            result = func()

            if result is not None:
                return result

    def _print_menu(self) -> None:
        print(f"\n=== {self._title} Menu ===")
        for key, (label, _func) in self._actions.items():
            print(f"{key}. {label}")
        print("b. Back")
        print("q. Quit")