import serial
import time

# SETTINGS
# /dev/ttyACM0 is usually the Pico 2 when plugged into the Pi Zero
try:
    pico = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
    print("[SUCCESS] PICO 2 CONNECTED")
except:
    print("[ERROR] PICO 2 NOT FOUND")

# RUST WEAPON NAMES FOR THE HUD
rust_names = {
    "301": "M249 - LASER",
    "302": "AK47 - PATTERN",
    "303": "MP5 - FAST",
    "304": "TOMMY - STEADY",
    "0": "SAFE MODE"
}

def forward_command(cmd):
    if pico.is_open:
        pico.write(f"{cmd}\n".encode())
        print(f"[BRIDGE] SENT TO PICO: {cmd}")
        # Here is where you'd trigger your HUD update function
        # update_ili9488(rust_names.get(cmd, "UNKNOWN"))

# Main loop listening for Laptop commands
while True:
    # Example: Listen for input from the Laptop Serial/USB
    # Replace 'input()' with a serial read if using the Laptop GUI
    user_input = input("ENTER RUST CMD: ") 
    forward_command(user_input)
