.. _hubs_susceptibility:

Hub susceptibility
======================================

This page contains descriptions and examples to build hub susceptibility models!


Cortical hubs
------------------------------------------
| ...

.. tabs::

   .. code-tab:: py
       
        >>> ...


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


|


Subcortical hubs
---------------------------------------------
| ...

.. tabs::

   .. code-tab:: py

        >>> ...

   .. code-tab:: matlab

        %% ...


|


Relations between hubs and morphological measures
-------------------------------------------------------
| ...

.. tabs::

   .. code-tab:: py

        >>> ...

   .. code-tab:: matlab

        %% ...

