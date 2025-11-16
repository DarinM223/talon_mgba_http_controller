from mgba_api import MGBA_API, Key, BITMASK_DIRECTIONS, BITMASK_ALL_KEYS
import logging
import threading
import time

logger = logging.getLogger(__name__)


class GameController:
    SCROLL_TIMEOUT = 0.15

    lock: threading.Lock
    api: MGBA_API
    direction: Key | None
    holding: set[Key]
    timeout: float | None
    thread: threading.Thread

    def __init__(self, api: MGBA_API) -> None:
        self.lock = threading.Lock()
        self.api = api
        self.direction = None
        self.holding = set()
        self.timeout = None

        def poll_time():
            while True:
                with self.lock:
                    t = time.time()
                    if self.timeout and t > self.timeout:
                        logger.debug("Clearing scrolling")
                        self.timeout = None
                        self.api.clear_keys(bitmask=BITMASK_DIRECTIONS)

        self.thread = threading.Thread(target=poll_time)
        self.thread.start()

    def _tap_direction(self, direction: Key) -> None:
        with self.lock:
            self.timeout = None
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

    def _unhold_key(self, key: Key) -> bool:
        if key in self.holding:
            self.holding.remove(key)
            self.api.clear_key(key)
            return True
        return False

    def _hold_key(self, key: Key) -> None:
        if not self._unhold_key(key):
            self.holding.add(key)
            self.api.add_key(key)

    def press_a(self) -> None:
        self._unhold_key(Key.A)
        self.api.tap(Key.A)

    def hold_a(self) -> None:
        self._hold_key(Key.A)

    def press_b(self) -> None:
        self._unhold_key(Key.B)
        self.api.tap(Key.B)

    def hold_b(self) -> None:
        self._hold_key(Key.B)

    def press_l(self) -> None:
        self._unhold_key(Key.L)
        self.api.tap(Key.L)

    def hold_l(self) -> None:
        self._hold_key(Key.L)

    def press_r(self) -> None:
        self._unhold_key(Key.R)
        self.api.tap(Key.R)

    def hold_r(self) -> None:
        self._hold_key(Key.R)

    def _scroll_direction(self, direction: Key) -> None:
        if not self.timeout:
            self.api.add_key(direction)
        self.timeout = time.time() + GameController.SCROLL_TIMEOUT

    def scroll_up(self) -> None:
        with self.lock:
            if self.direction:
                self._scroll_direction(self.direction.reverse())

    def scroll_down(self) -> None:
        with self.lock:
            if self.direction:
                self._scroll_direction(self.direction)

    def reset(self) -> None:
        with self.lock:
            self.direction = None
            self.holding.clear()
            self.timeout = None
            self.api.clear_keys(bitmask=BITMASK_ALL_KEYS)
