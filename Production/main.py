import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.rgb import RGB, AnimationModes

# Initialize the keyboard base engine
keyboard = KMKKeyboard()

# Configure your 4x4 matrix pin paths exactly to match your KiCad schematic
keyboard.col_pins = (board.D0, board.D1, board.D2, board.D3)
keyboard.row_pins = (board.D7, board.D8, board.D9, board.D10)

# Set your diode scanning direction (pointing from switches down to columns)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# Initialize the anti-ghosting volume wheel handler module
encoders = EncoderHandler()
keyboard.modules.append(encoders)

# Map your rotary encoder pin highways (Pin A, Pin B)
# Assumes DI goes to D6 and the other encoder pin goes to D5
encoders.pins = (
    (board.D6, board.D5, None, False), # (Pin A, Pin B, Click Pin, Is Inverted)
)

# Define your custom key bindings layout map (Layer 0)
keyboard.keymap = [
    [
        KC.N7, KC.N8, KC.N9, KC.MINUS,
        KC.N4, KC.N5, KC.N6, KC.PLUS,
        KC.N1, KC.N2, KC.N3, KC.SLASH,
        KC.N0, KC.DOT, KC.ENT, KC.SPC,
    ]
]

# Map your rotary encoder spinning actions to system media audio channels
encoders.map = [
    ( (KC.VOLU, KC.VOLD), ) # (Spin Clockwise = Vol Up, Spin Counter-Clockwise = Vol Down)
]

rgb = RGB(
    pixel_pin=board.D4,        # <-- Update this to the exact pin you wired to the RGB data line in KiCad!
    num_pixels=8,             # <-- Change this to the exact number of LEDs on your physical strip segment
    val_limit=150,            # Max brightness pad safety limiter (Saves battery/power load from the USB port)
    animation_mode=AnimationModes.RAINBOW, # Boots up with the classic gamer rainbow wave cycle effect
)
keyboard.extensions.append(rgb)

keyboard.extensions.append(rgb)

if __name__ == '__main__':
    keyboard.go()
