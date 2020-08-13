.. _surf_visualization:

Surface data visualization
======================================

This page contains descriptions and examples to visualize surface data!


Cortical surface visualization
-----------------------------------
**ENIGMA TOOLBOX** comes equipped with fsaverage5 and Conte69 cortical midsurfaces and numerous parcellations!   
Following the examples below, we can easily map parcellated data (*e.g.*, Desikan-Killiany) to fsaverage5 surface space (*i.e.*, vertices).
In the following example, we will display mean subcortical volume reductions in individuals with left TLE (*z*-scored to healthy controls).

.. admonition:: Parcellations, parcellations for everyone

     Mapping parcellated data to the surface has never been easier - even for ENIGMA datasets (yes, those datasets with 68, as opposed to 71, Desikan-
     Killiany cortical parcels). Our ``parcel_to_surface()`` function works with ENIGMA- and non-ENIGMA-derived datasets. We also included several
     other parcellations (*e.g.*, glasser_fsa5, schaefer_100_fsa5, schaefer_200_fsa5, schaefer_300_fsa5, and so on ...), so you can take advantage of
     our visualization tools for all your other projects!

.. admonition:: Don't like fsaverage5? Relax, we got you covered!

     The same approach can be used to map parcellated data to the Conte69 surface template; simply replace every instance of 'fsa5' with 'conte69'!
     Easy peasy lemon squeezy 🍋

.. tabs::

   .. code-tab:: py
       
        >>> import numpy as np
        >>> from enigmatoolbox.datasets import load_example_data
        >>> from enigmatoolbox.utils.useful import zscore_matrix
        >>> from enigmatoolbox.utils.parcellation import parcel_to_surface
        >>> from enigmatoolbox.plotting import plot_cortical

        >>> # Let's first load our example data. Here we only need the covariates and the cortical thickness data
        >>> cov, _, metr2_CortThick, _ = load_example_data()

        >>> # We can z-score the data in patients relative to controls (lower z-score = more atrophy)
        >>> data = metr2_CortThick.iloc[:, 1:-5]            # Selecting only columns with cortical thickness values
        >>> group = cov['Dx'].to_list()                     # Selecting the group assignment column for all participants
        >>> controlCode = 0                                 # Specifying that controls are coded as 0
        >>> Z = zscore_matrix(data, group, controlCode)

        >>> # As a quick example, let's choose data from individuals with left TLE
        >>> Z_TLE = np.mean(Z.to_numpy()[cov[cov['SDx'] == 3].index, :], axis=0)   # Mean z-score values for left TLE patients (SDx == 3)

        >>> # Before visualizing the data, we need to map the parcellated data to the surface
        >>> Z_TLE_fsa5 = parcel_to_surface(Z_TLE, 'aparc_fsa5')

        >>> # We can now project cortical thickness descreases in left TLE to the cortical surface!
        >>> plot_cortical(array_name=Z_TLE_fsa5, surface_name="fsa5", size=(800, 400),
        ...               cmap='Blues_r', color_bar=True, color_range=(-2, 0))

   .. code-tab:: matlab

        %% Add the path to the ENIGMA TOOLBOX matlab folder
        addpath(genpath('/path/to/ENIGMA/matlab/'));

        %% Let's first load our example data. Here we only need the covariates and the cortical thickness data
        [cov, ~, metr2_CortThick, ~] = load_example_data();

        %% We can z-score the data in patients relative to controls (lower z-score = more atrophy)
        data           = metr2_CortThick(:, 2:end-5);         % Selecting only columns with cortical thickness values
        group          = cov.Dx;                              % Selecting the group assignment column for all participants
        controlCode    = 0;                                   % Specifying that controls are coded as 0
        Z              = zscore_matrix(data, group, controlCode);
        
        %% As a quick example, let's choose data from individuals with left TLE
        Z_TLE          = mean(Z(find(cov.SDx == 3), :), 1);   % Mean z-score values for left TLE patients (SDx == 3)

        %% Before visualizing the data, we need to map the parcellated data to the surface
        Z_TLE_fsa5   = parcel_to_surface(Z_TLE, 'aparc_fsa5');

        %% Plot cortical values
        f = figure,
            plot_cortical(Z_TLE_fsa5, 'fsa5')
            colormap(flipud(Blues));                          % change colormap here 
            SurfStatColLim([-2, 0])                           % change colorbar limits here

.. image:: ./examples/example_figs/ctx_py.png
    :align: center


|


Subcortical surface visualization
---------------------------------------
The **ENIGMA TOOLBOX**'s subcortical viewer includes 16 segmented subcortical structures obtained from the Desikan-Killiany atlas (aparc+aseg.mgz). 
Subcortical regions include bilateral accumbens, amygdala, caudate, hippocampus, pallidum, putamen, thalamus, and ventricles. In the following example,
we will display subcortical volume reductions (*z*-scored to healthy controls) in individuals with left TLE.

.. admonition:: We've mentioned this already, but don't forget that...

     Subcortical input values are ordered as follows: left-accumbens, left-amygdala, left-caudate, left-hippocampus, 
     left-pallidum, left-putamen, left-thalamus, left-ventricles, right-accumbens, right-amygdala, right-caudate, right-hippocampus, 
     right-pallidum, right-putamen, right-thalamus, right-ventricles! You can re-order your subcortical dataset using our ``reorder_sctx()`` function! 
     \*Ventricles are optional.


.. tabs::

   .. code-tab:: py

        >>> import numpy as np
        >>> from enigmatoolbox.datasets import load_example_data
        >>> from enigmatoolbox.utils.useful import zscore_matrix, reorder_sctx
        >>> from enigmatoolbox.plotting import plot_subcortical

        >>> # Let's first load our example data; here we only need the covariates and the subcortical volumes
        >>> cov, metr1_SubVol, _, _ = load_example_data()

        >>> # After loading our subcortical data, we must re-order them (alphabetically and by hemisphere) as a requisite for plot_subcortical!
        >>> metr1_SubVol_r = reorder_sctx(metr1_SubVol)

        >>> # Let's also z-score the data in patients, relative to controls, so that lower z-score indexes more atrophy
        >>> data = metr1_SubVol_r.iloc[:, 1:-1]             # Selecting only columns with subcortical volume values
        >>> group = cov['Dx'].to_list()                     # Selecting the group assignment column for all participants
        >>> controlCode = 0                                 # Specifying that controls are coded as 0
        >>> Z = zscore_matrix(data, group, controlCode)

        >>> # As a quick example, let's project data from individuals with left TLE to the subcortical surface template
        >>> Z_LTLE = np.mean(Z.to_numpy()[cov[cov['SDx'] == 3].index, :], axis=0)   # Mean z-score values for left TLE patients (SDx == 3)
        >>> plot_subcortical(array_name=Z_LTLE, size=(800, 400),
        >>>                  cmap='Blues_r', color_bar=True, color_range=(-3, 0))

   .. code-tab:: matlab

        %% Add the path to the ENIGMA TOOLBOX matlab folder
        addpath(genpath('/path/to/ENIGMA/matlab/'));

        %% Let's first load our example data; here we only need the covariates and the subcortical volumes
        [cov, metr1_SubVol, ~, ~] = load_example_data();

        %% After loading our subcortical data, we must re-order them (alphabetically and by hemisphere) as a requisite for plot_subcortical!
        metr1_SubVol_r = reorder_sctx(metr1_SubVol);

        %% Let's also z-score the data in patients, relative to controls, so that lower z-score indexes more atrophy
        data           = metr1_SubVol_r(:, 2:end-1);   % Selecting only columns with subcortical volume values
        group          = cov.Dx;                       % Selecting the group assignment column for all participants
        controlCode    = 0;                            % Specifying that controls are coded as 0
        Z              = zscore_matrix(data, group, controlCode);  

        %% As a quick example, let's project data from individuals with left TLE to the subcortical surface template
        Z_TLE = mean(Z(find(cov.SDx == 3), :), 1);     % Mean z-score values for left TLE patients (SDx == 3)
        f = figure,
            plot_subcortical(Z_TLE);
            colormap(flipud(Blues))                    % change colormap here
            SurfStatColLim([-3, 0])                    % change colorbar limits here

.. image:: ./examples/example_figs/sctx_py.png
    :align: center
