import time
import random
import sys
import usb_hid
from adafruit_hid.mouse import Mouse

m = Mouse(usb_hid.devices)

# Warzone Meta Profiles: (Vertical, Horizontal, Sleep, RapidFire)
WZ_PROFILES = {
    "0": (0.0, 0.0, 0.01, False),
    "201": (3.2, 0.1, 0.007, False),  # MCW
    "202": (4.5, -0.3, 0.006, False), # SVA-545
    "203": (3.8, 0.4, 0.005, False),  # HRM-9
    "204": (2.9, 0.0, 0.008, False),  # WSP-9
    "205": (5.2, -0.2, 0.01, False),  # PULEMYOT
    "206": (4.0, 0.2, 0.02, True),    # MTZ-762 (Rapid)
    "207": (3.5, 0.0, 0.015, True)    # INTERCEPTOR (Rapid)
}

active_id = "0"

def execute_wz_move(v, h, s, rf):
    # Warzone Evasion: Higher jitter to counter Ricochet heuristics
    jv = v * random.uniform(0.88, 1.12)
    jh = h * random.uniform(0.88, 1.12)
    
    if rf:
        m.click(Mouse.LEFT_BUTTON)
        time.sleep(0.01)
    
    m.move(x=int(jh), y=int(jv))
    time.sleep(s)

while True:
    if sys.stdin.readable():
        line = sys.stdin.readline().strip()
        if line in WZ_PROFILES:
            active_id = line

    v, h, s, rf = WZ_PROFILES.get(active_id, (0,0,0.01, False))
    if v > 0:
        execute_wz_move(v, h, s, rf)