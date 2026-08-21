from abc import ABC, abstractmethod

from computer.types import Target


class ComputerSurface(ABC):

    @abstractmethod
    def navigate(self, url: str) -> None:
        pass

    @abstractmethod
    def click(self, target: Target) -> None:
        pass

    @abstractmethod
    def type(self, target: Target, value: str) -> None:
        pass

    @abstractmethod
    def read(self, target: Target) -> str:
        pass

    @abstractmethod
    def observe(self) -> str:
        pass

    @abstractmethod
    def screenshot(self, path: str) -> None:
        pass

    @abstractmethod
    def is_visible(self, target: Target) -> bool:
        pass