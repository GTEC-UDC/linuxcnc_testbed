# Introduction

The system uses LinuxCNC as its control platform, with two Igus dryve D1 controllers which are used to control a stepper motor and a brushless motor, respectively. The system diagram is shown in {numref}`fig:system_diagram`. Below, we detail the system's configuration, including the boards and components used.

:::{ext-figure} images/system_diagram/system_diagram.\*
:height-html: 300px
:name: fig:system_diagram

System diagram.
:::

## LinuxCNC

LinuxCNC, formerly known as the {{EMC}}, is a software system designed for the computer control of various machine tools, such as milling machines and lathes, as well as robots like PUMA and SCARA, and other computer-controlled machinery with up to nine axes. LinuxCNC is free, open-source software. Current versions are fully licensed under the [GPL](https://www.gnu.org/licenses/gpl.html) and [LGPL](https://gnu.org/licenses/lgpl.html).

In our system, LinuxCNC communicates with the Igus dryve D1 controllers via the MESA 7I96S and 7I77 boards. LinuxCNC is responsible for coordinating the operation of all motors, providing precise, real-time control over the system.

Detailed information on LinuxCNC’s operation and configuration can be found in {numref}`sec:linuxcnc`.

## System Hardware

{numref}`fig:installation` shows a photograph of the test setup. This system comprises the following key components:

:::{figure} images/installation_labelled.*
:name: fig:installation

Test setup.
:::

- **Aim-TTI EL302RD Dual Power Supply**: Provides two independent power outputs, each capable of delivering a maximum of 30 V and 2 A. For the test setup, we required 24 V and 5 V power.

- **Two Igus dryve D1 Motor Controllers** [Igus dryve D1](https://www.igus.eu/product/D1): Igus dryve D1 can be used for controlling stepper, DC, and brushless motors in industrial and automation applications. The Igus dryve D1 supports the following communication methods with control systems:

  - **CANopen**: A communication protocol widely used in industrial automation systems, built upon the CAN bus (ISO 11898) standard.
  - **Modbus TCP**: A communication protocol extensively employed in industrial applications for data transmission over Ethernet networks using the TCP protocol.
  - **Analog and Digital Signals**: In addition to network communication options, the Igus dryve D1 can receive analog and digital signals for direct control.

    In this system, we communicate with the Igus dryve D1 controllers using MESA 7I96S and 7I77 boards using digital and analog signals. This setup enables LinuxCNC to have precise, real-time control over the motors' operation.

- **MESA 7I96S Board**: This board is the primary hardware interface between LinuxCNC and the Igus dryve D1 controllers. It connects to the computer running LinuxCNC via an Ethernet connection. Its main functions include:

  - Controlling the stepper motor by sending step and direction signals to its designated Igus dryve D1 controller.
  - Receiving input signals from limit switches.

- **MESA 7I77 Daughter Board**: This board connects to the 7I96S board via a 25-pin flat cable. Its primary functions are:

  - Controlling the brushless motor by sending an analog speed signal to its corresponding Igus dryve D1 controller.
  - Receiving position feedback signals from motor encoders.
  - Receiving warning and error signals from the controllers.
  - Receiving the emergency stop signal when the emergency stop switch is activated.

- **Brushless Motor**: A [STEPPERONLINE 42BLS40-24-01](https://www.omc-stepperonline.com/24v-4000rpm-0-0625nm-26w-1-8a-42x42x40mm-brushless-dc-motor-42bls40-24-01), equipped with a [CUI Devices AMT102-0512-I5000-S](https://www.cuidevices.com/product/motion-and-control/rotary-encoders/incremental/modular/amt10-series) optical encoder of 512 PPR.

- **Stepper Motor**: A [STEPPERONLINE 17HS24-2104-ME1K](https://www.omc-stepperonline.com/nema-17-closed-loop-stepper-motor-65ncm-92oz-in-with-magnetic-encoder-1000ppr-4000cpr-17hs24-2104-me1k). This motor includes a 1000 PPR magnetic encoder.

- **LED Indicators**: Custom indicators with red, yellow, and green LEDs, which provide a visual display of the system's status.

- **Two Buttons for Limit Sensor Simulation**.

- **Emergency Stop Switch**: This switch has both a normally closed and a normally open contact.

The system wiring diagram, detailing all components and their interconnections, is available in the `pruebas_robot.pdf` file.
