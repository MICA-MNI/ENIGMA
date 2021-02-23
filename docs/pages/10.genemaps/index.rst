.. _gene_maps:

.. title:: Gene expression data

Gene expression data
======================================

This page contains descriptions and examples to load gene expression data.


Fetch gene expression data
--------------------------------------
The **ENGMA TOOLBOX** provides microarray expression data obtained from the `Allen Human Brain Atlas <https://human.brain-map.org/>`_.
Following the examples below, we can fetch microarray expression data.


.. admonition:: Wanna know where we got those genes? 👖

     The Allen Human Brain Atlas microarray expression data loaded as part of the **ENIGMA TOOLBOX** was originally
     fetched from the `abagen <https://github.com/rmarkello/abagen>`_ toolbox using the ``abagen.get_expression_data()``
     command, using data from *all* donors. We then re-organized the rows (corresponding to region labels) to match the order 
     used in ENIGMA-derived data matrices. For more flexibility, check out their toolbox!

.. admonition:: Got NaNs? 🥛

     Please note that two regions (right frontal pole and right temporal pole) in the Desikan-Killiany atlas were 
     not matched to any tissue sample and thus are filled with NaN values in the data matrix.

.. admonition:: Slow internet connection? 🐌

     The command ``fetch_ahba()`` fetches a large (~24 MB) microarray dataset from the internet and may thus be 
     incredibly slow to load if you lack a good connection. But don't you worry: you can download the
     relevant file by typing this command in your terminal ``wget https://github.com/saratheriver/enigma-extra/raw/master/ahba/allgenes_stable_r0.2.csv``
     and specifying its path in the ``fetch_ahba()`` function as follows:``fetch_ahba('/path/to/allgenes_stable_r0.2.csv')``

.. _fetch_genes:

.. tabs::

   .. code-tab:: py
       
        >>> from enigmatoolbox.datasets import fetch_ahba

        >>> # Fetch gene expression data
        >>> genes = fetch_ahba()

        >>> # Obtain region labels
        >>> reglabels = genes['label']

        >>> # Obtain gene labels
        >>> genelabels = list(genes.columns)[1]

   .. code-tab:: matlab

        % Fetch gene expression data
        genes = fetch_ahba();

        % Obtain region labels
        reglabels = genes.label;

        % Obtain gene labels
        genelabels = genes.Properties.VariableNames(2:end);  

.. image:: ./examples/example_figs/gx.png
    :align: center


