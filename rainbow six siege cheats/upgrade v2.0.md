============================================================

&nbsp;         PICO 2: HARDWARE INJECTION SETUP GUIDE

============================================================



\[STEP 1: INSTALLING THE FIRMWARE]

1\. Hold down the 'BOOTSEL' button on your Pico 2.

2\. While holding, plug the Pico 2 into your laptop via USB.

3\. A new drive named 'RPI-RP2' will appear on your computer.

4\. Download the Pico 2 CircuitPython .UF2 file from:

&nbsp;  https://circuitpython.org/board/raspberry\_pi\_pico2/

5\. Drag and drop that .UF2 file onto the 'RPI-RP2' drive.

6\. The Pico will reboot and appear as a drive named 'CIRCUITPY'.



\[STEP 2: ADDING THE USB LIBRARIES]

The Pico needs 'HID' (Human Interface Device) drivers to

act like a controller/mouse to the Xbox.



1\. Create a folder named 'lib' inside the 'CIRCUITPY' drive.

2\. Download the 'Adafruit HID' library bundle:

&nbsp;  https://github.com/adafruit/Adafruit\_CircuitPython\_HID/releases

3\. Copy the 'adafruit\_hid' folder from the bundle into the 

&nbsp;  'lib' folder on your Pico.

&nbsp;  (Path should be: CIRCUITPY/lib/adafruit\_hid/...)



\[STEP 3: LOADING THE CHEAT SCRIPT]

1\. Open a text editor (Notepad) on your laptop.

2\. Copy the 'Pico 2 Core Script' provided earlier.

3\. Save the file as 'code.py' on the root of the 'CIRCUITPY' drive.

&nbsp;  (CircuitPython runs 'code.py' automatically on startup).



\[STEP 4: XBOX HANDSHAKE BYPASS]

To avoid the 'Unauthorized Accessory' error:

1\. Connect your StarTech OTG Adapter to the Pico 2.

2\. Plug your official Xbox Controller into the OTG Adapter.

3\. Plug the Pico 2's main USB cable into the Xbox.

4\. The Pico 2 will now 'pass through' the security signal 

&nbsp;  from your real controller while injecting your cheats.



\[STEP 5: TESTING]

Open a text document on your laptop and plug the Pico 2 in. 

If you trigger your 'Fire' logic, you should see the cursor 

slowly pull down on your laptop screen. This confirms the 

recoil math is working before you plug it into the Xbox.

============================================================

