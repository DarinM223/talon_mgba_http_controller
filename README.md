Talon mGBA Controller
=====================

Voice input controls for Game Boy Advance games running on the mGBA emulator using Talon Voice.

![Running through Pokemon Fire Red using voice input](demo.gif)

Holding down direction keys on a controller is simulated with scrolling,
which in Talon can be activated through hissing.
Scrolling down will continually press the arrow key in the direction last specified and scrolling up will
press the opposite direction key. This prevents voice strain by only requiring spoken voice input for
changing directions.

The rest of the keys are shown in this table:

| Key press | Button pressed on GBA    |
|-----------|--------------------------|
|   Enter   |       Start              |
| Backspace |       Select             |
|    a      |   A (single press)       |
|    b      |   B (single press)       |
|    l      |   L (single press)       |
|    r      |   R (single press)       |
|    A      |   A (hold down)          |
|    B      |   B (hold down)          |
|    L      |   L (hold down)          |
|    R      |   R (hold down)          |
|  Escape   | Stop holding all buttons |

The escape key resets all held buttons on the controller in case of a bug where a key is being held down forever. If
a key is being held down, pressing the key again stops the key being held down.

Installing
----------

Install the `uv` package manager, then clone the repository and run `uv sync`.

Running
-------

* Install and run [mGBA](https://github.com/mgba-emu/mgba) and [mGBA-http](https://github.com/nikouu/mGBA-http) (0.8.0)
* Load mGBA with the `mGBASocketServer.lua` script from mGBA-http by going into Tools->Scripting in
mGBA and then File->Load Script... and selecting `mGBASocketServer.lua`.
* Run `uv run main.py` inside the project directory.