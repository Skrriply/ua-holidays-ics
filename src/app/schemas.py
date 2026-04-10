from dataclasses import dataclass
from datetime import datetime

from icalendar import TRANSP


@dataclass(frozen=True, slots=True)
class Holiday:
    """A holiday event.

    Attributes:
        name: The name of the holiday.
        start_date: The beginning timestamp of the holiday event.
        end_date: The ending timestamp of the holiday event.
        transparency: iCalendar transparency setting. Defaults to `TRANSP.TRANSPARENT`.
    """

    name: str
    start_date: datetime
    end_date: datetime
    transparency: TRANSP | None = TRANSP.TRANSPARENT
