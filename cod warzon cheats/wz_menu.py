import tkinter as tk
import serial

# Configure to your Pi Zero 2 COM Port
try:
    ser = serial.Serial('COM3', 115200, timeout=1)
except:
    ser = None

def load_profile(p_id):
    if ser:
        ser.write(f"{p_id}\n".encode())
    status.config(text=f"WARZONE ACTIVE: {wz_names[p_id]}")

root = tk.Tk()
root.title("Warzone Loadout Injector")
root.geometry("250x450")
root.configure(bg="#1a1a1a")

wz_names = {
    "0": "SYSTEM OFF",
    "201": "MCW (AR)",
    "202": "SVA-545 (AR)",
    "203": "HRM-9 (SMG)",
    "204": "WSP-9 (SMG)",
    "205": "PULEMYOT (LMG)",
    "206": "MTZ (BATTLE)",
    "207": "INTERCEPTOR (DMR)"
}

status = tk.Label(root, text="SYSTEM READY", fg="#00ff00", bg="#1a1a1a", font=("Courier", 10))
status.pack(pady=20)

for k, v in wz_names.items():
    if k == "0": continue
    btn = tk.Button(root, text=v, width=20, bg="#333333", fg="white", 
                    command=lambda i=k: load_profile(i))
    btn.pack(pady=2)

tk.Button(root, text="STOP ALL", width=20, bg="red", command=lambda: load_profile("0")).pack(pady=20)

root.mainloop()