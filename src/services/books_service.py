from dataclasses import dataclass, field
from enum import Enum


class BookStatus(Enum):
    AVAILABLE = "Pasiekiama"
    UNAVAILABLE = "Paimta"


@dataclass
class Book:
    name: str
    author: str
    year: int
    status: BookStatus = field(default=BookStatus.AVAILABLE)

    def is_available(self) -> bool:
        return self.status == BookStatus.AVAILABLE

    def is_unavailable(self) -> bool:
        return self.status == BookStatus.UNAVAILABLE

    def set_unavailable(self) -> None:
        self.status = BookStatus.UNAVAILABLE

    def set_available(self) -> None:
        self.status = BookStatus.AVAILABLE

    def __repr__(self) -> str:
        return f"({self.name}: {self.year} - {self.status.value})"
