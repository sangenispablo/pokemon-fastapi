from dataclasses import dataclass


@dataclass
class Pokemon:
    number: int
    name: str
    id: int | None = None
