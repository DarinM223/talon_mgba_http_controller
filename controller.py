from mgba_api import MGBA_API, Key
import threading


class GameController:
    lock: threading.Lock
    api: MGBA_API
    direction: Key | None

    def __init__(self, api: MGBA_API) -> None:
        self.lock = threading.Lock()
        self.api = api
        self.direction = None

    def _tap_direction(self, direction: Key) -> None:
        with self.lock:
            self.direction = direction
            self.api.tap(self.direction)

    def press_left(self) -> None:
        self._tap_direction(Key.LEFT)

    def press_right(self) -> None:
        self._tap_direction(Key.RIGHT)

    def press_up(self) -> None:
        self._tap_direction(Key.UP)

    def press_down(self) -> None:
        self._tap_direction(Key.DOWN)

    def press_start(self) -> None:
        self.api.tap(Key.START)

    def press_select(self) -> None:
        self.api.tap(Key.SELECT)
