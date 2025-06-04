# Introducción

El sistema utiliza LinuxCNC como plataforma de control principal, y dos
controladores Igus dryve D1 para controlar respectivamente un motor paso
a paso y un motor sin escobillas. El diagrama del sistema se muestra en
la {numref}`fig:system_diagram`. A continuación, se detalla la configuración del sistema, incluyendo las placas y componentes utilizados.

:::{ext-figure} images/system_diagram/system_diagram.\*
:height-html: 300px
:name: fig:system_diagram

Esquema del sistema.
:::

## LinuxCNC

LinuxCNC, previamente el {{EMC}}, es un sistema de software para el control
por ordenador de máquinas herramienta como fresadoras y tornos, robots
como puma y scara, y otras máquinas controladas por ordenador de hasta 9
ejes. LinuxCNC es software libre con código fuente abierto. Las
versiones actuales de LinuxCNC están totalmente licenciadas bajo la
[GPL](https://www.gnu.org/licenses/gpl.html) y la
[LGPL](https://gnu.org/licenses/lgpl.html).

En nuestro sistema usamos LinuxCNC para comunicarnos con los
controladores Igus dryve D1 mediante las placas MESA 7I96S y 7I77.
LinuxCNC se encarga de coordinar el funcionamiento de todos los motores,
proporcionándonos un control preciso y en tiempo real del sistema.

En la {numref}`sec:linuxcnc` se describe en
detalle el funcionamiento y la configuración de LinuxCNC.

## Hardware del sistema

En la {numref}`fig:installation` se muestra una
fotografía del montaje de prueba, este sistema consta de los siguientes
elementos principales:

:::{figure} images/installation_labelled.*
:name: fig:installation

Montaje de prueba.
:::

- **Fuente de alimentación doble Aim-TTI EL302RD**: Proporciona dos
    fuentes de alimentación con un máximo de 30 V y 2 A cada una. En el
    montaje de prueba hemos necesitado alimentación de 24 V y 5 V.

- **2 controladores de motores** [Igus dryve
    D1](https://www.igus.eu/product/D1): Los controladores Igus dryve D1
    son dispositivos utilizados para controlar motores paso a paso, de
    corriente continua, y sin escobillas en aplicaciones industriales y
    de automatización. Los Igus dryve D1 admiten las siguientes formas
    de interacción con sistemas de control:

  - **CANopen**: Protocolo de comunicación usado en sistemas de
        automatización industrial, basado en el bus CAN (ISO 11898).
  - **Modbus TCP**: Protocolo de comunicación ampliamente utilizado
        en aplicaciones industriales para la transmisión de datos en
        redes Ethernet sobre el protocolo TCP.
  - **Señales analógicas y digitales**: Además de las opciones de
        comunicación en red, los dryve D1 pueden recibir señales
        analógicas y digitales para el control directo.

    En nuestro caso nos comunicamos con los controladores Igus dryve D1
    mediante las placas MESA 7I96S y 7I77 usando señales digitales y
    analógicas. De esta forma, podemos emplear LinuxCNC para tener un
    control preciso y en tiempo real sobre el funcionamiento de los
    motores en el sistema.

- **Placa** [MESA
    7I96S](http://store.mesanet.com/index.php?route=product/product&product_id=374):
    Es la interfaz de hardware principal entre LinuxCNC y los
    controladores Igus dryve D1. Esta placa está conectada a la
    computadora que ejecuta LinuxCNC a través de una conexión Ethernet.
    Sus funciones principales incluyen:

  - Controlar el motor paso a paso enviando señales de paso y
        dirección al controlador Igus dryve D1 correspondiente.
  - Recibir las señales de los interruptores de límite.

- **Placa hija** [MESA
    7I77](http://store.mesanet.com/index.php?route=product/product&product_id=120):
    Está conectada a la placa 7i96S mediante un cable plano de 25 pines.
    Sus funciones principales incluyen:

  - Controlar el motor sin escobillas enviando una señal analógica
        de velocidad al controlador Igus dryve D1 correspondiente.
  - Recibir las señales de posición de los encoders de los motores.
  - Recibir las señales de advertencia y error provenientes de los
        controladores.
  - Recibir la señal de parada de emergencia al presionar el
        interruptor de parada de emergencia.

- **Motor sin escobillas**: [STEPPERONLINE
    42BLS40-24-01](https://www.omc-stepperonline.com/24v-4000rpm-0-0625nm-26w-1-8a-42x42x40mm-brushless-dc-motor-42bls40-24-01),
    con un codificador óptico [CUI Devices
    AMT102-0512-I5000-S](https://www.cuidevices.com/product/motion-and-control/rotary-encoders/incremental/modular/amt10-series)
    de 512 PPR.

- **Motor paso a paso**: [STEPPERONLINE
    17HS24-2104-ME1K](https://www.omc-stepperonline.com/nema-17-closed-loop-stepper-motor-65ncm-92oz-in-with-magnetic-encoder-1000ppr-4000cpr-17hs24-2104-me1k).
    Incluye codificador magnético de 1000 PPR.

- **Indicadores LED**: Sistema de desarrollo propio con LEDs rojo,
    amarillo y verde, que permite mostrar visualmente el estado del
    sistema.

- **2 botones para simular sensores de límites**.

- **Interruptor de parada de emergencia**: Dispone de un contacto
    normalmente cerrado y un contacto normalmente abierto.

El esquema de conexionado del sistema, donde se especifican todos los
componentes usados y sus conexiones, se proporciona en el archivo
`pruebas_robot.pdf`.
