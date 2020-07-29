.. _gene_maps:

Gene expression data
======================================

This page contains descriptions and examples to load gene expression data!


Fetch gene expression data
--------------------------------------
The **ENGMA TOOLBOX** provides microarray expression data obtained from the `Allen Human Brain Atlas <https://human.brain-map.org/>`_.
Following the examples below, we can fetch microarray expression data and extract GWAS-implicated disease risk genes.


.. Note::
     The Allen Human Brain Atlas microarray expression data loaded as part of the **ENIGMA TOOLBOX** was originally
     fetched from the `abagen <https://github.com/rmarkello/abagen>`_ toolbox using the ``abagen.get_expression_data()``
     command, using data from *all* donors. We then re-organized the rows (corresponding to region labels) to match the order 
     used in ENIGMA-derived data matrices!

.. Note:: 
     Please also note that two regions (right frontal pole and right temporal pole) in the Desikan-Killiany atlas were 
     not matched to any tissue sample and thus are filled with NaN values in the data matrix.

.. tabs::

   .. code-tab:: py
       
        >>> ...


   .. code-tab:: matlab

        %% ...  




