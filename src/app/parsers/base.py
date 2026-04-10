from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Any

import httpx

if TYPE_CHECKING:
    from app.schemas import Holiday


class BaseParser(ABC):
    def __init__(self, http: httpx.Client) -> None:
        self.http: httpx.Client = http

    def _fetch_html(self, url: str, **kwargs: Any) -> str:
        response = self.http.get(url, **kwargs)
        response.raise_for_status()
        return response.text

    @abstractmethod
    def parse(self) -> list[Holiday]:
        pass
