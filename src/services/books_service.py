import datetime
from dataclasses import dataclass, field, InitVar
from enum import Enum


class BookStatus(Enum):
    AVAILABLE = "Pasiekiama"
    UNAVAILABLE = "Paimta"


@dataclass(eq=False)
class Book:
    name: str
    author: str
    year: int
    status: BookStatus = field(default=BookStatus.AVAILABLE)
    return_date: datetime = field(default=None)

    def is_available(self) -> bool:
        return self.status == BookStatus.AVAILABLE

    def is_unavailable(self) -> bool:
        return self.status == BookStatus.UNAVAILABLE

    def set_unavailable(self) -> None:
        self.status = BookStatus.UNAVAILABLE

    def set_available(self) -> None:
        self.status = BookStatus.AVAILABLE

    def __repr__(self) -> str:
        return f"({self.name}: {self.year} - {self.status.value} {self.return_date})"

    def __eq__(self, other):
        return self.name == other.name and self.status == other.status and self.year == other.year and self.author == other.author