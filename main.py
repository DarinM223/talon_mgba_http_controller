from controller import GameController
from http_api import HTTP_API
import logging
from pynput import mouse, keyboard
from pynput.keyboard import Key, KeyCode

logger = logging.getLogger(__name__)
controller = GameController(HTTP_API("http://localhost:5000"))

key_mapping = {
    Key.left: GameController.press_left,
    Key.right: GameController.press_right,
    Key.up: GameController.press_up,
    Key.down: GameController.press_down,
    Key.enter: GameController.press_start,
    Key.backspace: GameController.press_select,
    Key.esc: GameController.reset,
    "a": GameController.press_a,
    "b": GameController.press_b,
    "l": GameController.press_l,
    "r": GameController.press_r,
    "A": GameController.hold_a,
    "B": GameController.hold_b,
    "L": GameController.hold_l,
    "R": GameController.hold_r,
}


def on_press(key: Key | KeyCode | None) -> None:
    map_key = key.char if isinstance(key, KeyCode) else key
    if map_key in key_mapping:
        logger.debug(f"Pressed {map_key}")
        key_mapping[map_key](controller)


def on_scroll(_x: int, _y: int, _dx: int, dy: int) -> bool | None:
    if dy < 0:
        logger.debug(f"Scrolled down {dy}")
        controller.scroll_down()
    else:
        logger.debug(f"Scrolled up {dy}")
        controller.scroll_up()


def main():
    logging.basicConfig(level=logging.INFO)
    print("talon-mgba-http-controller started...")
    print("Listening to a/b/l/r/enter/backspace/escape/arrow keys...")
    with (
        mouse.Listener(on_scroll=on_scroll) as mouse_listener,
        keyboard.Listener(on_press=on_press) as keyboard_listener,
    ):
        try:
            mouse_listener.join()
            keyboard_listener.join()
        except KeyboardInterrupt:
            pass


if __name__ == "__main__":
    main()
