.. _surface_visualization:

Surface visualization
======================================

This page contains descriptions and examples to visualize surface data!


Cortical surface visualization
---------------
**ENIGMA TOOLBOX** comes equipped with fsaverage5 and Conte69 cortical midsurfaces... and mapping between parcellations and vertices.

.. tabs::

   .. code-tab:: py
       
        >>> from brainspace.datasets import load_conte69

        >>> # Load left and right hemispheres
        >>> surf_lh, surf_rh = load_conte69()
        >>> surf_lh.n_points
        32492

        >>> surf_rh.n_points
        32492

   .. code-tab:: matlab

        %% add the path to the ENIGMA TOOLBOX matlab folder
        addpath(genpath('/path/to/ENIGMA/matlab/'));

        %% Because ENIGMA does not provide values for the brain mask and the corpus callosum
        % we will give them a value of zero
        a_idx                 = [2:1:4 6:1:39 41:1:71];       % indices of parcels included in ENIGMA
        data_DK               = zeros(71, 1);                 % vector of zeros to be filled with cortical values
        data_DK(a_idx)        = 0:1:67;                       % insert cortical values (one per region, 68 x 1 vector) in vector of zeros
        
        %% Map parcellation values to surface (vertices)
        data_fsa5             = parcels_to_vertices(data_DK, 'fsa5')
        
        %% Plot cortical values
        f = figure,
            plot_cortical(data_fsa5, 'fsa5')
            colormap(viridis)                                   % change colormap here 
            SurfStatColLim([min(data_fsa5), max(data_fsa5)])    % change colorbar limits here


        % A similar approach can be done to map Desikan-Killiany data to Conte69                      
        data_conte69          = parcels_to_vertices(data_DK, 'conte69')
        f = figure,
            plot_cortical(data_conte69, 'conte69')
            colormap(viridis)                                   
            SurfStatColLim([min(data_conte69), max(data_conte69)])   

|

Subcortical surface visualization
---------------
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