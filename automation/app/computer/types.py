from dataclasses import dataclass
from typing import Literal, Optional


LocatorStrategy = Literal[
    "label",
    "role",
    "text",
    "css",
]


@dataclass
class Target:
    strategy: LocatorStrategy
    value: str
    role: Optional[str] = None