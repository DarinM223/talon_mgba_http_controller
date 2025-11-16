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
        return _reverse_keys[self] if self in _reverse_keys else self


_reverse_keys = {
    Key.LEFT: Key.RIGHT,
    Key.RIGHT: Key.LEFT,
    Key.UP: Key.DOWN,
    Key.DOWN: Key.UP,
}
BITMASK_DIRECTIONS = (
    Key.RIGHT.bitmask() | Key.LEFT.bitmask() | Key.UP.bitmask() | Key.DOWN.bitmask()
)
BITMASK_ALL_KEYS = (
    Key.A.bitmask()
    | Key.B.bitmask()
    | Key.SELECT.bitmask()
    | Key.START.bitmask()
    | Key.L.bitmask()
    | Key.R.bitmask()
    | BITMASK_DIRECTIONS
)


class MGBA_API(ABC):
    """Functions for controlling mGBA with input keys."""

    @abstractmethod
    def add_key(self, key: Key) -> None:
        """Adds a key to be held down."""
        pass

    @abstractmethod
    def add_keys(self, bitmask: int) -> None:
        """
        Adds a bitmask of multiple keys to be held down.
        Multiple keys are combined with the bitwise or of their bitmasks.
        """
        pass

    @abstractmethod
    def clear_key(self, key: Key) -> None:
        """Releases a held down key."""
        pass

    @abstractmethod
    def clear_keys(self, bitmask: int) -> None:
        """
        Adds a bitmask of multiple keys to be released.
        Multiple keys are combined with the bitwise or of their bitmasks.
        """
        pass

    @abstractmethod
    def tap(self, key: Key) -> None:
        """A cycle of holding down and releasing a key."""
        pass
