# Vibe coding some firmware because python is boring 🤑
# Board: Waveshare ESP32-S3-Zero
import keypad
import touchio
from adafruit_midi.control_change import ControlChange
from microcontroller import pin

from kmk.extensions.media_keys import MediaKeys
from kmk.extensions.rgb import RGB, AnimationModes
from kmk.keys import KC, Key
from kmk.kmk_keyboard import KMKKeyboard
from kmk.modules.encoder import EncoderHandler
from kmk.modules.midi import MidiKeys
from kmk.scanners import Scanner
from kmk.scanners.keypad import KeysScanner


# KMK doesn't have a scanner for touch pads, so here's a tiny one.
# Don't touch the pads while the board boots - they calibrate on startup!
class TouchScanner(Scanner):
    def __init__(self, pins):
        self.pads = [touchio.TouchIn(p) for p in pins]
        self.pressed = [False] * len(pins)

    @property
    def key_count(self):
        return len(self.pads)

    def scan_for_changes(self):
        for i, pad in enumerate(self.pads):
            touched = pad.value
            if touched != self.pressed[i]:
                self.pressed[i] = touched
                return keypad.Event(i + self.offset, touched)


keyboard = KMKKeyboard()
# These have to be created before we use KC.MIDI_NOTE / KC.VOLU below
midi = MidiKeys()
media_keys = MediaKeys()

keyboard.matrix = [
    # TOUCH1-TOUCH7 on J1 (keys 0-6)
    TouchScanner([pin.GPIO7, pin.GPIO8, pin.GPIO9, pin.GPIO10, pin.GPIO11, pin.GPIO12, pin.GPIO13]),
    # SW1, SW2, SW3 (keys 7-9), each switches to GND
    KeysScanner([pin.GPIO5, pin.GPIO4, pin.GPIO3], value_when_pressed=False, pull=True),
]

# Touch pads play a C major scale, switches play drum sounds
keyboard.keymap = [[
    KC.MIDI_NOTE(60), KC.MIDI_NOTE(62), KC.MIDI_NOTE(64), KC.MIDI_NOTE(65),
    KC.MIDI_NOTE(67), KC.MIDI_NOTE(69), KC.MIDI_NOTE(71),
    KC.MIDI_NOTE(36), KC.MIDI_NOTE(38), KC.MIDI_NOTE(42),  # kick, snare, hi-hat
]]

# Second encoder acts as a mod wheel (MIDI CC 1)
MOD_STEP = 8  # how much each click changes the value (0-127)
mod_value = 0


def change_mod(amount):
    global mod_value
    mod_value = max(0, min(127, mod_value + amount))
    midi.send(ControlChange(1, mod_value))


MOD_DOWN = Key(on_press=lambda *args: change_mod(-MOD_STEP))
MOD_UP = Key(on_press=lambda *args: change_mod(MOD_STEP))

# Encoders: (A, B, button). The push switches aren't wired, so button = None
encoder = EncoderHandler()
encoder.pins = (
    (pin.GPIO44, pin.GPIO43, None),  # SW4: A = RX, B = TX
    (pin.GPIO2, pin.GPIO1, None),    # SW5: A = GP2, B = GP1
)
encoder.map = [(
    (KC.VOLD, KC.VOLU, KC.NO),  # SW4: computer volume
    (MOD_DOWN, MOD_UP, KC.NO),  # SW5: mod wheel
)]

keyboard.modules = [midi, encoder]
keyboard.extensions = [
    media_keys,
    # D1-D3, data on GP6
    RGB(pixel_pin=pin.GPIO6, num_pixels=3, val_default=80, animation_mode=AnimationModes.RAINBOW),
]

if __name__ == '__main__':
    keyboard.go()
