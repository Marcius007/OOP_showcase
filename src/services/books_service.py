import datetime
from dataclasses import dataclass, field
from enum import Enum
from typing import ClassVar


class BookStatus(Enum):
    AVAILABLE = "Pasiekiama"
    UNAVAILABLE = "Paimta"


@dataclass(repr=False)
class Book:
    name: str
    author: str
    year: int
    status: BookStatus = field(default=BookStatus.AVAILABLE)
    return_date: ClassVar[datetime.datetime | None] = None

    @classmethod
    def set_return_date(cls, days):
        if days:
            cls.return_date = datetime.datetime.today() + datetime.timedelta(days=days)
        else:
            cls.return_date = None

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
