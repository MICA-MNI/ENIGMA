.. _install_page:

Installation
==============================

**ENIGMA TOOLBOX** is available in Python and MATLAB


Python installation
-------------------

**ENIGMA TOOLBOX** relies heavily on BrainSpace, which is already included in our repository.

Alternatively, you can also install BrainSpace using ``pip``: ::

    pip install brainspace


Or directly from the **ENIGMA TOOLBOX** Github as follows: ::

    git clone https://github.com/MICA-MNI/ENIGMA.git
    cd python/BrainSpace
    python setup.py install


**ENIGMA TOOLBOX** and BrainSpace have the following dependencies:

- `numpy <https://numpy.org/>`_
- `scipy <https://scipy.org/scipylib/index.html>`_
- `scikit-learn <https://scikit-learn.org/stable/>`_
- `vtk <https://vtk.org/>`_
- `matplotlib <https://matplotlib.org/>`_
- `nibabel <https://nipy.org/nibabel/index.html>`_

Nibabel is required for reading/writing Gifti surfaces. Matplotlib is only
used for colormaps and we may remove this dependency in future releases.
To enable interactivity, some plotting functionality in IPython notebooks makes
use of the panel package. PyQT is another dependency for background plotting.
See `PyVista <https://docs.pyvista.org/plotting/qt_plotting.html#background-plotting>`_
for more on background plotting. The support of background rendering however
is still experimental.

* `panel <https://panel.pyviz.org/>`_
* `pyqt <https://riverbankcomputing.com/software/pyqt/intro>`_



MATLAB installation
-------------------

**ENIGMA TOOLBOX** was tested with MATLAB R2017b.

To install the MATLAB toolbox simply `download
<https://github.com/MICA-MNI/ENIGMA>`_, unzip the GitHub toolbox, and run
the following in MATLAB: ::

    addpath('/path/to/ENIGMA/matlab/')

