============================================================

&nbsp;         HARDWARE UPGRADE: ILI9488 STATUS SCREEN

============================================================



\[WIRING MAP: PI ZERO 2 -> MSP3520]

Screen Pin | Pi Pin (Physical) | Function

------------------------------------------

VCC        | Pin 1 (3.3V)      | Power

GND        | Pin 6 (GND)       | Ground

CS         | Pin 24 (GPIO 8)   | Chip Select

RESET      | Pin 18 (GPIO 24)  | Reset

DC/RS      | Pin 22 (GPIO 25)  | Data/Command

SDI (MOSI) | Pin 19 (GPIO 10)  | Data In

SCK        | Pin 23 (GPIO 11)  | Clock

LED        | Pin 2 (5V)        | Backlight



\[SOFTWARE INSTALL]

1\. Enable SPI: Run 'sudo raspi-config' -> Interface -> SPI -> Yes.

2\. Install Driver: 

&nbsp;  git clone https://github.com/juj/fbcp-ili9341.git

&nbsp;  cd fbcp-ili9341 \&\& mkdir build \&\& cd build

&nbsp;  cmake -DILI9488=ON -DGPIO\_TFT\_DATA\_CONTROL=25 -DGPIO\_TFT\_RESET\_PIN=24 ..

&nbsp;  make -j



\[THE STANDALONE HUD]

Your Pi script can now draw a custom HUD on this screen.

\- TOP BAR: Game Status (Online/Offline)

\- MIDDLE: Big text showing "ASH - R4C"

\- BOTTOM: Recoil Strength Bar (e.g. \[|||||     ] 50%)



\[BENEFIT]

You no longer need to look at your laptop to see if your 

hacks are on. You can glance at the 3.5" screen sitting 

next to your monitor.

============================================================

