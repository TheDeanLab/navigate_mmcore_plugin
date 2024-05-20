
.. _navigate-mmcore-plugin-home:

##########################
**navigate-mmcore-plugin**
##########################


**navigate-mmcore-plugin** is a plugin for navigate, a microscope control software.

**navigate-mmcore-plugin** enables users to access devices supported by the
`Micro-Manager <https://micro-manager.org>`_ Core API (MMCore), greatly increasing
the number of devices that can be controlled by navigate. Currently,
**navigate-mmcore-plugin** supports the following devices:

- Stages
- Shutters

Future versions of **navigate-mmcore-plugin** will support additional devices, including:

- Cameras
- Lasers
- Filter Wheels


.. note::

   This project is under active development. See our `GitHub repository for updates
   <https://github.com/TheDeanLab/navigate-mmcore-plugin>`_.

.. warning::

    Not all devices supported by the Micro-Manager Core API have been tested
    by the Dean Lab. They are available for use at your own risk.
    If you encounter any issues, please report them on as an issue on GitHub.
    No warranty is provided for the use of this software.

.. warning::

    Please be advised that while the Dean Lab has implemented several safeguards in the
    automation of hardware, including but not limited to stage limits, voltage minimums,
    and maximums, are more, there are inherent risks associated with the use of such
    automated systems. Despite these precautions, the complexity and nature of automated
    hardware can lead to unpredictable outcomes. Therefore, the Dean Lab and UT
    Southwestern expressly disclaim any responsibility for any damages, losses, or
    injuries that may arise from or be related to the use of **navigate**.
    Users should be aware of these risks and agree to utilize **navigate** at their own risk.


.. toctree::
   :caption: Installation
   :maxdepth: 2

   software_installation
   micromanager_configuration


.. toctree::
   :caption: Reference
   :maxdepth: 2

   api


**Authors**
============
**navigate-mmcore-plugin** was developed by the Dean lab at UT Southwestern Medical
Center by Annie (Xiaoding) Wang. More information about the Dean Lab can be found
`here <https://www.dean-lab.org>`_.

**Acknowledgements**
============
**Micro-Manager** is an open-source software for microscope control and image
acquisition that is generously supported by a very generous community of developers.
The Dean Lab would like to thank the Micro-Manager team for their selfless contributions
to the scientific community. This includes, but is not limited to, Mark Tsuchida,
Nico Stuurman, Nenad Amodaj, Chris Weisiger, Arthur Edelstein, Henry Pinkard,
Karl Hoover, Ziah Dean, and Oleksiy Danihkhno. We would also like to thank Talley Lambert
for his advice in the development of this plugin.



**Funding**
============
**navigate** is supported by:

-   `UT Southwestern and University of North Carolina Center for Cell Signaling
    <https://cellularsignaltransduction.org>`_, a Biomedical Technology Development
    and Dissemination (BTDD) Center funded by the NIH NIGMS (RM1GM145399).
-   The `Center for Metastatic Tumor Imaging <https://www.metastasis-imaging.org>`_, a
    Cellular Cancer Biology Imaging Research (CCBIR) program funded by the NIH NCI
    (U54CA268072).
-   The Simmons Comprehensive Cancer Center at UT Southwestern Medical Center.
-   The President's Research Council at UT Southwestern Medical Center.
