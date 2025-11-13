from pynput import mouse, keyboard
from pynput.keyboard import Key, KeyCode
import threading

lock = threading.Lock()


def on_press(key: Key | KeyCode | None) -> None:
    match key:
        case Key.left:
            print("Pressed left")
        case Key.right:
            print("Pressed right")
        case Key.up:
            print("Pressed up")
        case Key.down:
            print("Pressed down")
        case Key.enter:
            print("Pressed start")
        case Key.backspace:
            print("Pressed select")
        case KeyCode() if key.char == "a":
            print("Pressed A")
        case KeyCode() if key.char == "A":
            print("Holding A")
        case KeyCode() if key.char == "b":
            print("Pressed B")
        case KeyCode() if key.char == "B":
            print("Holding B")
        case KeyCode() if key.char == "l":
            print("Pressed L")
        case KeyCode() if key.char == "L":
            print("Holding L")
        case KeyCode() if key.char == "r":
            print("Pressed R")
        case KeyCode() if key.char == "R":
            print("Holding R")
        case _:
            pass


def on_scroll(_x: int, _y: int, dx: int, dy: int) -> bool | None:
    if dy < 0:
        print(f"Scrolled down {dy}")
    else:
        print(f"Scrolled up {dy}")


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
