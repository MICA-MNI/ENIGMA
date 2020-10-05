.. _epi_mapping:

.. title:: Epicenter mapping

Epicenter mapping
======================================

This page contains descriptions and examples to identify disease epicenters!


Cortical epicenters
---------------------
Using the :ref:`HCP connectivity data <hcp_connectivity>`, we can also identify epicenters of cortical atrophy.
This is done by systematically correlating every cortical region's seed-based connectivity profile (*i.e.*, cortico-cortical connectivity) with 
a whole-brain atrophy map. Disease epicenters thus represent regions whose connectivity profile 
spatially resembles the disease-related atrophy map. In this tutorial, our *atrophy map* will be 
derived from cortical thickness decreases in individuals with left TLE.


.. admonition:: Epicenters? 🤔

     Cortical and subcortical epicenter regions are identified if their connectivity profiles correlate with a disease-specific *cortical* atrophy map. 
     In the following examples, regions with strong *negative* correlations represent disease epicenters. Moreover, and regardless of its atrophy level, 
     a cortical or subcortical region can be an epicenter if it is (*i*) strongly connected to other high-atrophy cortical regions and (*ii*) weakly connected 
     to low-atrophy cortical regions. 

.. parsed-literal:: 

    **Prerequisites**
    ↪ Load :ref:`summary statistics <load_sumstats>` **or** :ref:`example data <load_example_data>`
    ↪ :ref:`Z-score data <zscore_data>` (*individual site/mega-analysis data only*)
    ↪ Load :ref:`cortico-cortical connectivity matrices <load_corticocortical>` 

.. tabs::

   .. code-tab:: py **Python** | meta
     
        >>> import numpy as np
        >>> from enigmatoolbox.utils.parcellation import parcel_to_surface
        >>> from enigmatoolbox.plotting import plot_cortical

        >>> # Identify cortical epicenters (from functional connectivity)
        >>> fc_ctx_epi = []
        >>> for seed in range(fc_ctx.shape[0]):
        ...     seed_con = fc_ctx[:, seed]
        ...     fc_ctx_epi = np.append(fc_ctx_epi, np.corrcoef(seed_con, CT_d)[0, 1])

        >>> # Identify cortical epicenters (from structural connectivity)
        >>> sc_ctx_epi = []
        >>> for seed in range(sc_ctx.shape[0]):
        ...     seed_con = sc_ctx[:, seed]
        ...     sc_ctx_epi = np.append(sc_ctx_epi, np.corrcoef(seed_con, CT_d)[0, 1])


        >>> # Project the results on the surface brain
        >>> plot_cortical(array_name=parcel_to_surface(fc_ctx_epi, 'aparc_fsa5'), surface_name="fsa5", size=(800, 400),
        ...               cmap='Reds_r', color_bar=True, color_range=(-0.5, -0.2))

        >>> plot_cortical(array_name=parcel_to_surface(sc_ctx_epi, 'aparc_fsa5'), surface_name="fsa5", size=(800, 400),
        ...               cmap='Blues_r', color_bar=True, color_range=(-0.5, 0))

   .. code-tab:: matlab **Matlab** | meta

        % Add the path to the ENIGMA TOOLBOX matlab folder
        addpath(genpath('/path/to/ENIGMA/matlab/'));

        % Identify cortical epicenters (from functional connectivity)
        fc_ctx_epi              = zeros(size(fc_ctx, 1), 1);
        fc_ctx_epi_p            = zeros(size(fc_ctx, 1), 1);
        for seed = 1:size(fc_ctx, 1)
            seed_conn           = fc_ctx(:, seed);
            r_tmp               = corrcoef(seed_conn, CT_d);
            fc_ctx_epi(seed)    = r_tmp(1, 2);
            fc_ctx_epi_p(seed)  = spin_test(seed_conn, CT_d, 'fsa5', ...
                                           'aparc', 1000, 'pearson');
        end

        % Identify cortical epicenters (from structural connectivity)
        sc_ctx_epi              = zeros(size(sc_ctx, 1), 1);
        sc_ctx_epi_p            = zeros(size(sc_ctx, 1), 1);
        for seed = 1:size(sc_ctx, 1)
            seed_conn           = sc_ctx(:, seed);
            r_tmp               = corrcoef(seed_conn, CT_d);
            sc_ctx_epi(seed)    = r_tmp(1, 2);
            sc_ctx_epi_p(seed)  = spin_test(seed_conn, CT_d, 'fsa5', ...
                                           'aparc', 1000, 'pearson');
        end

        % Project the results on the surface brain
        f = figure,
            plot_cortical(parcel_to_surface(fc_ctx_epi, 'aparc_fsa5'), 'fsa5', 'functional cortical epicenters')
            colorbar_range([-0.5 -0.2])
            colormap(flipud(Reds))

        f = figure,
            plot_cortical(parcel_to_surface(sc_ctx_epi, 'aparc_fsa5'), 'fsa5', 'structural cortical epicenters')
            colorbar_range([-0.5 0])
            colormap(flipud(Blues))

   .. tab:: ⤎ ⤏

          | ⤎ If you have **meta**-analysis data (*e.g.*, summary statistics)
          | ⤏ If you have individual site or **mega**-analysis data

   .. code-tab:: py **Python** | mega
       
        >>> import numpy as np
        >>> from enigmatoolbox.utils.parcellation import parcel_to_surface
        >>> from enigmatoolbox.plotting import plot_cortical

        >>> # Identify cortical epicenters
        >>> fc_ctx_epi = []
        >>> for seed in range(fc_ctx.shape[0]):
        ...     seed_con = fc_ctx[:, seed]
        ...     fc_ctx_epi = np.append(fc_ctx_epi, np.corrcoef(seed_con, ct_tle)[0, 1])

        >>> sc_ctx_epi = []
        >>> for seed in range(sc_ctx.shape[0]):
        ...     seed_con = sc_ctx[:, seed]
        ...     sc_ctx_epi = np.append(sc_ctx_epi, np.corrcoef(seed_con, ct_tle)[0, 1])


        >>> # And project the results on the surface brain
        >>> plot_cortical(array_name=parcel_to_surface(fc_ctx_epi, 'aparc_fsa5'), surface_name="fsa5", size=(800, 400),
        ...               cmap='Reds_r', color_bar=True, color_range=(-0.5, 0))

        >>> plot_cortical(array_name=parcel_to_surface(sc_ctx_epi, 'aparc_fsa5'), surface_name="fsa5", size=(800, 400),
        ...               cmap='Blues_r', color_bar=True, color_range=(-0.5, 0))


   .. code-tab:: matlab **Matlab** | mega

        % Add the path to the ENIGMA TOOLBOX matlab folder
        addpath(genpath('/path/to/ENIGMA/matlab/'));

        % Functional cortical epicenters 
        fc_ctx_epi             = zeros(size(fc_ctx, 1), 1); % 68 x 1
        for seed = 1:size(fc_ctx, 1)
            seed_conn          = fc_ctx(:, seed);
            r_tmp              = corrcoef(transpose(seed_conn), ct_tle);
            fc_ctx_epi(seed)   = r_tmp(1, 2);
        end

        sc_ctx_epi             = zeros(size(sc_ctx, 1), 1); % 68 x 1
        for seed = 1:size(sc_ctx, 1)
            seed_conn          = sc_ctx(:, seed);
            r_tmp              = corrcoef(transpose(seed_conn), ct_tle);
            sc_ctx_epi(seed)   = r_tmp(1, 2);
        end


        % Functional cortical epicenters
        f = figure,
            plot_cortical(parcel_to_surface(fc_ctx_epi, 'aparc_fsa5'), 'fsa5', 'functional cortical epicenters')
            colorbar_range([-0.5 0])
            colormap(flipud(Reds))

        f = figure,
            plot_cortical(parcel_to_surface(sc_ctx_epi, 'aparc_fsa5'), 'fsa5', 'structural cortical epicenters')
            colorbar_range([-0.5 0])
            colormap(flipud(Blues))

.. image:: ./examples/example_figs/epi_ctx.png
    :align: center


|


Subcortical epicenters
-------------------------
To identify subcortical epicenters of cortical atrophy, we once again correlate every subcortical region's seed-based 
connectivity profile (*e.g.*, subcortico-cortical connectivity) with 
a whole-brain cortical atrophy map. As above, our *atrophy map* will be 
derived from cortical thickness decreases in individuals with left TLE.

.. parsed-literal:: 

    **Prerequisites**
    ↪ Load :ref:`summary statistics <load_sumstats>` **or** :ref:`example data <load_example_data>`
    ↪ :ref:`Z-score data <zscore_data>` (*individual site/mega-analysis data only*)
    ↪ Load :ref:`subcortico-cortical connectivity matrices <load_subcorticocortical>` 

.. tabs::

   .. code-tab:: py **Python** | meta
     
        >>> import numpy as np
        >>> from enigmatoolbox.plotting import plot_subcortical

        >>> # Identify subcortical epicenters
        >>> fc_sctx_epi = []
        >>> for seed in range(fc_sctx.shape[0]):
        ...     seed_con = fc_sctx[seed, :]
        ...     fc_sctx_epi = np.append(fc_sctx_epi, np.corrcoef(seed_con, CT_d)[0, 1])

        >>> sc_sctx_epi = []
        >>> for seed in range(sc_sctx.shape[0]):
        ...     seed_con = sc_sctx[seed, :]
        ...     sc_sctx_epi = np.append(sc_sctx_epi, np.corrcoef(seed_con, CT_d)[0, 1])

        >>> # And project the results on the surface brain
        >>> plot_subcortical(fc_sctx_epi, ventricles=False, size=(800, 400),
        ...                  cmap='Reds_r', color_bar=True, color_range=(-0.5, -0.2))

        >>> plot_subcortical(sc_sctx_epi, ventricles=False, size=(800, 400),
        ...                  cmap='Blues_r', color_bar=True, color_range=(-0.5, 0))

   .. code-tab:: matlab **Matlab** | meta

          ello

   .. tab:: ⤎ ⤏

          | ⤎ If you have **meta**-analysis data (*e.g.*, summary statistics)
          | ⤏ If you have individual site or **mega**-analysis data

   .. code-tab:: py **Python** | mega

        >>> import numpy as np
        >>> from enigmatoolbox.plotting import plot_subcortical

        >>> # Identify subcortical epicenters
        >>> fc_sctx_epi = []
        >>> for seed in range(fc_sctx.shape[0]):
        ...     seed_con = fc_sctx[seed, :]
        ...     fc_sctx_epi = np.append(fc_sctx_epi, np.corrcoef(seed_con, ct_tle)[0, 1])

        >>> sc_sctx_epi = []
        >>> for seed in range(sc_sctx.shape[0]):
        ...     seed_con = sc_sctx[seed, :]
        ...     sc_sctx_epi = np.append(sc_sctx_epi, np.corrcoef(seed_con, ct_tle)[0, 1])

        >>> # And project the results on the surface brain
        >>> plot_subcortical(fc_sctx_epi, ventricles=False, size=(800, 400),
        ...                  cmap='Reds_r', color_bar=True, color_range=(-0.5, 0))

        >>> plot_subcortical(sc_sctx_epi, ventricles=False, size=(800, 400),
        ...                  cmap='Blues_r', color_bar=True, color_range=(-0.5, 0))

   .. code-tab:: matlab **Matlab** | mega

        %% Add the path to the ENIGMA TOOLBOX matlab folder
        addpath(genpath('/path/to/ENIGMA/matlab/'));

        %% 1 - Let's start by loading our example data
        % Here we need the covariates and the cortical thickness data
        [cov, ~, metr2_CortThick, ~] = load_example_data();


        %% 2 - We can then and z-score data in patients relative to controls, so that lower values
        %      correspond to greater atrophy
        % Z-score patients' data relative to controls (lower z-score = more atrophy)
        group        = cov.Dx;
        controlCode  = 0;
        ct           = zscore_matrix(metr2_CortThick(:, 2:end-5), group, controlCode);

        % Mean z-score values across individuals with left TLE (SDx == 3)
        ct_tle       = mean(ct(find(cov.SDx == 3), :), 1);


        %% 3 - Let's then load our functional and structural connectivity matrices
        % Load functional and structural cortico-cortical connectivity data (for simplicity, we won't load the regions' labels)
        [~, ~, fc_sctx, ~]   = load_fc();
        [~, ~, sc_sctx, ~]   = load_sc();


        %% 4 - Functional/structural subcortical disease epicenters
        %      Correlations between seed-based connectivity (looping over
        %      all subcortical regions) and cortical thickness decreases in left TLE
        % Functional subcortical epicenters
        fc_sctx_epi            = zeros(size(fc_sctx, 1), 1); % 14 x 1
        for seed = 1:size(fc_sctx, 1)
            seed_conn          = fc_sctx(seed, :);
            r_tmp              = corrcoef(transpose(seed_conn), ct_tle);
            fc_sctx_epi(seed)  = r_tmp(1, 2);
        end

        % Structural subcortical epicenters
        sc_sctx_epi            = zeros(size(sc_sctx, 1), 1); % 14 x 1
        for seed = 1:size(sc_sctx, 1)
            seed_conn          = sc_sctx(seed, :);
            r_tmp              = corrcoef(transpose(seed_conn), ct_tle);
            sc_sctx_epi(seed)  = r_tmp(1, 2);
        end


        %% 5 - Project our findings onto subcortical surfaces
        % Functional subcortical epicenters
        f = figure,
            plot_subcortical(fc_sctx_epi, 'False', 'functional subcortical epicenters')
            colorbar_range([-0.5 0])
            colormap(flipud(Reds))

        % Structural subcortical epicenters
        f = figure,
            plot_subcortical(sc_sctx_epi, 'False', 'structural subcortical epicenters')
            colorbar_range([-0.5 0])
            colormap(flipud(Blues))

.. image:: ./examples/example_figs/epi_sctx.png
    :align: center
