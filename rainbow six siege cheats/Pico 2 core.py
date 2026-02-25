import time
import random
import sys

# (Vertical Pull, Horizontal Pull, Speed)
# Positive Vertical = Pulls stick DOWN
# Positive Horizontal = Pulls stick LEFT
RECOIL_DATA = {
    "0": (0.0, 0.0, 0.01),    # OFF
    "1": (3.4, 0.1, 0.01),    # R4C: Heavy down, tiny right drift
    "2": (1.8, 0.0, 0.01),    # MP5: Low vertical, very steady
    "3": (5.5, 0.2, 0.008),   # SMG11: Extreme vertical, very fast fire
    "4": (6.0, -0.6, 0.008),  # SMG12: Max vertical, pulls right (needs left)
    "5": (4.2, 0.4, 0.006),   # Vector: Fast vertical, slight right kick
    "6": (4.8, 0.0, 0.01),    # F2: Very high vertical
    "7": (3.0, -0.2, 0.015)   # G8A1: Heavy LMG pull
}

current_gun = "0"

def apply_recoil(v, h, s):
    # MouseTrap Evasion: Add 5% random human jitter
    jitter_v = v * random.uniform(0.95, 1.05)
    jitter_h = h * random.uniform(0.95, 1.05)
    
    # This sends the hardware command to the Xbox
    send_joy_move(jitter_h, jitter_v)
    time.sleep(s)

while True:
    # Check if Laptop/Pi Zero sent a new gun command
    if sys.stdin.any():
        current_gun = sys.stdin.readline().strip()

    if is_firing():
        v, h, s = RECOIL_DATA.get(current_gun, (0,0,0.01))
        if v > 0:
            apply_recoil(v, h, s)