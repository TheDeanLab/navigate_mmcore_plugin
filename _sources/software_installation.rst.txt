=====================
Plugin Installation
=====================

Install navigate
===============

This guide assumes that the latest version of **navigate** has been
installed and is functional. If not, please refer to the `installation guide
<https://thedeanlab.github.io/navigate/software_installation.html>`_ in **navigate**'s
documentation.

---------------------

Install navigate-mmcore-plugin
==============================

Once **navigate** is installed, the next step is to install the **navigate-mmcore-plugin**.
Broadly, this consists of activating the **navigate** environment, cloning the
**navigate-mmcore-plugin** repository, and installing the plugin.

Activate the navigate Environment
---------------------------------

.. code-block:: console

    (base) MyComputer ~ $ conda activate navigate

Clone **navigate-mmcore-plugin**
--------------------------------

Clone the latest version of **navigate-mmcore-plugin**, change your directory to its
root folder (e.g., ``D://path/to/navigate-mmcore-plugin/``, and install the libraries
necessary to run **navigate-mmcore-plugin** using the following command:

.. code-block:: console

    (navigate) MyComputer ~ $ pip install -e .

Run **navigate** Software
----------------------------

.. code-block:: console

    (navigate) MyComputer ~ $ navigate

.. note::

    If you are running the software on a computer that is not connected to any
    microscope hardware, you can add the flag ``-sh`` (``--synthetic-hardware``) to
    launch the program:

    .. code-block:: console

        navigate -sh

Installing the **navigate-mmcore-plugin**
-----------------------------------------

Once **navigate** is running, you can install the plugin by selecting the menu
:menuselection:`Plugins --> Install Plugin` and selecting the **navigate-mmcore-plugin**
folder. **navigate** will automatically install the plugin and prompt you to restart
the software. After restarting, the plugin will be available in the **navigate**

---------------------

Install Micro-Manager
=====================
Once **navigate** and the **navigate-mmcore-plugin** are installed, you need to install
and configure Micro-Manager.

Download the nightly build of Version 2.0 of **Micro-Manager** from the
`Micro-Manager website <https://micro-manager.org/Micro-Manager_Nightly_Builds>`_

Detailed information on how to install **Micro-Manager** can be found `here
<https://micro-manager.org/Micro-Manager_Installation_Notes>`_.


Configure Devices in Micro-Manager
-----------------------------------

Next you should configure the devices in **Micro-Manager** and save the configuration file. 
This is done by opening the Micro-Manager and using the Hardware Configuration Wizard. 
Importantly, all of the devices should be confirmed functional in **Micro-Manager** before proceeding to the next step.

Installation details for each device can be found `here <https://micro-manager.org/Device_Support>`_.

---------------------

Configure your Windows Environment
==================================

Next, you need to make sure that Windows knows where to find the Micro-Manager
device files. This is done by adding the path to the Micro-Manager device files
to the Windows environment variables.

1. Open the Windows Control Panel.
2. Click on System and Security.
3. Click on System.
4. Click on Advanced system settings.
5. Click on Environment Variables.
6. Double click on the Path variable in the System variables section.
7. Click on New and add the path to the Micro-Manager device files. This is
   typically ``C:\\Program Files\\Micro-Manager-2.0``.

Once this is complete, restart your Anaconda Prompt so that the new Path variable
is recognized.

---------------------

Modify the Configuration Files
==============================

Configure *navigate-mmcore-plugin* configuration file.
-----------------------------------------------------

Next, you will need to modify the configuration file for the **navigate-mmcore-plugin**.
Provide it with the name of the plugin, the view type (e.g., if it should be displayed
as a tab or a popup), and the path to the Micro-Manager device adapter.

.. code-block:: yaml

    name: MMCore Plugin
    view: Popup # Tab or Popup if has an GUI

    device_adapter_path:
      - "C:\\Program Files\\Micro-Manager-2.0"


Configure the **navigate** configuration file.
----------------------------------------------

Finally, you will need to modify the **navigate** configuration file to include the
device that you wish to use. For example, if we were to be configuring MMCore to
use a Physik Instrumente (PI) stage, the configuration file would look like this:

.. code-block:: yaml


  stage:
    hardware:
      -
        type: MMCore
        serial_number: 119060508
        config_path: "C:\\Program Files\\Micro-Manager-2.0\\test.cfg"
        axes: [z] # axes used in navigate
        axes_mapping: [z] # axes used in MMCore

      -
        type: PI
        controllername: E-709
        stages: P-726.1CD
        refmode: ATZ
        serial_number: 0116049747
      -
        type: SyntheticStage
        serial_number: 01234

Here, the first stage in the list, which is type ``MMCore``, is the stage that will be
used by the **navigate-mmcore-plugin**. The ``serial_number`` is the serial number of 
the stage and the ``config_path`` is the path to the Micro-Manager configuration file.


---------------------

Launch the Software
===================

Once the configuration files have been modified, you can launch **navigate** and the
**navigate-mmcore-plugin**. The plugin will automatically connect to the Micro-Manager
device adapter and the devices will be available for use in **navigate**.