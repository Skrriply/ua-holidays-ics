from datetime import timedelta
from pathlib import Path

import httpx

from app.ics import CalendarService
from app.parsers.parser import HolidaysParser


def main() -> None:
    ROOT_PATH = Path(__file__).parent.parent.parent
    OUTPUT_PATH = ROOT_PATH / "calendar.ics"

    http = httpx.Client()
    parser = HolidaysParser(http)
    cal_service = CalendarService()

    holidays = parser.parse()
    cal_service.generate(
        OUTPUT_PATH,
        holidays,
        name="Свята в Україні",
        description="Календар офіційних свят в Україні",
        language="UK",
        source="https://raw.githubusercontent.com/Skrriply/ua-holidays-ics/refs/heads/main/calendar.ics",
        refresh_interval=timedelta(days=30),
    )


if __name__ == "__main__":
    main()
