.. _ep_genes:

Epilepsy-related gene expression
=========================================

This page contains descriptions and examples to extract epilepsy-related gene expression data
and project them to cortical and subcortical surfaces!


Epilepsy-related gene expression maps
-----------------------------------------
Leveraging findings from a recent `GWAS <https://www.nature.com/articles/s41467-018-07524-z>`_ from the International 
League Against Epilepsy Consortium on Complex Epilepsies, we can extract gene expression maps for a set of pre-defined 
epilepsy-related genes! 

.. tabs::

   .. code-tab:: py
       
        >>> from enigmatoolbox.datasets import fetch_ahba
        >>> from enigmatoolbox.datasets import epilepsy_genes

        >>> # Let's start by loading the microarray expression data
        >>> gx = fetch_ahba()

        >>> # Get the names of genes associated with specific epilepsy subtypes (using Focal HS as example here)
        >>> # Other subtypes include: 'allepilepsy', 'focalepilepsy', 'generalizedepilepsy', 'jme', 'cae'
        >>> epigx = epilepsy_genes()
        >>> fh_genes = epigx['focalhs']

        >>> # We can now extract the gene expression data for these specifc genes
        >>> fh_gx = gx[fh_genes]

        >>> # Alternatively, we can also combine all dem epilepsy genes together (and removing duplicates)
        >>> allg = epigx['allepilepsy'] + epigx['focalepilepsy'] + epigx['generalizedepilepsy'] + epigx['jme'] + epigx['cae'] + epigx['focalhs']
        >>> allg = list(dict.fromkeys(allg))
        >>> allgx = gx[allg]

   .. code-tab:: matlab

        %% add the path to the ENIGMA TOOLBOX matlab folder
        addpath(genpath('/path/to/ENIGMA/matlab/'));
        
        %% Let's start by loading the microarray expression data
        [gx, reglabels, genelabels] = fetch_ahba();

        %% Get the names of genes associated with specific epilepsy subtypes (using Focal HS as example here)
        % Other subtypes include: 'allepilepsy', 'focalepilepsy', 'generalizedepilepsy', 'jme', 'cae'
        epigx        = epilepsy_genes();
        fh_genes     = find(ismember(genelabels, epigx.focalhs));

        %% We can now extract the gene expression data for these specifc genes
        fh_gx        = gx(:, fh_genes);

        %% Alternatively, we can also combine all dem epilepsy genes together (and removing duplicates)
        allg         = unique([epigx.allepilepsy epigx.focalepilepsy epigx.generalizedepilepsy ...
                               epigx.jme epigx.cae epigx.focalhs]);
        all_genes    = find(ismember(genelabels, allg));    
        allgx        = gx(:, all_genes);


|


Visualize epilepsy-related gene expression patterns
------------------------------------------------------------------------
Following up on the above example, we provide a brief example to project gene expression maps to the surface!
Additional details are provided in the :ref:`surface visualization <surf_visualization>` section!

.. tabs::

   .. code-tab:: py
       
        >>> import os
        >>> import numpy as np
        >>> import enigmatoolbox.datasets
        >>> from enigmatoolbox.utils.parcellation import map_to_labels
        >>> from enigmatoolbox.plotting import plot_cortical, plot_subcortical

        >>> # Following the above code, we can then map epilepsy-related gene expression to the cortical surface!
        >>> labeling = np.loadtxt(os.path.join(os.path.dirname(enigmatoolbox.datasets.__file__),
        ...            'parcellations', 'aparc_fsa5.csv'), dtype=np.int)
        >>> fh_gx_fsa5 = map_to_labels(np.mean(fh_gx, axis=1)[:68], labeling)
        >>> plot_cortical(array_name=fh_gx_fsa5, surface_name="fsa5", size=(800, 400), nan_color=(1, 1, 1, 1),
        ...               cmap='Greys', color_bar=True, color_range=(0.4, 0.55))

        >>> # And to the subcortical surface!!
        >>> plot_subcortical(array_name=np.mean(fh_gx, axis=1)[68:], ventricles=False, size=(800, 400),
        ...                 cmap='Greys', color_bar=True, color_range=(0.4, 0.65))


   .. code-tab:: matlab

        %% add the path to the ENIGMA TOOLBOX matlab folder
        addpath(genpath('/path/to/ENIGMA/matlab/'));

        %% Following the above code, we can then map epilepsy-related gene expression to the cortical surface!
        mean_fh_gx           = mean(fh_gx, 2);
        fh_gx_fsa5           = map_to_labels(mean_fh_gx(1:68), 'aparc_fsa5.csv');

        f = figure,
          plot_cortical(fh_gx_fsa5, 'fsa5', 'focal hs-related gene expression')
          colormap([Greys])
          SurfStatColLim([.4 .55])
  
        %% And to the subcortical surface!!
        f = figure,
          plot_subcortical(mean_fh_gx(69:end), 'False', 'focal hs-related gene expression')
          colormap([Greys])
          SurfStatColLim([.4 .65]) 

.. image:: ./examples/example_figs/epigx.png
    :align: center


