.. _install_page:

Installation
==============================

**ENIGMA TOOLBOX** is available in Python and MATLAB


.. tabs::

    .. tab:: Python installation

        **ENIGMA TOOLBOX** has the following dependencies:

        - `numpy <https://numpy.org/>`_
        - `panda <https://pandas.pydata.org/>`_
        - `vtk <https://vtk.org/>`_
        - `nibabel <https://nipy.org/nibabel/index.html>`_
        - `nilearn <https://nilearn.github.io/>`_

        The **ENIGMA TOOLBOX** can be directly downloaded from Github as follows: ::

            git clone https://github.com/saratheriver/ENIGMA.git
            cd ENIGMA
            python setup.py install


        Alternatively, you can also install the **ENIGMA TOOLBOX** using ``pip``: ::

            pip install enigmatoolbox



    .. tab:: Matlab installation

        **ENIGMA TOOLBOX** was tested with MATLAB R2017b.

        To install the MATLAB toolbox simply `download
        <https://github.com/MICA-MNI/ENIGMA>`_ and unzip the GitHub toolbox, and run
        the following in MATLAB: ::

            addpath('/path/to/ENIGMA/matlab/')