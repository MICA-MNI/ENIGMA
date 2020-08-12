.. _surf_visualization:

Surface data visualization
======================================

This page contains descriptions and examples to visualize surface data!


Cortical surface visualization
-----------------------------------
**ENIGMA TOOLBOX** comes equipped with fsaverage5 and Conte69 cortical midsurfaces and numerous parcellations!   
Following the examples below, we can easily map parcellated data (*e.g.*, Desikan-Killiany) to fsaverage5 surface space (*i.e.*, vertices).
In the following example, we will display mean subcortical volume reductions in individuals with TLE (*z*-scored to healthy controls).

.. Note::
     The same approach can be used to map parcellated data to the Conte69 surface template; simply replace every instance of 'fsa5' with 'conte69'...
     easy peasy lemon squeezy!

.. tabs::

   .. code-tab:: py
       
        >>> import os
        >>> import numpy as np
        >>> import enigmatoolbox.datasets
        >>> from enigmatoolbox.plotting import plot_cortical

        >>> # Load example data
        >>> # code here here here 

        >>> # Load mapping between parcellation (e.g., Desikan-Killiany) and surface (fsa5)
        >>> fname = 'aparc_fsa5.csv'
        >>> labeling = np.loadtxt(os.path.join(os.path.dirname(enigmatoolbox.datasets.__file__),
        ...           'parcellations', fname), dtype=np.int)

        >>> # Map parcellation values to surface (vertices)
        >>> # In addition to several parcellations (Schaefer, Glasser, aparc, etc.), the function below also works with 
        >>> # ENIGMA-parcellated data (e.g., Desikan-Killiany atlas without values for the brain mask and the corpus
        >>> # callosum [68 x 1 ndarray])
        >>> xdata_fsa5 = map_to_labels(xdata, labeling)

        >>> # Load cortical surface and map values to the surface brain
        >>> plot_hemispheres(surface_name="fsa", array_name=xdata_fsa5, size=(800, 400),
        ...                  cmap='viridis', color_bar=True, color_range=(np.min(data_fsa5), np.max(data_fsa5)))


   .. code-tab:: matlab

        %% Add the path to the ENIGMA TOOLBOX matlab folder
        addpath(genpath('/path/to/ENIGMA/matlab/'));

        %% Load example data
        % code here here here 

        %% Map parcellation values to surface (vertices)
        % In addition to several parcellations (Schaefer, Glasser, aparc, etc.), the function below also works with 
        % ENIGMA-parcellated data (e.g., Desikan-Killiany atlas without values for the brain mask and the corpus 
        % callosum [68 x 1 vector])
        xdata_fsa5             = map_to_labels(xdata, 'aparc_fsa5.csv');
        
        %% Plot cortical values
        f = figure,
            plot_cortical(xdata_fsa5, 'fsa5')
            colormap(viridis)                                % change colormap here 
            SurfStatColLim([min(data_fsa5), max(data_fsa5)]) % change colorbar limits here

.. image:: ./examples/example_figs/ctx_py.png
    :align: center



Subcortical surface visualization
---------------------------------------
The **ENIGMA TOOLBOX**'s subcortical viewer includes 16 segmented subcortical structures obtained from the Desikan-Killiany atlas (aparc+aseg.mgz). 
Subcortical regions include bilateral accumbens, amygdala, caudate, hippocampus, pallidum, putamen, thalamus, and ventricles. In the following example,
we will display subcortical volume reductions (*z*-scored to healthy controls) in an individual with left TLE.

.. admonition:: We've mentioned this already, but don't forget that...

     Subcortical input values are ordered as follows: left-accumbens, left-amygdala, left-caudate, left-hippocampus, 
     left-pallidum, left-putamen, left-thalamus, left-ventricles, right-accumbens, right-amygdala, right-caudate, right-hippocampus, 
     right-pallidum, right-putamen, right-thalamus, right-ventricles! You can re-order them using our ``reorder_sctx()`` function! 
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
        >>> data = metr1_SubVol_r.iloc[:, 1:-1]             # Selecting only columns with cortical thickness values
        >>> group = cov['Dx'].to_list()                     # Selecting the group assignment column for all participants
        >>> controlCode = 0                                 # Specifying that controls are coded as 0
        >>> Z = zscore_matrix(data, group, controlCode)

        >>> # As a quick example, let's project data from sub-PX013 to the subcortical surface template
        >>> Z_PX013 = Z.to_numpy()[cov[cov['SubjID'] == 'sub-PX013'].index, :]
        >>> plot_subcortical(array_name=Z_PX013, size=(800, 400),
        ...                  cmap='Blues_r', color_bar=True, color_range=(-2, 0))

   .. code-tab:: matlab

        %% Add the path to the ENIGMA TOOLBOX matlab folder
        addpath(genpath('/path/to/ENIGMA/matlab/'));

        %% Let's first load our example data; here we only need the covariates and the subcortical volumes
        [cov, metr1_SubVol, ~, ~] = load_example_data();

        %% After loading our subcortical data, we must re-order them (alphabetically and by hemisphere) as a requisite for plot_subcortical!
        metr1_SubVol_r = reorder_sctx(metr1_SubVol);

        %% Let's also z-score the data in patients, relative to controls, so that lower z-score indexes more atrophy
        data           = metr1_SubVol_r(:, 2:end-1);   % Selecting only columns with cortical thickness values
        group          = cov.Dx;                       % Selecting the group assignment column for all participants
        controlCode    = 0;                            % Specifying that controls are coded as 0
        Z              = zscore_matrix(data, group, controlCode);

        %% As a quick example, let's project data from sub-PX013 to the subcortical surface template
        Z_PX013 = Z(find(strcmp(cov.SubjID, 'sub-PX013')), :);
        f = figure,
            plot_subcortical(Z_PX013);
            colormap(flipud(Blues))                     % change colormap here
            SurfStatColLim([-2, 0])                     % change colorbar limits here

.. image:: ./examples/example_figs/sctx_py.png
    :align: center
