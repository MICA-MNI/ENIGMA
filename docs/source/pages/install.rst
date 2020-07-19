.. _install_page:

Installation
==============================

**ENIGMA TOOLBOX** is available in Python and MATLAB


Python installation
-------------------

**ENIGMA TOOLBOX** has the following dependencies:

- `numpy <https://numpy.org/>`_
- `scipy <https://scipy.org/scipylib/index.html>`_
- `scikit-learn <https://scikit-learn.org/stable/>`_
- `vtk <https://vtk.org/>`_
- `matplotlib <https://matplotlib.org/>`_
- `nibabel <https://nipy.org/nibabel/index.html>`_
-

Additional softwares for gene expression mapping and surface visualization can be directly downloaded from the **ENIGMA TOOLBOX** Github as follows: ::

    git clone https://github.com/saratheriver/ENIGMA.git
    cd python/BrainSpace && python setup.py install
    cd python/abagen && python setup.py install


Alternatively, you can also install BrainSpace and abagen using ``pip``: ::

    pip install brainspace abagen





MATLAB installation
-------------------

**ENIGMA TOOLBOX** was tested with MATLAB R2017b.

To install the MATLAB toolbox simply `download
<https://github.com/MICA-MNI/ENIGMA>`_ and unzip the GitHub toolbox, and run
the following in MATLAB: ::

    addpath('/path/to/ENIGMA/matlab/')

