.. _gene_maps:

Gene expression data
======================================

This page contains descriptions and examples to load gene expression data!


Fetch gene expression data
--------------------------------------
The **ENGMA TOOLBOX** provides microarray expression data obtained from the `Allen Human Brain Atlas <https://human.brain-map.org/>`_.
Following the examples below, we can fetch microarray expression data.


.. Note::
     The Allen Human Brain Atlas microarray expression data loaded as part of the **ENIGMA TOOLBOX** was originally
     fetched from the `abagen <https://github.com/rmarkello/abagen>`_ toolbox using the ``abagen.get_expression_data()``
     command, using data from *all* donors. We then re-organized the rows (corresponding to region labels) to match the order 
     used in ENIGMA-derived data matrices!

.. Note:: 
     Please also note that two regions (right frontal pole and right temporal pole) in the Desikan-Killiany atlas were 
     not matched to any tissue sample and thus are filled with NaN values in the data matrix.

.. Warning::
     The command ``fetch_ahba()`` fetches a large (~24 MB) microarray dataset from the internet and may thus be 
     incredibly slow to load if you lack a good connection. But don't you worry: you can download the
     relevant file by typing this command in your terminal ``wget https://raw.githubusercontent.com/saratheriver/enigma-extra/master/ahba/allgenes.csv``
     and specifying its path in the ``fetch_ahba()`` function as follows:``fetch_ahba('/path/to/allgenes.csv')``

.. tabs::

   .. code-tab:: py
       
        >>> from enigmatoolbox.datasets import fetch_ahba

        >>> # Fetch gene expression data (output of fetch_ahba() is a dataframe)
        >>> df = fetch_ahba()

        >>> # However, if you prefer to use numpy, you can also extract the data as follows:
        >>> genex = df.iloc[:, 1:].to_numpy()

        >>> # Obtain the region labels
        >>> reglabels = df.iloc[:,0].to_list()

        >>> # As well as the gene labels
        >>> glabels = df.columns.values[1:].tolist()

   .. code-tab:: matlab

        %% Fetch gene expression data
        %    gx          = matrix of gene expression data (82 x 15633)
        %    reglabels   = name of cortical regions in same order as gx
        %                  (82 x 1 cell array)
        %    genelabels  = name of genes in same order as gx
        %                  (1 x 15633 cell array)
        [gx, reglabels, genelabels] = fetch_ahba();  

.. image:: ./examples/example_figs/gx.png
    :align: center


