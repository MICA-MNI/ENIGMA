.. _hubs_susceptibility:

Hub susceptibility
======================================

This page contains descriptions and examples to build hub susceptibility models!


Cortical hubs
------------------------------------------
Using the :ref:`HCP connectivity data <surf_visualization>`, we can then compute weighted (optimal for unthresholded connectivity
matrices) degree centrality to identify structural and functional hub regions. This is done by simply 
computing the sum of all weighted cortico-cortical connections for every region. Higher degree centrality 
denotes increased hubness (*i.e.*, node with many connections). 

.. tabs::

   .. code-tab:: py
       
        >>> import os
        >>> import numpy as np
        >>> import enigmatoolbox.datasets
        >>> from enigmatoolbox.plotting import plot_cortical
        >>> from enigmatoolbox.datasets import load_sc, load_fc
        >>> from enigmatoolbox.utils.parcellation import map_to_labels

        >>> # Load functional and structural cortico-cortical connectivity data
        >>> fc, _, _, _ = load_fc()
        >>> sc, _, _, _ = load_sc()

        >>> # Compute weighted degree centrality measures from the connectivity data
        >>> dc_f = np.sum(fc, axis=0)
        >>> dc_s = np.sum(sc, axis=0)

        >>> # Map parcellated data to the surface
        >>> fname = 'aparc_fsa5.csv'
        >>> labeling = np.loadtxt(os.path.join(os.path.dirname(enigmatoolbox.datasets.__file__),
        ...           'parcellations', fname), dtype=np.int)
        >>> dc_f_fsa5 = map_to_labels(dc_f, labeling)
        >>> dc_s_fsa5 = map_to_labels(dc_s, labeling)

        >>> # And project the results on the surface brain
        >>> plot_cortical(array_name=dc_f_fsa5, surface_name="fsa5", size=(800, 400),
        ...                 cmap='Reds', color_bar=True, color_range=(20, 30))

        >>> plot_cortical(array_name=dc_s_fsa5, surface_name="fsa5", size=(800, 400),
        ...               cmap='Blues', color_bar=True, color_range=(100, 300))


   .. code-tab:: matlab

        %% Load functional and structural cortico-cortical connectivity data
        [fc, ~, ~, ~]     = load_fc();
        [sc, ~, ~, ~]     = load_sc();

        %% Compute weighted degree centrality measures from the connectivity data
        dc_f                = sum(fc);
        dc_s                = sum(sc);

        %% Map parcellated data to the surface
        dc_f_fsa5           = map_to_labels(dc_f, 'aparc_fsa5.csv');
        dc_s_fsa5           = map_to_labels(dc_s, 'aparc_fsa5.csv');

        %% And project the results on the surface brain
        f = figure,
          plot_cortical(dc_f_fsa5, 'fsa5', 'functional degree centrality')
          colormap([Reds])
          SurfStatColLim([20 30])
     
        f = figure,
          plot_cortical(dc_s_fsa5, 'fsa5', 'structural degree centrality')
          colormap([Blues])
          SurfStatColLim([100 300]) 

.. image:: ./examples/example_figs/fc_hubs_ctx.png
    :align: center


|


Subcortical hubs
---------------------------------------------
The :ref:`HCP connectivity data <surf_visualization>` can also be used to identify structural 
and functional subcortico-cortical hub regions. As above, we simply compute the sum of all weighted 
subcortico-cortical connections for every subcortical area. Once again, higher degree centrality 
denotes increased hubness!

.. Attention:: 
     Because we do not have connectivity values for the ventricles, do make sure to set 
     the "ventricles" flag to ``False`` when displaying the findings on the subcortical surfaces!

.. tabs::

   .. code-tab:: py

        >>> import numpy as np
        >>> from enigmatoolbox.plotting import plot_subcortical
        >>> from enigmatoolbox.datasets import load_sc, load_fc

        >>> # Load functional and structural subcortico-cortical connectivity data
        >>> _, _, fc, _ = load_fc()
        >>> _, _, sc, _ = load_sc()

        >>> # Compute weighted degree centrality measures from the connectivity data
        >>> dc_f = np.sum(fc, axis=1)
        >>> dc_s = np.sum(sc, axis=1)

        >>> # And project the results on the subcortical surfaces (don't forget to set the ventricles flag to False!)
        >>> plot_subcortical(array_name=dc_f, ventricles=False, size=(800, 400),
        ...                  cmap='Reds', color_bar=True, color_range=(5, 10))

        >>> plot_subcortical(array_name=dc_s, ventricles=False, size=(800, 400),
        ...                  cmap='Blues', color_bar=True, color_range=(100, 300))

   .. code-tab:: matlab

        %% Load functional and structural subcortico-cortical connectivity data
        [~, ~, fc, ~]     = load_fc();
        [~, ~, sc, ~]     = load_sc();

        %% Compute weighted degree centrality measures from the connectivity data
        dc_f                = sum(fc, 2);
        dc_s                = sum(sc, 2);

        %% And project the results on the subcortical surfaces (don't forget to set the ventricles flag to 'False'!
        f = figure,
          plot_subcortical(dc_f, 'False', 'functional degree centrality')
          colormap([Reds])
          SurfStatColLim([5 10])
     
        f = figure,
          plot_subcortical(dc_s, 'False', 'structural degree centrality')
          colormap([Blues])
          SurfStatColLim([100 300])

.. image:: ./examples/example_figs/fc_hubs_sctx.png
    :align: center


|


Relations between hubs and morphological measures
-------------------------------------------------------
| ...

.. tabs::

   .. code-tab:: py

        >>> ...

   .. code-tab:: matlab

        %%

