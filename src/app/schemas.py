from dataclasses import dataclass
from datetime import datetime

from icalendar import TRANSP


@dataclass(frozen=True, slots=True)
class Holiday:
    name: str
    date: datetime
    transparency: TRANSP | None = TRANSP.TRANSPARENT
