import PIL.Image, PIL.ImageDraw, PIL.ImageFont

def update_hud(gun_name, strength):
    img = PIL.Image.new("RGB", (480, 320), (0, 0, 0))
    draw = PIL.ImageDraw.Draw(img)
    
    # Draw Gun Name
    draw.text((20, 100), f"ACTIVE: {gun_name}", fill="white")
    
    # Draw Recoil Bar
    draw.rectangle([20, 200, 20 + (strength * 4), 230], fill="red")
    
    # Push to SPI Screen
    disp.image(img)