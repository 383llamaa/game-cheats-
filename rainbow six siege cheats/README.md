============================================================

&nbsp;          R6 HARDWARE INJECTION SYSTEM (XBOX)

============================================================



\[HARDWARE REQUIREMENTS]

1\. Raspberry Pi Zero 2 W (The Brain)

2\. Raspberry Pi Pico 2 (The Injector)

3\. 4K HDMI Capture Card w/ Loop-Out

4\. StarTech Micro-USB OTG Adapter

5\. Laptop (The Command Center)



\[WIRING DIAGRAM]

1\. Xbox HDMI OUT -> Capture Card IN

2\. Capture Card OUT -> Gaming Monitor

3\. Capture Card USB -> Pi Zero 2 W

4\. Pi Zero 2 W USB -> Laptop (Data/Power)

5\. Pi Zero 2 W GPIO/USB -> Pico 2

6\. Official Xbox Controller -> OTG Adapter -> Pico 2

7\. Pico 2 -> Xbox Console USB Port



\[PICO 2 SETUP]

1\. Hold BOOTSEL on Pico 2, plug into Laptop.

2\. Drag 'pico2\_circuitpython.uf2' onto RPI-RP2 drive.

3\. Open CIRCUITPY drive. Create a folder named 'lib'.

4\. Put 'adafruit\_hid' folder inside 'lib'.

5\. Save SCRIPT\_1 (below) as 'code.py' on the Pico 2.



\[LAPTOP SETUP]

1\. Install Python 3 on your Laptop.

2\. Install Serial library: 'pip install pyserial'

3\. Save SCRIPT\_2 (below) as 'menu.py' on your Laptop.



\[OPERATION]

1\. Power on Xbox and Monitor.

2\. Connect Pi Zero 2 W to Laptop.

3\. Run 'menu.py' on Laptop.

4\. Select Gun Profile to instantly swap recoil math.

5\. Unplug Pi Zero 2 W to wipe all temporary session data.



============================================================

