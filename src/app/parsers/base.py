from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Any

import httpx

if TYPE_CHECKING:
    from app.schemas import Holiday


class BaseParser(ABC):
    """Base class for parsers."""

    def __init__(self, http: httpx.Client) -> None:
        """Initializes the class.

        Args:
            http: The `httpx.Client` instance.
        """
        self.http: httpx.Client = http

    def _fetch_html(self, url: str, **kwargs: Any) -> str:
        """Fetches the HTML content from a specified URL.

        Args:
            url: The target URL to fetch content from.
            **kwargs: Additional arguments passed to the request.

        Returns:
            The HTML content of the page as a string.

        Raises:
            httpx.HTTPStatusError: If the request returned an unsuccessful status code.
        """
        response = self.http.get(url, **kwargs)
        response.raise_for_status()
        return response.text

    @abstractmethod
    def parse(self) -> list[Holiday]:
        """Parses the fetched content into a list of `Holiday` objects.

        Returns:
            A list of `Holiday` objects.
        """
        pass
