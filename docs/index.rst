.. ENIGMA TOOLBOX documentation master file, created by
   sphinx-quickstart on Wed Jul 15 16:09:38 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. **ENIGMA TOOLBOX**
   ============================
   *An open source repository for the sharing of neuroimaging and genetics data, analytical
   codes, and visualization tools that are 100% ENIGMA-friendly and -focused.*

.. title:: ENIGMA TOOLBOX

.. raw:: html

   <style type="text/css">
      hr {
      width: 100%;
      height: 1px;
      background-color: #259595;
      margin-top: 24px;
      }
   </style>

.. .. image:: ./pages/extrafigs/wmap.png
   :align: left
   :target: http://enigma.ini.usc.edu/
   :alt: ENIGMA TOOLBOX


**Welcome to the ENIGMA TOOLBOX 👋🏼**
==========================================

.. raw:: html

   <a href="http://enigma.ini.usc.edu/">
      <img src="https://raw.githubusercontent.com/saratheriver/enigma-extra/master/wmap2.gif"
         width=300px>
   </a>


.. raw:: html

   <hr>

|


Data archiving and accessing 🗝
------------------------------------
The **ENIGMA TOOLBOX** has a *No data, No problem* policy! We provide a central repository for archiving meta-analytical :ref:`case-control 
comparisons<load_sumstats>` across a wide range of disorders. As many ENIGMA groups have moved beyond meta-analysis 
towards ‘mega’-analysis of subject-level data, the **ENIGMA TOOLBOX** also includes subject-level :ref:`example data<load_ct>` 
from an individual site that have been processed according to ENIGMA protocols.

.. raw:: html

   <br>

Visualization tools 🎨
-------------------------------------
Tired of displaying your surface findings in tables? Look no further! The **ENIGMA TOOLBOX** has got you 
covered! Check out our :ref:`visualization tools<surf_visualization>` and project your cortical and subcortical data to the surface!

.. raw:: html

   <br>

Data sharing and exploiting 💌
------------------------------------
As part of the **ENIGMA TOOLBOX**, we are 
also making several data matrices openly available! As of now, these include :ref:`functional and structural 
connectivity data<hcp_connectivity>` and :ref:`transcriptomic data<gene_maps>`.

.. raw:: html

   <br>

Advanced analytical workflows 🦾
--------------------------------------------------------
The main goal of the **ENIGMA TOOLBOX** is
to provide the ENIGMA community with open-access pipelines and analytical tools for 
conducting advanced secondary analyses, offering a platform to facilitate results reproducibility both 
*within* and *across* ENIGMA Working Groups. From these workflows, users can gain further neurobiological 
insights into how disease-related regional susceptibility patterns are anchored to multiple scales of 
cortical and subcortical brain network architecture.

.. raw:: html

   <br>

Step-by-step tutorials 👣
------------------------------------
The **ENIGMA TOOLBOX** includes ready-to-use and easy-to-follow code snippets
for every functionality and analytical workflow! Owing to its comprehensive tutorials, detailed functionality descriptions, 
and visual reports, the **ENIGMA TOOLBOX** is easy to use for researchers and clinicians without extensive programming expertise. 

.. raw:: html

   <br>

Development and getting involved ⚙️
-------------------------------------------
Should you have any problems, questions, or suggestions about the **ENIGMA TOOLBOX**, please do not
hesitate to post them to our `mailing list <https://groups.google.com/g/enigma-toolbox>`_! Or are you interested in collaborating 
or sharing your ENIGMA-related codes/tools? `Noice <https://www.urbandictionary.com/define.php?term=noice>`_! 
Make sure you familiarize yourself with our `contributing guidelines <https://github.com/MICA-MNI/ENIGMA/blob/master/CONTRIBUTING.md>`_ 
first and then discuss your ideas on our Github `issues <https://github.com/MICA-MNI/ENIGMA/issues>`_ and 
`pull request <https://github.com/MICA-MNI/ENIGMA/pulls>`_.

.. toctree::
   :maxdepth: 1
   :hidden:
   :caption: Getting started
   
   pages/01.install/index
   pages/02.01.tutorialsinstructions/index
   pages/02.whatsnew/index


.. toctree::
   :maxdepth: 1
   :hidden:
   :caption: ENIGMA datasets
   
   pages/04.loadsumstats/index
   pages/03.loadct/index


.. toctree::
   :maxdepth: 1
   :hidden:
   :caption: Surface data visualization

   pages/12.visualization/index


.. toctree::
   :maxdepth: 1
   :hidden:
   :caption: Data sharing and exploiting
   
   pages/05.HCP/index
   pages/10.genemaps/index


.. toctree::
   :maxdepth: 1
   :hidden:
   :caption: Microscale contextualization

   pages/11.epilepsygenes/index
   pages/11.01.bigbrain/index
   pages/11.02.voneconomo/index


.. toctree::
   :maxdepth: 1
   :hidden:
   :caption: Network-based atrophy models
   
   pages/06.hubs/index
   pages/07.epicenter/index
   pages/08.spintest/index


.. .. toctree::
   :maxdepth: 1
   :hidden:
   :caption: Structural covariance networks
   pages/08.covariance/index
   pages/09.gt/index


.. toctree::
   :maxdepth: 1
   :hidden:
   :caption: References & acknowledgements

   pages/13.citeus/index
   pages/13.01.apireference/index
   pages/13.02.apireferencematlab/index
   pages/14.refs/index
   pages/15.funding/index

|

___________________________________________________________________________________________________

.. raw:: html

   <br>

Core developers 👩🏻‍💻
-------------------------

- **Sara Larivière**, *MICA Lab - Montreal Neurological Institute*
- **Boris Bernhardt**, *MICA Lab - Montreal Neurological Institute*