import tkinter as tk
import serial

# Connect to the Pi Zero 2 / Pico 2 via USB
# (Update 'COM3' or '/dev/ttyACM0' to match your port)
ser = serial.Serial('COM3', 115200)

def set_gun(gun_id):
    ser.write(f"{gun_id}\n".encode())
    label.config(text=f"ACTIVE GUN: {gun_names[gun_id]}")

root = tk.Tk()
root.title("R6 Loadout Swapper")
root.geometry("200x400")

gun_names = {"0":"OFF", "1":"R4C", "2":"MP5", "3":"SMG11", "4":"SMG12", "5":"Vector", "6":"F2", "7":"G8A1"}

label = tk.Label(root, text="ACTIVE GUN: OFF", fg="red")
label.pack(pady=10)

for id, name in gun_names.items():
    btn = tk.Button(root, text=name, width=15, command=lambda i=id: set_gun(i))
    btn.pack(pady=2)

root.mainloop()