.. _surf_visualization:

Surface data visualization
======================================

This page contains descriptions and examples to visualize surface data!


Cortical surface visualization
-----------------------------------
**ENIGMA TOOLBOX** comes equipped with fsaverage5 and Conte69 cortical midsurfaces and numerous parcellations!   
Following the examples below, we can easily map parcellated data (*e.g.*, Desikan-Killiany) to fsaverage5 surface space (*i.e.*, vertices). 
The same approach can be used to map parcellated data to conte69 surface space; simply replace every instance of 'fsa5' with 'conte69'!

.. tabs::

   .. code-tab:: py
       
        >>> import os
        >>> import numpy as np
        >>> import enigmatoolbox.datasets
        >>> from enigmatoolbox.datasets import load_fsa5
        >>> from enigmatoolbox.plotting import plot_hemispheres

        >>> # Load mapping between parcellation (e.g., Desikan-Killiany) and surface (fsa5)
        >>> fname = 'aparc_fsa5.csv'
        >>> labeling = np.loadtxt(os.path.join(os.path.dirname(enigmatoolbox.datasets.__file__),
        ...           'parcellations', fname), dtype=np.int)

        >>> # Map parcellation values to surface (vertices)
        >>> # In addition to several parcellations (Schaefer, Glasser, aparc, etc.), the function below also works with 
        >>> # ENIGMA-parcellated data (e.g., Desikan-Killiany atlas without values for the brain mask and the corpus
        >>> # callosum [68 x 1 ndarray])
        >>> data_fsa5 = map_to_labels(np.arange(68), labeling)

        >>> # Load cortical surface and map values to the surface brain
        >>> surf_lh, surf_rh = load_fsa5()
        >>> plot_hemispheres(surf_lh, surf_rh, array_name=data_fsa5, size=(800, 400),
        ...                  cmap='viridis', color_bar=True, color_range=(np.min(data_fsa5), np.max(data_fsa5)))


   .. code-tab:: matlab

        %% add the path to the ENIGMA TOOLBOX matlab folder
        addpath(genpath('/path/to/ENIGMA/matlab/'));

        %% Map parcellation values to surface (vertices)
        % In addition to several parcellations (Schaefer, Glasser, aparc, etc.), the function below also works with 
        % ENIGMA-parcellated data (e.g., Desikan-Killiany atlas without values for the brain mask and the corpus 
        % callosum [68 x 1 vector])
        mat                   = 1:1:68;
        data_fsa5             = map_to_labels(mat, 'aparc_fsa5.csv');
        
        %% Plot cortical values
        f = figure,
            plot_cortical(data_fsa5, 'fsa5')
            colormap(viridis)                                % change colormap here 
            SurfStatColLim([min(data_fsa5), max(data_fsa5)]) % change colorbar limits here


.. image:: ./examples/example_figs/ctx_py.png
    :align: center



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
    :align: center
