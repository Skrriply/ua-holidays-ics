from datetime import timedelta
from pathlib import Path

import httpx

from app.ics import CalendarService
from app.parsers.parser import HolidaysParser


def main() -> None:
    """Main entry point for the application."""
    ROOT_PATH: Path = Path(__file__).parent.parent.parent
    OUTPUT_PATH: Path = ROOT_PATH / "calendar.ics"
    SOURCE_URL: str = "https://raw.githubusercontent.com/Skrriply/ua-holidays-ics/refs/heads/main/calendar.ics"

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
        source=SOURCE_URL,
        refresh_interval=timedelta(days=30),
    )


if __name__ == "__main__":
    main()
