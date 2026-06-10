import board, digitalio, usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

kbd = Keyboard(usb_hid.devices)

# Pin → Key mapping
pins = [board.D8, board.D9, board.D10, board.D7]
keys = [Keycode.W, Keycode.A, Keycode.S, Keycode.D]

# Configure switches
switches = []
for p in pins:
    sw = digitalio.DigitalInOut(p)
    sw.direction = digitalio.Direction.INPUT
    sw.pull = digitalio.Pull.UP
    switches.append(sw)

while True:
    for sw, key in zip(switches, keys):
        if not sw.value:   # pressed (pin pulled low)
            kbd.press(key)
        else:
            kbd.release(key)
