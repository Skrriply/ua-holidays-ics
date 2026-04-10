import re
from datetime import datetime, timedelta

from bs4 import BeautifulSoup

from app.parsers.base import BaseParser
from app.schemas import Holiday


class HolidaysParser(BaseParser):
    """Парсер для структури сайту zakon.rada.gov.ua"""

    URL: str = "https://zakon.rada.gov.ua/laws/main/days/sps"
    HEADERS: dict[str, str] = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:147.0) Gecko/20100101 Firefox/147.0"
    }

    @staticmethod
    def _clean_holiday_name(raw_title: str) -> str:
        inner_soup = BeautifulSoup(raw_title, "lxml")

        for circle in inner_soup.find_all(class_="iday"):
            circle.decompose()

        return inner_soup.get_text(separator=" ").strip()

    def parse(self) -> list[Holiday]:
        html = self._fetch_html(self.URL, headers=self.HEADERS, timeout=30)
        soup = BeautifulSoup(html, "lxml")

        day_elements = soup.find_all("td", class_=re.compile(r"^holiday"))
        holidays: list[Holiday] = []

        for el in day_elements:
            title_raw = el.get("title")
            date_span = el.find("span", attrs={"data-cal": True})
            date_raw = date_span.get("data-cal") if date_span else None

            if not title_raw or not date_raw:
                continue

            clean_name = self._clean_holiday_name(str(title_raw))
            start_date = datetime.strptime(str(date_raw), "%Y%m%d")
            end_date = start_date + timedelta(days=1)

            if not clean_name:
                continue

            holidays.append(Holiday(clean_name, start_date, end_date))

        return holidays
