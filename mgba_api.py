from abc import ABC, abstractmethod
from enum import Enum


class Key(Enum):
    A = 0
    B = 1
    SELECT = 2
    START = 3
    RIGHT = 4
    LEFT = 5
    UP = 6
    DOWN = 7
    R = 8
    L = 9

    def bitmask(self) -> int:
        return 1 << self.value

    def __str__(self) -> str:
        return self.name[0] + self.name[1:].lower()

    def reverse(self) -> "Key":
        match self:
            case Key.LEFT:
                return Key.RIGHT
            case Key.RIGHT:
                return Key.LEFT
            case Key.UP:
                return Key.DOWN
            case Key.DOWN:
                return Key.UP
            case _:
                return self


class MGBA_API(ABC):
    @abstractmethod
    def add_key(self, key: Key) -> None:
        pass

    @abstractmethod
    def clear_key(self, key: Key) -> None:
        pass

    @abstractmethod
    def tap(self, key: Key) -> None:
        pass
