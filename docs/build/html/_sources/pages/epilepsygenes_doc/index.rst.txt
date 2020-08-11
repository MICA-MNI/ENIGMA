.. _ep_genes:

Disease-related gene expression maps
=========================================

This page contains descriptions and examples to extract GWAS-implicated gene expression data
and project them to cortical and subcortical surfaces!


Extract disease-related genes
-----------------------------------------
Leveraging findings from recent GWAS, we can extract gene expression maps for a set of pre-defined 
disease-related genes, including:
`attention deficit/hyperactivity disorder <https://www.nature.com/articles/s41588-018-0269-7>`_,
`autism spectrum disorder <https://www.nature.com/articles/s41588-019-0344-8>`_, 
`bipolar disorder <https://www.nature.com/articles/s41588-019-0397-8>`_, 
`depression <https://www.nature.com/articles/s41593-018-0326-7>`_,  
`common epilepsies <https://www.nature.com/articles/s41467-018-07524-z>`_,
`schizophrenia <https://www.nature.com/articles/s41588-018-0059-2>`_, and
`tourette's syndrome <https://ajp.psychiatryonline.org/doi/10.1176/appi.ajp.2018.18070857?url_ver=Z39.88-2003&rfr_id=ori:rid:crossref.org&rfr_dat=cr_pub%20%200pubmed>`_. 
In the following tutorial, we will use epilepsy-related genes (more specifically, genes related to focal 
hippocampal sclerosis) as an example, but feel free to replace *epilepsy* with any other disorder listed above!

.. Caution::
     Pre-defined gene sets are obtained from individual studies and are liable to be changed!
     We welcome any suggestions you may have on defining proper disease-related gene sets and are
     happy to expand this function to include other interesting disorders! Get in touch with us
     `here <https://github.com/saratheriver/ENIGMA/issues>`_!

.. tabs::

   .. code-tab:: py
       
        >>> from enigmatoolbox.datasets import fetch_ahba
        >>> from enigmatoolbox.datasets import risk_genes

        >>> # Let's start by loading the microarray expression data
        >>> gx = fetch_ahba()

        >>> # Get the names of genes associated with a specific epilepsy subtype (using Focal HS as example here)
        >>> # Other epilepsy subtypes include: 'allepilepsy', 'focalepilepsy', 'generalizedepilepsy', 'jme', and 'cae'
        >>> epigx = risk_genes("epilepsy")
        >>> fh_genes = epigx['focalhs']

        >>> # We can now extract the gene expression data for these Focal HS genes
        >>> fh_gx = gx[fh_genes]

   .. code-tab:: matlab

        %% add the path to the ENIGMA TOOLBOX matlab folder
        addpath(genpath('/path/to/ENIGMA/matlab/'));
        
        %% Let's start by loading the microarray expression data
        [gx, reglabels, genelabels] = fetch_ahba();

        %% Get the names of genes associated with a specific epilepsy subtype (using Focal HS as example here)
        % Other subtypes include: 'allepilepsy', 'focalepilepsy', 'generalizedepilepsy', 'jme', and 'cae'
        epigx        = risk_genes("epilepsy");
        fh_genes     = find(ismember(genelabels, epigx.focalhs));

        %% We can now extract the gene expression data for these Focal HS genes
        fh_gx        = gx(:, fh_genes);


|


Visualize disease-related gene expression maps
------------------------------------------------------------------------
Following up on the above example, we provide a brief example to project gene expression maps to the surface! 
Once again, we use Focal HS (epilepsy) genes as an example.
Additional details on surface visualization are provided in :ref:`this section <surf_visualization>` section!

.. tabs::

   .. code-tab:: py
       
        >>> import os
        >>> import numpy as np
        >>> import enigmatoolbox.datasets
        >>> from enigmatoolbox.utils.parcellation import map_to_labels
        >>> from enigmatoolbox.plotting import plot_cortical, plot_subcortical

        >>> # Following the above code, we can then map epilepsy-related gene expression to the cortical surface!
        >>> # Let's first compute the mean of all Focal HS genes across cortical areas only
        >>> fh_gx = np.mean(fh_gx, axis=1)

        >>> # And separate cortical (ctx) from subcortical (sctx) areas
        >>> fh_gx_ctx = np.mean(fh_gx, axis=1)[:68]
        >>> fh_gx_sctx = np.mean(fh_gx, axis=1)[68:]

        >>> # We can now compute the mapping between the parcellated gene expression data and our surface template
        >>> labeling = np.loadtxt(os.path.join(os.path.dirname(enigmatoolbox.datasets.__file__),
        ...            'parcellations', 'aparc_fsa5.csv'), dtype=np.int)
        >>> fh_gx_ctx_fsa5 = map_to_labels(fh_gx_ctx, labeling)

        >>> # And finally project the output to the cortical surface
        >>> plot_cortical(array_name=fh_gx_ctx_fsa5, surface_name="fsa5", size=(800, 400), nan_color=(1, 1, 1, 1),
        ...               cmap='Greys', color_bar=True, color_range=(0.4, 0.55))

        >>> # ... as well as to the subcortical surface!!
        >>> plot_subcortical(array_name=fh_gx_sctx, ventricles=False, size=(800, 400),
        ...                 cmap='Greys', color_bar=True, color_range=(0.4, 0.65))

   .. code-tab:: matlab

        %% Add the path to the ENIGMA TOOLBOX matlab folder
        addpath(genpath('/path/to/ENIGMA/matlab/'));

        %% Following the above code, we can then map epilepsy-related gene expression to the cortical surface!
        % Let's first compute the mean of all Focal HS genes
        mean_fh_gx           = mean(fh_gx, 2);

        % And separate cortical (ctx) from subcortical (sctx) areas
        fh_gx_ctx            = mean_fh_gx(1:68);
        fh_gx_sctx           = mean_fh_gx(69:end);

        %% We can now compute the mapping between the parcellated (cortex only) gene expression data and our surface template
        fh_gx_ctx_fsa5       = map_to_labels(fh_gx_ctx(1:68), 'aparc_fsa5.csv');

        %% Finally, we can project the output to the cortical surface
        f = figure,
          plot_cortical(fh_gx_ctx_fsa5, 'fsa5', 'focal hs-related gene expression')
          colormap([Greys])
          SurfStatColLim([.4 .55])
  
        %% ... as well as to the subcortical surface!!
        f = figure,
          plot_subcortical(fh_gx_sctx, 'False', 'focal hs-related gene expression')
          colormap([Greys])
          SurfStatColLim([.4 .65]) 

.. image:: ./examples/example_figs/epigx.png
    :align: center


