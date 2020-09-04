.. _epi_mapping:

.. title:: Epicenter mapping! 📍

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


.. admonition:: Epicenter whaaat? 🤔

     Cortical and subcortical epicenter regions are identified if their connectivity profiles correlate with a disease-specific *cortical* atrophy map. 
     In the following examples, regions with strong *negative* correlations represent disease epicenters. Moreover, and regardless of its atrophy level, 
     a cortical or subcortical region can be an epicenter if it is (*i*) strongly connected to other high-atrophy cortical regions and (*ii*) weakly connected 
     to low-atrophy cortical regions. 


.. admonition:: Long code alert 🚨

     For completeness, we include code that has been detailed elsewhere (:ref:`loading example data <load_ct>`,
     :ref:`z-scoring and visualizing cortical surface data <surf_visualization>`). 
     If you're already comfortable with these steps, feel free to simply skip right to the last two sections!


.. tabs::

   .. code-tab:: py
       
        >>> ...


   .. code-tab:: matlab

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
        [fc_ctx, ~, ~, ~]   = load_fc();
        [sc_ctx, ~, ~, ~]   = load_sc();


        %% 4 - Functional/structural cortical disease epicenters
        %      Correlations between seed-based connectivity (looping over
        %      all cortical regions) and cortical thickness decreases in left TLE 
        % Functional cortical epicenters 
        fc_ctx_epi             = zeros(size(fc_ctx, 1), 1); % 68 x 1
        for seed = 1:size(fc_ctx, 1)
            seed_conn          = fc_ctx(:, seed);
            r_tmp              = corrcoef(transpose(seed_conn), ct_tle);
            fc_ctx_epi(seed)   = r_tmp(1, 2);
        end

        % Structural cortical epicenters 
        sc_ctx_epi             = zeros(size(sc_ctx, 1), 1); % 68 x 1
        for seed = 1:size(sc_ctx, 1)
            seed_conn          = sc_ctx(:, seed);
            r_tmp              = corrcoef(transpose(seed_conn), ct_tle);
            sc_ctx_epi(seed)   = r_tmp(1, 2);
        end


        %% 5 - Project our findings onto cortical surfaces
        % Functional cortical epicenters
        f = figure,
            plot_cortical(parcel_to_surface(fc_ctx_epi, 'aparc_fsa5'), 'fsa5', 'functional cortical epicenters')
            colorbar_range([-0.5 0])
            colormap(flipud(Reds))

        % Structural cortical epicenters
        f = figure,
            plot_cortical(parcel_to_surface(sc_ctx_epi, 'aparc_fsa5'), 'fsa5', 'structural cortical epicenters')
            colorbar_range([-0.5 0])
            colormap(flipud(Blues))


|


Subcortical epicenters
-------------------------
To identify subcortical epicenters of cortical atrophy, we once again correlate every subcortical region's seed-based 
connectivity profile (*e.g.*, subcortico-cortical connectivity) with 
a whole-brain cortical atrophy map. As above, our *atrophy map* will be 
derived from cortical thickness decreases in individuals with left TLE.

.. admonition:: Long code alert 🚨

     For completeness, we include code that has been detailed elsewhere (:ref:`loading example data <load_ct>`,
     :ref:`z-scoring and visualizing cortical surface data <surf_visualization>`). Sections 1-3 are identical to 
     the above example for identifying cortical epicenters.
     If you're already comfortable with these steps, feel free to simply skip right to the last two sections!

.. tabs::

   .. code-tab:: py

        >>> ...

   .. code-tab:: matlab

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
        %      all cortical regions) and cortical thickness decreases in left TLE
        % Functional cortical epicenters
        fc_sctx_epi            = zeros(size(fc_sctx, 1), 1); % 14 x 1
        for seed = 1:size(fc_sctx, 1)
            seed_conn          = fc_sctx(seed, :);
            r_tmp              = corrcoef(transpose(seed_conn), ct_tle);
            fc_sctx_epi(seed)  = r_tmp(1, 2);
        end

        % Structural cortical epicenters
        sc_sctx_epi            = zeros(size(sc_sctx, 1), 1); % 68 x 1
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

