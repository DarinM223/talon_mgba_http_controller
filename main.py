from pynput import mouse, keyboard
from pynput.keyboard import Key


def on_press(key, injected):
    match key:
        case Key.left:
            print("Pressed left")
        case Key.right:
            print("Pressed right")
        case Key.up:
            print("Pressed up")
        case Key.down:
            print("Pressed down")


def on_scroll(x, y, dx, dy, injected):
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
        except:
            pass


if __name__ == "__main__":
    main()
