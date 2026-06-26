# Travel Navigation Macropad

## Overview

This project is a compact 4-key travel-themed macropad powered by the Seeed Studio XIAO RP2040. It features four directional navigation keys and two SK6812 MINI-E RGB LEDs. The project includes a custom PCB designed in KiCad, a custom enclosure designed in Fusion 360, and firmware developed using KMK.

## Features

* Seeed Studio XIAO RP2040
* 4 Mechanical Switches
* 2 SK6812 MINI-E RGB LEDs
* Compact 2-Layer PCB
* Custom Designed Enclosure
* KMK Firmware
* USB-C Connectivity

## Key Layout

* **8** → Up Arrow
* **6** → Right Arrow
* **4** → Left Arrow
* **2** → Down Arrow

The layout is inspired by classic numpad navigation controls to provide an intuitive travel and navigation experience.

## Design Process

After completing the PCB in KiCad, I verified the layout by checking component placement, USB connector alignment, mounting hole positions, and overall board dimensions. I then designed the top and bottom enclosure in Fusion 360 using the PCB as a reference, creating switch cutouts, screw holes, and the internal cavity. After verifying the enclosure dimensions, I exported the models as STEP files. Finally, I configured the KMK firmware by mapping the correct GPIO pins and assigning directional arrow key functions.
