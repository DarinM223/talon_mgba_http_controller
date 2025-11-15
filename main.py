from controller import GameController
from http_api import HTTP_API
import logging
from pynput import mouse, keyboard
from pynput.keyboard import Key, KeyCode

logger = logging.getLogger(__name__)
controller = GameController(HTTP_API("http://localhost:5000"))


def on_press(key: Key | KeyCode | None) -> None:
    match key:
        case Key.left:
            logger.debug("Pressed left")
            controller.press_left()
        case Key.right:
            logger.debug("Pressed right")
            controller.press_right()
        case Key.up:
            logger.debug("Pressed up")
            controller.press_up()
        case Key.down:
            logger.debug("Pressed down")
            controller.press_down()
        case Key.enter:
            logger.debug("Pressed start")
            controller.press_start()
        case Key.backspace:
            logger.debug("Pressed select")
            controller.press_select()
        case KeyCode() if key.char == "a":
            logger.debug("Pressed A")
            controller.press_a()
        case KeyCode() if key.char == "A":
            logger.debug("Holding A")
            controller.hold_a()
        case KeyCode() if key.char == "b":
            logger.debug("Pressed B")
            controller.press_b()
        case KeyCode() if key.char == "B":
            logger.debug("Holding B")
            controller.hold_b()
        case KeyCode() if key.char == "l":
            logger.debug("Pressed L")
            controller.press_l()
        case KeyCode() if key.char == "L":
            logger.debug("Holding L")
            controller.hold_l()
        case KeyCode() if key.char == "r":
            logger.debug("Pressed R")
            controller.press_r()
        case KeyCode() if key.char == "R":
            logger.debug("Holding R")
            controller.hold_r()
        case Key.esc:
            logger.debug("Pressed escape")
            controller.reset()
        case _:
            pass


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
