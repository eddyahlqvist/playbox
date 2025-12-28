# counters.py

from ..system_commands import SystemCommand
from ..ui import info
from .base_menu_toolbox import BaseMenuToolbox

class CountersToolbox(BaseMenuToolbox):
    def __init__(self) -> None:
        super().__init__(
            "Counters",
            {
                "1": ("Placeholder 1", self._placeholder_1),
                "2": ("Placeholder 2", self._placeholder_2),
                "3": ("Placeholder 3", self._placeholder_3),
            },
        )

    def _placeholder_1(self) -> SystemCommand | None:
        info("Placeholder 1 (not yet implemented)")
        return None

    def _placeholder_2(self) -> SystemCommand | None:
        info("Placeholder 2 (not yet implemented)")
        return None

    def _placeholder_3(self) -> SystemCommand | None:
        info("Placeholder 3 (not yet implemented)")
        return None