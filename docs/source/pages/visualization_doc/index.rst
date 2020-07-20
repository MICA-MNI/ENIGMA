.. _surf_visualization:

Surface data visualization
======================================

This page contains descriptions and examples to visualize surface data!


Cortical surface visualization
-----------------------------------
**ENIGMA TOOLBOX** comes equipped with fsaverage5 and Conte69 cortical midsurfaces.   
Following the examples below, we can easily map parcellated data (*e.g.*, Desikan-Killiany) to fsaverage5 surface space (*i.e.*, vertices). 
The same approach can be used to map parcellated data to conte69 surface space; simply replace every instance of 'fsa5' with 'conte69'!

.. tabs::

   .. code-tab:: py
       
        >>> import os
        >>> import numpy as np
        >>> import brainspace.datasets
        >>> from brainspace.datasets import load_fsa5
        >>> from brainspace.plotting import plot_hemispheres
        >>> from brainspace.utils.parcellation import map_to_labels

        >>> # Because ENIGMA does not provide values for the brain mask and the corpus callosum
        >>> # we will give them a value of zeros
        >>> a_idx = list(range(1, 4)) + list(range(5, 39)) + list(range(40, 71)) # indices of parcels included in ENIGMA
        >>> data_DK = np.zeros(71)                                               # vector of zeros to be filled with cortical values
        >>> data_DK[a_idx] = list(range(1, 69))                                  # insert orginal Desikan-Killiany cortical values (68 values) in the vector of zeros

        >>> # Load cortical surface
        >>> surf_lh, surf_rh = load_fsa5()

        >>> # Load mapping between parcellation (Desikan-Killiany) and surface (fsa5)
        >>> fname = 'aparc_fsa5.csv'
        >>> labeling = np.loadtxt(os.path.join(os.path.dirname(brainspace.datasets.__file__),
        ...                       'parcellations', fname), dtype=np.int)

        >>> # Map parcellation values to surface (vertices)
        >>> data_fsa5 = map_to_labels(data_DK, labeling)

        >>> plot_hemispheres(surf_lh, surf_rh, array_name=data_fsa5, size=(800, 400),
        ...                  cmap='viridis', color_bar=True, color_range=(0, 68))


   .. code-tab:: matlab

        %% add the path to the ENIGMA TOOLBOX matlab folder
        addpath(genpath('/path/to/ENIGMA/matlab/'));

        %% Because ENIGMA does not provide values for the brain mask and the corpus callosum
        % we will give them a value of zero
        a_idx                 = [2:1:4 6:1:39 41:1:71];     % indices of parcels included in ENIGMA
        data_DK               = zeros(71, 1);               % vector of zeros to be filled with cortical values
        data_DK(a_idx)        = 1:1:68;                     % insert orginal Desikan-Killiany cortical values (68 values) in the vector of zeros
        
        %% Map parcellation values to surface (vertices)
        data_fsa5             = parcels_to_vertices(data_DK, 'fsa5')
        
        %% Plot cortical values
        f = figure,
            plot_cortical(data_fsa5, 'fsa5')
            colormap(viridis)                                % change colormap here 
            SurfStatColLim([min(data_fsa5), max(data_fsa5)]) % change colorbar limits here


        % A similar approach can be done to map Desikan-Killiany data to Conte69                      
        data_conte69          = parcels_to_vertices(data_DK, 'conte69')
        f = figure,
            plot_cortical(data_conte69, 'conte69')
            colormap(viridis)                                   
            SurfStatColLim([min(data_conte69), max(data_conte69)])   


.. image:: ./examples/example_figs/ctx_py.png



Subcortical surface visualization
---------------------------------------
| The **ENIGMA TOOLBOX**'s subcortical viewer includes 16 segmented subcortical structures obtained from the Desikan-Killiany atlas (aparc+aseg.mgz). Subcortical regions include bilateral accumbens, amygdala, caudate, hippocampus, pallidum, putamen, thalamus, and ventricles. 

.. tabs::

   .. code-tab:: py

        >>> import numpy as np
        >>> from brainspace.datasets import load_subcortical
        >>> from brainspace.plotting import plot_hemispheres
        >>> from brainspace.utils.parcellation import subcorticalvertices

        >>> # Transform subcortical values (one per subcortical structure) to vertices
        >>> # Input values (i.e., subcortical_values) are ordered as follows:
        >>> #     np.array([left-accumbens, left-amygdala, left-caudate, left-hippocampus, 
        >>> #               left-pallidum, left-putamen, left-thalamus, left-ventricles,
        >>> #               right-accumbens, right-amygdala, right-caudate, right-hippocampus, 
        >>> #               right-pallidum, right-putamen, right-thalamus, right-ventricles]) 
        >>> data = subcorticalvertices(subcortical_values=np.array(range(16)))

        >>> # Load subcortical surfaces
        >>> surf_lh, surf_rh = load_subcortical()

        >>> # Plot subcortical values
        >>> plot_hemispheres(surf_lh, surf_rh, array_name=data, size=(800, 400), 
        ...                  cmap='viridis', color_range=(0,15), color_bar=True)


   .. code-tab:: matlab

        %% add the path to the ENIGMA TOOLBOX matlab folder
        addpath(genpath('/path/to/ENIGMA/matlab/'));

        %% Plot subcortical values
        % Input values are ordered as follows:
        %      [left-accumbens, left-amygdala, left-caudate, left-hippocampus, 
        %       left-pallidum, left-putamen, left-thalamus, left-ventricles,
        %       right-accumbens, right-amygdala, right-caudate, right-hippocampus, 
        %       right-pallidum, right-putamen, right-thalamus, right-ventricles]
        data = 0:1:15;                               % 16 x 1 data vector
        f = figure,
            plot_subcortical(data);
            colormap(viridis)                         % change colormap here 
            SurfStatColLim([min(data), max(data)])    % change colorbar limits here


.. image:: ./examples/example_figs/sctx_py.png