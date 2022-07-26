.. _install_page:


.. title:: Install me

Installation
==============================

**ENIGMA TOOLBOX** is available in Python and Matlab!

.. tabs::

    .. tab:: Python
    
        **ENIGMA TOOLBOX** has the following dependencies:

        - `numpy <https://numpy.org/>`_
        - `matplotlib <https://matplotlib.org/>`_ 
        - `vtk <https://vtk.org/>`_
        - `nibabel <https://nipy.org/nibabel/index.html>`_
        - `pillow <https://pillow.readthedocs.io/en/stable/>`_
        - `pandas <https://pandas.pydata.org/>`_
        - `scipy <https://www.scipy.org/>`_
        - `scikit-learn <https://scikit-learn.org/stable/>`_
        - `nilearn <https://nilearn.github.io/>`_

        The **ENIGMA TOOLBOX** can be directly downloaded from Github as follows: ::

            git clone https://github.com/MICA-MNI/ENIGMA.git
            cd ENIGMA
            python setup.py install


    .. tab:: Matlab

        **ENIGMA TOOLBOX** was tested with Matlab R2017b.

        To install the Matlab toolbox simply `download <https://github.com/MICA-MNI/ENIGMA/archive/2.0.0.zip>`_ 
        and unzip the GitHub toolbox (slow 🐢) or run the following command in your terminal (fast 🐅): ::
            
            git clone https://github.com/MICA-MNI/ENIGMA.git
        
        
        Once you have the toolbox on your computer, simply run the following command in Matlab: ::

            addpath(genpath('/path/to/ENIGMA/matlab/'))