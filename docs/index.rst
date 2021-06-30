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

   <a href="https://github.com/MICA-MNI/ENIGMA">
      <img src="https://github.com/saratheriver/enigma-extra/blob/master/Enigma_toolbox2.png?raw=true"
         width=500px>
   </a>


.. raw:: html

   <hr>

|


100+ ENIGMA-derived statistical maps 💯
-------------------------------------------------
The **ENIGMA TOOLBOX** provides a centralized, and continuously updated, repository of meta-analytical :ref:`case-control 
comparisons <load_sumstats>` across a wide range of disorders. As many ENIGMA groups have moved beyond meta-analysis 
towards ‘mega’-analysis of subject-level data, the **ENIGMA TOOLBOX** also includes an example of subject-level :ref:`example data<load_ct>` 
from an individual site that have been processed according to `ENIGMA protocols <http://enigma.ini.usc.edu/protocols/>`_. 
It should be noted, however, that subject-level or raw imaging data are not openly available for dissemination to the scientific community. 
Interested scientists are encouraged to visit the `ENIGMA website <http://enigma.ini.usc.edu/>`_ to learn more about 
current projects, joining and contributing to an active Working Group, 
or proposing a new group.

.. raw:: html

   <br>

Compatible with any neuroimaging datasets and software 💌
--------------------------------------------------------------------
To increase generalizability and usability, every function within the **ENIGMA TOOLBOX** is also compatible with typical 
neuroimaging datasets parcellated according to the `Desikan-Killiany <https://www.sciencedirect.com/science/article/abs/pii/S1053811906000437?via%3Dihub>`_, 
`Glasser <https://www.nature.com/articles/nature18933>`_, and 
`Schaefer <https://academic.oup.com/cercor/article/28/9/3095/3978804>`_ parcellations. 

To simplify things, we provide tutorials on how to (*i*) :ref:`import vertexwise and/or parcellated data <import_data>`, 
(*ii*) :ref:`parcellate vertexwise cortical data <vw_to_parc>`, (*iii*) :ref:`map parcellated data to the surface <parc_to_vw>`, and 
(*iv*) :ref:`export data results <export_data>`. Import/export file formats include: .txt/.csv, 
FreeSurfer/"curv". mgh/.mgz, GIfTI/.gii, and CIfTI/.dscalar.nii/.dtseries.nii. Cortical and subcortical surfaces are also available in FreeSurfer/surface, GIfTI/.gii, .vtk, and .obj 
formats, allowing cross-software compatibility.

.. raw:: html

   <br>

Cortical and subcortical visualization tools 🎨
---------------------------------------------------------
Tired of displaying your surface findings in tables? Look no further! The **ENIGMA TOOLBOX** has got you 
covered! Check out our :ref:`visualization tools<surf_visualization>` to project cortical and subcortical data results 
to the surface and generate publication-ready figures.

.. raw:: html

   <br>

Preprocessed micro- and macroscale data 🤹🏼‍♀️
------------------------------------------------------------------------
The emergence of open databases yields new opportunities to link human gene expression, cytoarchitecture, and connectome data.  
As part of the **ENIGMA TOOLBOX**, we have generated and made available a range of preprocessed and parcellated data, including: 
(*i*) :ref:`transcriptomic data <gene_maps>` from the `Allen Human Brain Atlas <https://human.brain-map.org/>`_, 
(*ii*) :ref:`cytoarchitectural data <big_brain>` from the `BigBrain Project <https://science.sciencemag.org/content/340/6139/1472>`_, 
(*iii*) a :ref:`digitized parcellation <economo_koskinas>` of the `von Economo and Koskinas cytoarchitectonic map <https://www.karger.com/Article/Abstract/103258>`_, and 
(*iv*) :ref:`functional and structural connectivity data <hcp_connectivity>` from the `Human Connectome Project <http://www.humanconnectomeproject.org/>`_.

.. raw:: html

   <br>

Multiscale analytical workflows 🦾
--------------------------------------------------------
The **ENIGMA Toolbox** comprises two neural scales for the contextualization of findings: (*i*) using microscale properties, namely 
:ref:`gene expression <ep_genes>` and :ref:`cytoarchitecture <big_brain>`, and (*ii*) using macroscale network models, such as 
:ref:`regional hub susceptibility analysis <hubs_susceptibility>` and :ref:`disease epicenter mapping <epi_mapping>`. Moreover, our 
Toolbox includes non-parametric :ref:`spatial permutation models <spin_perm>` to assess statistical significance while preserving 
the spatial autocorrelation of parcellated brain maps. From these comprehensive workflows, users can gain a deeper understanding 
of the molecular, cellular, and macroscale network organization of the healthy and diseased brains.

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
hesitate to post them to our `mailing list <https://groups.google.com/g/enigma-toolbox>`_! Are you interested in collaborating 
or sharing your ENIGMA-related data/codes/tools? `Noice <https://www.urbandictionary.com/define.php?term=noice>`_! 
Make sure you familiarize yourself with our `contributing guidelines <https://github.com/MICA-MNI/ENIGMA/blob/master/CONTRIBUTING.md>`_ 
first and then discuss your ideas on our Github `issues <https://github.com/MICA-MNI/ENIGMA/issues>`_ and 
`pull request <https://github.com/MICA-MNI/ENIGMA/pulls>`_.

.. raw:: html

   <br>


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
   pages/04.crossdisorder/index


.. toctree::
   :maxdepth: 1
   :hidden:
   :caption: Compatibility with other datasets 

   pages/16.import/index
   pages/17.parcellate_vw/index
   pages/18.export/index


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