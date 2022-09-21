.. image:: https://api.codacy.com/project/badge/Grade/a793c78a53eb4435a4bb86d725c8f817
   :alt: Codacy Badge
   :target: https://app.codacy.com/gh/saratheriver/ENIGMA?utm_source=github.com&utm_medium=referral&utm_content=saratheriver/ENIGMA&utm_campaign=Badge_Grade

.. image:: https://img.shields.io/badge/license-BSD-brightgreen
   :target: https://opensource.org/licenses/BSD-3-Clause

.. image:: https://readthedocs.org/projects/pip/badge/?version=stable
    :target: https://pip.pypa.io/en/stable/?badge=stable
    :alt: Documentation Status   

.. image:: https://circleci.com/gh/MICA-MNI/ENIGMA/tree/master.svg?style=shield
    :target: https://circleci.com/gh/MICA-MNI/ENIGMA/tree/master

.. image:: https://img.shields.io/badge/doi-10.1101%2F2020.12.21.423838-brightgreen
    :target: https://doi.org/10.1101/2020.12.21.423838

.. image:: https://img.shields.io/twitter/follow/saratheriver?style=flat&logo=twitter&color=brightgreen
    :target: https://twitter.com/intent/follow?screen_name=saratheriver

.. image::  https://img.shields.io/badge/great%20tools-good%20vibes%20%F0%9F%A4%99-brightgreen
    :target: https://www.youtube.com/watch?v=kIV1a8tE_2w&ab_channel=Hypnotized

.. image:: https://img.shields.io/github/stars/MICA-MNI/ENIGMA.svg?style=flat&label=%E2%AD%90%EF%B8%8F%20give%20us%20some%20love&color=brightgreen
    :target: https://github.com/MICA-MNI/ENIGMA/stargazers

.. raw:: html

    <hr>

.. image::  https://github.com/saratheriver/enigma-extra/blob/master/title.png?raw=true
    :align: center
    :scale: 50%

.. raw:: html

    <hr>

The **ENIGMA TOOLBOX** is an open source repository for (*i*) accessing 100+ ENIGMA-derived statistical maps, (*ii*) 
visualizing and manipulating cortical and subcortical surface data, and (*iii*) contextualizing neuroimaging findings 
at the microscale (using *postmortem* gene expression and cytoarchitecture) and macroscale (using structural and functional 
connectome data).

.. image::  https://github.com/saratheriver/enigma-extra/blob/master/Figure0_GH3.png?raw=true
    :align: center
    :scale: 50%

Documentation 💼
---------------------------------------------
Check out our expandable online documentation at http://enigma-toolbox.readthedocs.io to learn how to:

| 🔌 install ENIGMA Toolbox in Python or Matlab
| 💯 load over 100 case-control datasets from several ENIGMA Working Groups
| 🥍 perform cross-disorder analyses
| 🚢 import your own data
| 🧩 map parcellated data to and from vertexwise space
| 🥡 export data and data results to several file formats
| 🧠 visualize and manipulate cortical and subcortical surface data
| 🔗 load preprocessed connectivity data from the Human Connectome Project (HCP)
| 🧬 load gene expression data from the Allen Human Brain Atlas
| 🎣 query pre-defined lists of disease-related genes from published GWAS
| 🔬 stratify neuroimaging findings according to BigBrain statistical moments and gradient
| 📱 stratify neuroimaging findings according to cytoarchitectural variations
| 🛩 build hub susceptibility models
| 📌 identify disease epicenters
| 🌪 perform spin permutation tests on parcellated data

|

Installation 🔨
---------------------------------------------

To install the Toolbox in ``Python``, run the following in your terminal:

.. code-block:: bash

    git clone https://github.com/MICA-MNI/ENIGMA.git
    cd ENIGMA
    python setup.py install

|

To install the Toolbox in ``Matlab``, run the following in your terminal:

.. code-block:: bash

    git clone https://github.com/MICA-MNI/ENIGMA.git

And then simply run the following in Matlab:

.. code-block:: matlab

    addpath(genpath('/path/to/ENIGMA/matlab/'))

|

Acknowledgements 💕
----------------------------

Please acknowledge this work using the citation below:

    Larivière, S., Paquola, C., Park, By. Royer, J., Wang, Y., Benkarim, O., Vos de Wael, R., Valk, S., Thomopoulos, S.I., Kirschner, M., Lewis, L.B., Evans, A.C., Sisodiya, S.M., McDonald, C.R., Thompson, P.T, Bernhardt, B.C.. The ENIGMA Toolbox: multiscale neural contextualization of multisite neuroimaging datasets. *Nat Methods* **18**, 698–700 (2021). https://doi.org/10.1038/s41592-021-01186-4

.. raw:: html

    <hr>
