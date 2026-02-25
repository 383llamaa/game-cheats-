import serial
from PIL import Image, ImageDraw, ImageFont

# Dictionary to match IDs to clear names for the LCD
id_map = {
    "201": "MCW - LOW RECOIL",
    "202": "SVA - BURST",
    "203": "HRM-9 - SPEED",
    "204": "WSP-9 - STEADY",
    "205": "LMG - HEAVY",
    "206": "MTZ - RAPID",
    "207": "DMR - RAPID"
}

def draw_hud(weapon_text):
    # Create blank image for 480x320 ILI9488
    img = Image.new("RGB", (480, 320), (0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw.text((40, 140), f"LOADED: {weapon_text}", fill=(0, 255, 0))
    # Command to push 'img' to SPI screen goes here
    # Example: disp.display(img)

# Input from Laptop, Output to Pico 2
laptop_in = serial.Serial('/dev/ttyACM0', 115200)
pico_out = serial.Serial('/dev/ttyAMA0', 115200)

while True:
    if laptop_in.in_waiting > 0:
        data = laptop_in.readline().decode().strip()
        pico_out.write(f"{data}\n".encode())
        
        display_name = id_map.get(data, "IDLE")
        draw_hud(display_name)