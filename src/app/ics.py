from __future__ import annotations

from datetime import datetime, timedelta
from typing import TYPE_CHECKING

from icalendar import Calendar, Event

if TYPE_CHECKING:
    from pathlib import Path

    from app.schemas import Holiday


class CalendarService:
    """Class for generating iCalendar (`.ics`) files."""

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
        """Generates an iCalendar file and saves it to the specified path.

        Args:
            output_path: The file path where the `.ics` file will be saved.
            holidays: A list of `Holiday` objects to be converted.
            name: The display name of the calendar.
            description: A brief summary of the calendar.
            language: The language code (e.g., 'EN') for the calendar content.
            source: A URL pointing to the source of the calendar data.
            refresh_interval: How often the calendar client should check for updates.

        Raises:
            OSError: If there is an issue writing the file.
        """
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
                start=holiday.start_date,
                end=holiday.end_date,
                transparency=holiday.transparency,
            )
            cal.add_component(event)

        with open(output_path, "wb") as cal_file:
            cal_file.write(cal.to_ical())
