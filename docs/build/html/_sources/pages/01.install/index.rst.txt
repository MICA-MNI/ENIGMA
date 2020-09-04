.. _install_page:

.. Alternatively, you can also install the **ENIGMA TOOLBOX** using ``pip``: ::
    pip install enigmatoolbox

.. title:: Install me! 👶🏽

Installation
==============================

**ENIGMA TOOLBOX** is available in Python and MATLAB!

.. tabs::

    .. tab:: Python installation
    
        **ENIGMA TOOLBOX** has the following dependencies:

        - `numpy <https://numpy.org/>`_
        - `pandas <https://pandas.pydata.org/>`_
        - `vtk <https://vtk.org/>`_
        - `nibabel <https://nipy.org/nibabel/index.html>`_
        - `nilearn <https://nilearn.github.io/>`_
        - `matplotlib <https://matplotlib.org/>`_

        The **ENIGMA TOOLBOX** can be directly downloaded from Github as follows: ::

            git clone https://github.com/MICA-MNI/ENIGMA.git
            cd ENIGMA
            python setup.py install


    .. tab:: Matlab installation

        **ENIGMA TOOLBOX** was tested with MATLAB R2017b.

        To install the MATLAB toolbox simply `download <https://github.com/MICA-MNI/ENIGMA/archive/0.0.1.zip>`_ 
        and unzip the GitHub toolbox, and run the following command in MATLAB: ::

            addpath('/path/to/ENIGMA/matlab/')