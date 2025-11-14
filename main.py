from controller import GameController
from http_api import HTTP_API
from pynput import mouse, keyboard
from pynput.keyboard import Key, KeyCode

controller = GameController(HTTP_API("http://localhost:5000"))


def on_press(key: Key | KeyCode | None) -> None:
    match key:
        case Key.left:
            print("Pressed left")
            controller.press_left()
        case Key.right:
            print("Pressed right")
            controller.press_right()
        case Key.up:
            print("Pressed up")
            controller.press_up()
        case Key.down:
            print("Pressed down")
            controller.press_down()
        case Key.enter:
            print("Pressed start")
            controller.press_start()
        case Key.backspace:
            print("Pressed select")
            controller.press_select()
        case KeyCode() if key.char == "a":
            print("Pressed A")
            controller.press_a()
        case KeyCode() if key.char == "A":
            print("Holding A")
            controller.hold_a()
        case KeyCode() if key.char == "b":
            print("Pressed B")
            controller.press_b()
        case KeyCode() if key.char == "B":
            print("Holding B")
            controller.hold_b()
        case KeyCode() if key.char == "l":
            print("Pressed L")
            controller.press_l()
        case KeyCode() if key.char == "L":
            print("Holding L")
            controller.hold_l()
        case KeyCode() if key.char == "r":
            print("Pressed R")
            controller.press_r()
        case KeyCode() if key.char == "R":
            print("Holding R")
            controller.hold_r()
        case Key.esc:
            print("Pressed escape")
            controller.reset()
        case _:
            pass


def on_scroll(_x: int, _y: int, _dx: int, dy: int) -> bool | None:
    if dy < 0:
        print(f"Scrolled down {dy}")
        controller.scroll_down()
    else:
        print(f"Scrolled up {dy}")
        controller.scroll_up()


def main():
    print("Hello from talon-mgba-http-controller!")
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
