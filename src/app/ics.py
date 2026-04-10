from __future__ import annotations

from datetime import datetime, timedelta
from typing import TYPE_CHECKING

from icalendar import Calendar, Event

if TYPE_CHECKING:
    from pathlib import Path

    from app.schemas import Holiday


class CalendarService:
    @staticmethod
    def generate(
        output_path: Path,
        holidays: list[Holiday],
        name: str | None = None,
        description: str | None = None,
        language: str | None = None,
        source: str | None = None,
        refresh_interval: timedelta | None = None,
    ):
        cal = Calendar.new(
            name=name,
            description=description,
            language=language,
            source=source,
            refresh_interval=refresh_interval,
            last_modified=datetime.now(),
        )

        for holiday in holidays:
            event = Event.new(
                summary=holiday.name,
                start=holiday.date,
                end=holiday.date,
                transparency=holiday.transparency,
            )
            cal.add_component(event)

        with open(output_path, "wb") as cal_file:
            cal_file.write(cal.to_ical())
