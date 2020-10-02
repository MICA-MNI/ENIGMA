.. _hcp_connectivity:

.. title:: Load connectivity data

Connectivity data
==================================================

This page contains descriptions and examples to use HCP connectivity data!
For details on HCP participants and data processing, please see our manuscript entitled 
`Network-based atrophy modelling in the common epilepsies: a worldwide ENIGMA study <https://www.biorxiv.org/content/10.1101/2020.05.04.076836v1>`_


.. _load_corticocortical:

Load cortical connectivity matrices
----------------------------------------
The **ENIGMA TOOLBOX** provides structural (diffusion MRI) and functional 
(resting-state functional MRI) connectivity matrices obtained from the Human Connectome Project (HCP). 
Following the examples below, we can load connectivity data and extract seed-based connectivity. 

.. admonition:: Oh, by the way... ☝🏼

     Seed-based connectivity, as well as various connectivity metrics, can be easily mapped onto 
     the surface template! Simply follow our tutorial :ref:`here <surf_visualization>`!

.. tabs::

   .. code-tab:: py
       
        >>> from enigmatoolbox.datasets import load_sc, load_fc
        >>> from nilearn import plotting

        >>> # Load and plot cortical functional connectivity data
        >>> fc_ctx, fc_ctx_labels, _, _ = load_fc()
        >>> fc_plot = plotting.plot_matrix(fc_ctx, figure=(9, 9), labels=fc_ctx_labels, vmax=0.8, vmin=0, cmap='Reds')

        >>> # Load and plot cortical structural connectivity data
        >>> sc_ctx, sc_ctx_labels, _, _ = load_sc()
        >>> sc_plot = plotting.plot_matrix(sc_ctx, figure=(9, 9), labels=sc_ctx_labels, vmax=10, vmin=0, cmap='Blues')

        >>> # We can also extract seed-based connectivity! Let's pick the middle temporal gyrus as example seed:
        >>> seed = "L_middletemporal"
        >>> seed_conn_fc = fc_ctx[[i for i, item in enumerate(fc_ctx_labels) if seed in item],]   # extract FC row corresponding to the seed
        >>> seed_conn_sc = sc_ctx[[i for i, item in enumerate(sc_ctx_labels) if seed in item],]   # extract SC row corresponding to the seed


   .. code-tab:: matlab

        % Add the path to the ENIGMA TOOLBOX matlab folder
        addpath(genpath('/path/to/ENIGMA/matlab/'));

        % Load and plot functional connectivity data
        [fc_ctx, fc_ctx_labels, ~, ~] = load_fc();
        f = figure,
          imagesc(fc_ctx, [0 0.8]);                % change axis limits here
          colormap(Reds);                          % change colormap here
          colorbar;                                % display colorbar
          set(gca, 'YTick', 1:1:length(fc_ctx_labels), ...   
              'YTickLabel', fc_ctx_labels)         % display name of regions on y-axis

        % Load and plot structural connectivity data
        [sc_ctx, sc_ctx_labels, ~, ~] = load_sc();
        f = figure,
          imagesc(sc_ctx, [0 10]);                 % change axis limits here
          colormap(Blues);                         % change colormap here
          colorbar;                                % display colorbar
          set(gca, 'YTick', 1:1:length(sc_ctx_labels), ...   
              'YTickLabel', sc_ctx_labels)         % display name of regions on y-axis

        % We can also extract seed-based connectivity! Let's pick the middle temporal gyrus as example seed:
        seed = 'L_middletemporal'
        seed_conn_fc = fc_ctx(find(strcmp(fc_ctx_labels, seed)), :)   % extract FC row corresponding to the seed
        seed_conn_sc = sc_ctx(find(strcmp(sc_ctx_labels, seed)), :)   % extract SC row corresponding to the seed
     

.. image:: ./examples/example_figs/ctx_conn.png
    :align: center


|


.. _load_subcorticocortical:

Load subcortical connectivity matrices
-------------------------------------------
| Subcortico-cortical as well as subcortico-subcortical connectivity matrices are also included in the
 **ENIGMA TOOLBOX**! As above, we can load these structural and functional matrices and extract seed-based connectivity
 from subcortical seeds!

.. tabs::

   .. code-tab:: py

        >>> from enigmatoolbox.datasets import load_sc, load_fc
        >>> from nilearn import plotting

        >>> # Load and plot subcortical functional connectivity data
        >>> _, _, fc_sctx, fc_sctx_labels = load_fc()
        >>> fc_plot = plotting.plot_matrix(fc_sctx, figure=(9, 9), labels=fc_sctx_labels, vmax=0.5, vmin=0, cmap='Reds')

        >>> # Load and plot subcortical structural connectivity data
        >>> _, _, sc_sctx, sc_sctx_labels = load_sc()
        >>> sc_plot = plotting.plot_matrix(sc_sctx, figure=(9, 9), labels=sc_sctx_labels, vmax=10, vmin=0, cmap='Blues')

        >>> # As above, we can also extract seed-based connectivity! Here, we chose the left hippocampus as example seed:
        >>> seed = "Lhippo"
        >>> seed_conn_fc = fc_sctx[[i for i, item in enumerate(fc_sctx_labels) if seed in item],]   # extract FC row corresponding to the seed
        >>> seed_conn_sc = sc_sctx[[i for i, item in enumerate(sc_sctx_labels) if seed in item],]   # extract SC row corresponding to the seed


   .. code-tab:: matlab

        % Add the path to the ENIGMA TOOLBOX matlab folder
        addpath(genpath('/path/to/ENIGMA/matlab/'));

        % Load and plot functional connectivity data
        [~, ~, fc_sctx, fc_sctx_labels] = load_fc();
        f = figure,
          imagesc(fc_sctx, [0 0.5]);               % change axis limits here
          colormap(Reds);                          % change colormap here
          colorbar;                                % display colorbar
          set(gca, 'YTick', 1:1:length(fc_sctx_labels), ...   
              'YTickLabel', fc_sctx_labels)        % display name of regions on y-axis

        % Load and plot structural connectivity data
        [~, ~, sc_sctx, sc_sctx_labels] = load_sc();
        f = figure,
          imagesc(sc_sctx, [0 10]);                % change axis limits here
          colormap(Blues);                         % change colormap here
          colorbar;                                % display colorbar
          set(gca, 'YTick', 1:1:length(sc_sctx_labels), ...   
              'YTickLabel', sc_sctx_labels)        % display name of regions on y-axis

        % We can also extract seed-based connectivity! Let's pick the middle temporal gyrus as example seed:
        seed = 'Lhippo'
        seed_conn_fc = fc_sctx(find(strcmp(fc_sctx_labels, seed)), :)   % extract FC row corresponding to the seed
        seed_conn_sc = sc_sctx(find(strcmp(sc_sctx_labels, seed)), :)   % extract SC row corresponding to the seed


.. image:: ./examples/example_figs/sctx_conn.png
    :align: center