import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC

keyboard = KMKKeyboard()

PINS = [board.D10, board.D9, board.D8, board.D7]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

keyboard.keymap = [
    [
        KC.UP,
        KC.RIGHT,
        KC.LEFT,
        KC.DOWN,
    ]
]

if __name__ == "__main__":
    keyboard.go()