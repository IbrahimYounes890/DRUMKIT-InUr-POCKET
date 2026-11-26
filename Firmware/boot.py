# The ESP32-S3 has USB MIDI turned off by default, and there aren't enough
# USB endpoints for everything at once. Give up the serial console to get MIDI.
# (The CIRCUITPY drive and HID volume keys still work.)
import usb_cdc
import usb_midi

usb_cdc.disable()
usb_midi.enable()
