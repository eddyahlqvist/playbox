# journal.py

from datetime import datetime

from ..system_commands import SystemCommand
from ..ui import info, warning
from ..storage import data_dir, load_json, save_json
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
        title = input("Title (optional): ").strip()
        body = input("Body: ").strip()

        if not body:
            info("Entry not saved (body was empty).")
            return None

        now = datetime.now().astimezone()
        created_at = now.isoformat(timespec="seconds")

        if not title:
            title = f"Entry {now.strftime('%Y-%m-%d %H:%M')}"

        entry = {
            "id": created_at,
            "created_at": created_at,
            "title": title,
            "body": body,
            "tags": [],
            "updated_at": None,
        }

        path = data_dir() / "journal.json"

        try:
            journal = load_json(path, default={"version": 1, "entries": []})
        except ValueError:
            warning("Journal data was corrupted. Starting with a new journal.")
            journal = {"version": 1, "entries": []}

        journal["entries"].append(entry)

        save_json(path, journal)
        info("Entry saved.")
        return None

    def _list_entries(self) -> SystemCommand | None:
        info("List entries (not yet implemented)")
        return None

    def _search(self) -> SystemCommand | None:
        info("Search (not yet implemented)")
        return None
