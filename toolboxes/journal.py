# journal.py

from ..system_commands import SystemCommand
from ..ui import info
from .base_menu_toolbox import BaseMenuToolbox

class JournalToolbox(BaseMenuToolbox):
    def __init__(self) -> None:
        super().__init__(
            "Journal",
            {
                "1": ("New entry", self._new_entry),
                "2": ("List entries", self._list_entries),
                "3": ("Search", self._search),
            },
        )

    def _new_entry(self) -> SystemCommand | None:
        info("New entry (not yet implemented)")
        return None

    def _list_entries(self) -> SystemCommand | None:
        info("List entries (not yet implemented)")
        return None

    def _search(self) -> SystemCommand | None:
        info("Search (not yet implemented)")
        return None
