import time
import random
import sys
import usb_hid
from adafruit_hid.mouse import Mouse

m = Mouse(usb_hid.devices)

# Rust Console Profiles: (Vert, Horiz, Delay, Is_Pattern)
# M249: Pure vertical pull
# AK-47: Heavy 'S' curve
# MP5/Tommy: Fast vertical with slight horizontal sway
RUST_PROFILES = {
    "0": (0, 0, 0.01),
    "301": (6.5, 0.0, 0.008),   # M249 (Heavy Down)
    "302": (5.8, -1.4, 0.01),   # AK-47 (Down & Left correction)
    "303": (3.2, 0.4, 0.009),   # MP5 (Light & Fast)
    "304": (2.8, 0.2, 0.01)     # TOMMY (Steady)
}

active_mode = "0"

def rust_inject(v, h, s):
    # DYNAMIC JITTER: Essential for Rust Console anti-cheat
    # Creates a "fuzzy" movement pattern
    chaos_v = v + random.uniform(-0.4, 0.4)
    chaos_h = h + random.uniform(-0.3, 0.3)
    
    m.move(x=int(chaos_h), y=int(chaos_v))
    time.sleep(s)

while True:
    if sys.stdin.readable():
        line = sys.stdin.readline().strip()
        if line in RUST_PROFILES:
            active_mode = line

    v, h, s = RUST_PROFILES.get(active_mode, (0,0,0.01))
    if v > 0:
        rust_inject(v, h, s)