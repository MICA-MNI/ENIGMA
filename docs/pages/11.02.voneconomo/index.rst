.. _economo_koskinas:

.. title:: Cytoarchitectonics

Economo-Koskinas cytoarchitectonics
==================================================

This page contains descriptions and examples to stratify and visualize surface-based findings according to cyatoarchitectural variation. 

.. _ve_classes:

Economo-Koskinas stratification
--------------------------------------
As part of the **ENIGMA TOOLBOX**, we included a digitized parcellation of `von Economo and Koskina’s cytoarchitectonic 
mapping of the human cerebral cortex <https://www.karger.com/Article/Abstract/103258>`_, from which five different structural types of cerebral cortex can be described: 
*i*) **agranular** (*purple*; thick with large cells but sparse layers II and IV), *ii*) **frontal** (*blue*; thick but not rich in cellular substance, 
visible layers II and IV), *iii*) **parietal** (*green*; thick and rich in cells with dense layers II and IV but small and slender pyramidal 
cells), *iv*) **polar** (*orange*; thin but rich in cells, particularly in granular layers), and *v*) **granular** or koniocortex (*yellow*; thin but rich 
in smalls cells, even in layer IV, and a rarified layer V).

.. image:: ./examples/example_figs/orig_atlas.png
    :align: center

In the following example, we contextualized disease-related cortical atrophy patterns with respect to the 
well-established von Economo and Koskinas cytoarchitectonic atlas by summarizing cortex-wide effects across each
of the five structural types of isocortex. To ease interpretation, stratification of findings based on the von Economo and Koskinas 
atlas are also visualized in a spider plot. Here, negative values (towards the center) represent
greater atrophy in disease cases relative to healthy controls.

.. parsed-literal:: 

     **Prerequisites**
     ↪ Load :ref:`summary statistics <load_sumstats>` **or** :ref:`example data <load_example_data>`
     ↪ :ref:`Z-score data <zscore_data>` (*mega only*)

.. tabs::

   .. code-tab:: py **Python** | meta

        >>> from enigmatoolbox.histology import economo_koskinas_spider

        >>> # Stratify cortical atrophy based on Economo-Koskinas classes
        >>> class_mean = economo_koskinas_spider(CT_d, axis_range=(-0.4, 0))
     
   .. code-tab:: matlab **Matlab** | meta

        % Stratify cortical atrophy based on Economo-Koskinas classes
        class_mean = economo_koskinas_spider(CT_d, 'axis_range', [-0.4 0])

   .. tab:: ⤎ ⤏

          | ⤎ If you have **meta**-analysis data (*e.g.*, summary statistics)
          | ⤏ If you have individual site or **mega**-analysis data

   .. code-tab:: py **Python** | mega

        >>> from enigmatoolbox.histology import economo_koskinas_spider
        
        >>> # Stratify cortical atrophy based on Economo-Koskinas classes
        >>> class_mean = economo_koskinas_spider(CT_z_mean, axis_range=(-1, 0))

   .. code-tab:: matlab **Matlab** | meta

        % Stratify cortical atrophy based on Economo-Koskinas classes
        class_mean = economo_koskinas_spider(CT_z_mean{:, :}, 'axis_range', [-1 0])

.. image:: ./examples/example_figs/spider.png
    :align: center