import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros

keyboard = KMKKeyboard()

macros = Macros()
keyboard.modules.append(macros)

# ORDEM DOS BOTÕES (ajusta só se quiseres mudar a função)
PINS = [
    board.D0,  # GPIO0 ⚠️
    board.D7,  # GPIO7
    board.D1,  # GPIO1 ⚠️
    board.D2,  # GPIO2
    board.D4,  # GPIO4
    board.D3,  # GPIO3
]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

keyboard.keymap = [
    [
        KC.A,
        KC.B,
        KC.C,
        KC.D,
        KC.E,
        KC.F,
    ]
]

if __name__ == '__main__':
    keyboard.go()
