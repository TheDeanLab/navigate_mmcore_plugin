=====================
Plugin Installation
=====================

Quick install
=============

**Setup your Python Environment**

Head over to the `miniconda website <https://docs.conda.io/en/latest/miniconda.html#latest-miniconda-installer-links>`_
and install the appropriate version based on your operating system.

.. tip::

    It is also handy to have the `conda cheatsheet <https://docs.conda.io/projects/conda/en/4.6.0/_downloads/52a95608c49671267e40c689e0bc00ca/conda-cheatsheet.pdf>`_
    open when first using miniconda to get accustomed to the commands available.

* Windows: Use the Windows taskbar search to find ``Anaconda Prompt (Miniconda3)``.
  Given how frequently you will use this, we recommend pinning it to your taskbar.
* Linux/Mac: Open a Terminal.

**Create a Python environment called navigate that uses Python version 3.9.7**

.. code-block:: console

    (base) MyComputer ~ $ conda create -n navigate python=3.9.7

**Activate the navigate environment**

.. code-block:: console

    (base) MyComputer ~ $ conda activate navigate

The active environment is shown in parentheses on the far-left.  Originally, we were in
the miniconda ``(base)`` environment. After activating the navigate environment, it
should now show ``(navigate)``.

**Install navigate-mmcore-plugin**

To install the latest version of **navigate-mmcore-plugin**, run the following command:

.. code-block:: console

    (navigate) MyComputer ~ $ pip install git+https://github.com/TheDeanLab/navigate-mmcore-plugin.git

**Run navigate software**

.. code-block:: console

    (navigate) MyComputer ~ $ navigate

.. note::

    If you are running the software on a computer that is not connected to microscope 
    hardware, you can add the flag ``-sh`` (``--synthetic-hardware``) to launch the
    program:

    .. code-block:: console

        navigate -sh

Launching **navigate**
======================

Open an ``Anaconda Prompt (Miniconda3)`` and enter the following.

.. code-block:: console

    (base) conda activate navigate
    (navigate) navigate


Installing the Plugin
======================
