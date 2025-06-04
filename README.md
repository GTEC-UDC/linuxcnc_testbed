# LinuxCNC Motor Control Testbed

<div align="center">

<img src="media/testbed_picture.jpg" style="width:100%; max-width:700px;"/>

[![LinuxCNC](https://img.shields.io/badge/Control-LinuxCNC-blue.svg)](https://linuxcnc.org/)
[![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC%20BY--SA%204.0-limegreen.svg)](https://creativecommons.org/licenses/by-sa/4.0/)
[![Documentation](https://img.shields.io/badge/docs-sphinx-blue.svg)](docs/)
[![Python](https://img.shields.io/badge/python-3.x-blue.svg)](https://python.org)

</div>

## 🎯 Overview

A motor control testbed using the open-source [LinuxCNC](https://www.linuxcnc.org) platform integrated with the [Mesa Electronics](https://store.mesanet.com/) 7i96S and 7I77 interface cards and the [Igus dryve D1](https://www.igus.eu/product/D1) motor controllers.

This system was used to to develop and validate the control system for a gantry robot.

## ✨ Key Features

- **⏱️ Real-time Control**: Precise real-time multi-axis motion using LinuxCNC with MESA interface cards and Igus dryve D1 motor controllers.
- **⚙️ Dual Motor System**: Stepper and brushless motors.
- **🔁 Closed Loop Control**: High-precision encoder feedback for accurate positioning.
- **🛡️ Safety Systems**: Emergency stop and limit switch functionality.
- **🚦 Visual Indicators**: Custom LED status system.

## 📖 Documentation

The following documentation is provided in this repository:

- 📘 **Technical Documentation**: Complete system documentation and setup guide in `docs/`
- ⚡ **Electrical Installation**: KiCAD electrical schematics in `electrical_installation/`

To build the Sphinx documentation:

```bash
cd docs
pip install -r requirements.txt
make html
```

## 🎥 Media

| Media | Description |
|-------|-------------|
| 📸 [**System Photo**](media/prototype_picture.jpg) | Photo of the complete system |
| 🎬 [**Demo Video**](media/prototype_video.webm) | System operation demonstration |

## 🛠️ Hardware Components

| Component | Model | Quantity | Function |
|-----------|-------|----------|----------|
| **Control Computer** | PC running LinuxCNC | 1 | Real-time motor coordination |
| **Motor Controllers** | Igus dryve D1 | 2 | Individual motor control |
| **Main Interface** | MESA 7I96S | 1 | Ethernet-LinuxCNC bridge. Stepper motor control. Limits detection |
| **I/O Expansion** | MESA 7I77 | 1 | Brushless motor control. Encoder inputs. Emergency stop detection and LED indicators|
| **Stepper Motor** | STEPPERONLINE 17HS24-2104-ME1K | 1 | Motor with 1000 PPR magnetic encoder |
| **Brushless Motor** | STEPPERONLINE 42BLS40-24-01 + CUI Devices AMT102-0512-I5000-S | 1 | Motor with 512 PPR optical encoder |
| **Power Supply** | Aim-TTI EL302RD | 1 | Dual output (24V/5V) |
| **Emergency Stop** | Push-button with NO/NC contacts | 1 | System safety shutdown |
| **Limit Switches** | Push-button switches | 2 | Position boundary detection |
| **LED Indicators** | 24V panel mount LEDs | 3 | System state indication |

## 🔧 System Architecture

![Prototype System](media/system_diagram.svg)

## 📁 Repository Structure

```txt
linuxcnc-testbed/
├── 📄 README.md             # This file
├── 🎥 media/                # Pictures and videos
├── 📚 docs/                 # Technical Documentation
├── ⚙️ linuxcnc/             # LinuxCNC configurations
├── 📋 schematics/           # Wiring diagrams
├── 📝 scripts/              # Example control scripts
├── 🔧 gcode/                # G-code example
└── 📄 documents/            # Hardware datasheets and manuals
```

## 📄 License

This project is licensed under the [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/) (CC BY-SA 4.0), except for files in the `documents/` directory. The Files in the `documents/` directory are datasheets and manuals from different manufacturers and retain their original copyright, these are included for reference only.
