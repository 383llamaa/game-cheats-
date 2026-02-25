________________________________________________________________________________
[ SYSTEM INITIALIZATION: CALL OF DUTY MODULE ]
[ REPOSITORY: COD-WARZONE-HARDWARE-INJECTION ]
[ HARDWARE: PI ZERO 2 W + PICO 2 + ILI9488 HUD ]
________________________________________________________________________________

> HELP --USAGE_GUIDE

================================================================================
|                         FILE EXECUTION HIERARCHY                             |
================================================================================

[ FILE 1: pico_warzone.py ]
- LOCATION: Raspberry Pi Pico 2 (Root Directory)
- ROLE: The "Hardware Injector"
- USAGE: Rename this file to 'code.py' on your Pico 2. It will boot 
  automatically as soon as the Pico 2 is plugged into the Xbox. It stays 
  idle until it receives a command from the Pi Zero 2.

[ FILE 2: pi_display.py ]
- LOCATION: Raspberry Pi Zero 2 W
- ROLE: The "Bridge & HUD Driver"
- USAGE: Run this via the terminal on your Pi Zero 2. It listens for 
  commands from your laptop via the USB-C data port and forwards them 
  to the Pico 2 while updating the 3.5" ILI9488 SPI screen.
  
  Terminal Command: 
  $ python3 pi_display.py

[ FILE 3: wz_menu.py ]
- LOCATION: Operator Laptop (Windows/Mac/Linux)
- ROLE: The "Command Center GUI"
- USAGE: Run this on your gaming laptop. It provides the visual buttons 
  for weapon selection. When a button is clicked, it sends the weapon ID 
  code through the USB cable to the Pi Zero 2.

  Terminal Command:
  $ python wz_menu.py

================================================================================
|                         TERMINAL OPERATION EXAMPLE                           |
================================================================================

STEP 1: Plug in the Hardware Chain (Xbox -> Pico 2 -> Pi Zero -> Laptop).
STEP 2: [PI ZERO TERMINAL]
        $ sudo systemctl start spi_driver
        $ python3 pi_display.py
        > [STATUS] HUD INITIALIZED. LISTENING FOR LAPTOP DATA...

STEP 3: [LAPTOP TERMINAL]
        $ python wz_menu.py
        > [STATUS] CONNECTED TO PI ZERO ON COM3.

STEP 4: [IN-GAME ACTION]
        - Operator clicks "MCW (AR)" on Laptop GUI.
        - Pi Zero Screen displays: "LOADED: MCW - LOW RECOIL"
        - Pico 2 applies math: (V: 3.2, H: 0.1)
        - [RESULT] Recoil is neutralized in Warzone.

================================================================================
|                         TROUBLESHOOTING                                      |
================================================================================

- IF HUD IS BLANK: Check SPI wiring and ensure pi_display.py is running.
- IF NO RECOIL PULL: Ensure wz_menu.py is set to the correct COM port.
- IF CONTROLLER DISCONNECTS: Verify the StarTech OTG security handshake.

________________________________________________________________________________
[ END OF DOCUMENT ]
[ SYSTEM STATUS: READY ]
________________________________________________________________________________