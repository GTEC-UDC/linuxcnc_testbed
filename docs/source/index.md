# {{project}}

A motor control testbed using the open-source [LinuxCNC](https://www.linuxcnc.org) platform integrated with the [Mesa Electronics](https://store.mesanet.com/) 7i96S and 7I77 interface cards and the [igus® dryve D1](https://www.igus.eu/product/D1) motor controllers.

This system was used to develop and validate the control system for [a large high-precision 3-axis gantry robot system](https://github.com/GTEC-UDC/linuxcnc_gantry_robot).

---

Copyright (C) 2000-2022 LinuxCNC.org\
Copyright (C) 2025 Tomás Domínguez Bolaño, Valentín Barral Vales, Carlos José Escudero Cascón, and José Antonio García Naya.

Permission is granted to copy, distribute and/or modify this document
under the terms of the GNU Free Documentation License, Version 1.3
or any later version published by the Free Software Foundation;
with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.
A copy of the license is included in the section entitled "GNU Free Documentation License".

---

This work has been supported by grant PID2022-137099NB-C42 (MADDIE) and by project TED2021-130240B-I00 (IVRY) funded by MCIN/AEI/10.13039/501100011033 and the European Union NextGenerationEU/PRTR.

:::{ext-image} images/logos/ack_logos.*
:width-html: 700px
:name: fig:ack_logos
:::

:::{only} html
<!-- -->
---
<!-- -->
:::

:::{toctree}
:maxdepth: 2
:numbered:
:caption: Table of Contents

doc/01_introduction/introduction.md
doc/02_igus_dryve_d1/00_index.md
doc/03_linuxcnc/00_index.md
:::

:::{raw} latex
% Do not show section numbers for the following sections in latex
\setcounter{secnumdepth}{-1}
:::

:::{toctree}
:maxdepth: 1

fdl-1.3.md
bibliography.md
:::
