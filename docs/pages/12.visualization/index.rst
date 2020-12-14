.. _surf_visualization:

.. title:: Visualization tools

Surface data visualization
======================================

This page contains descriptions and examples to visualize surface data.


Cortical surface visualization
-----------------------------------
**ENIGMA TOOLBOX** comes equipped with fsaverage5 and Conte69 cortical midsurfaces and numerous parcellations.   
Following the examples below, we can easily map parcellated data (*e.g.*, Desikan-Killiany) to fsaverage5 surface space (*i.e.*, vertices).
In the following example, we will display cortical atrophy in individuals with left TLE.

.. admonition:: Our visualization tools work with ENIGMA and non-ENIGMA datasets 👀

     Mapping parcellated data to the surface has never been easier! Our ``parcel_to_surface()`` function works with ENIGMA- and non-ENIGMA datasets. Our toolbox includes several
     other parcellations (*e.g.*, glasser_fsa5, schaefer_100_fsa5, schaefer_200_fsa5, schaefer_300_fsa5, ...), so you can take advantage of
     our visualization tools for all your other projects!

.. admonition:: Don't like fsaverage5? Relax, we got you covered! 🛀🏾

     The same approach can be used to map parcellated data to the Conte69 surface template; simply replace every instance of 'fsa5' with 'conte69'!
     Easy peasy lemon squeezy 🍋

.. parsed-literal:: 

     **Prerequisites**
     ↪ Load :ref:`summary statistics <load_sumstats>` **or** :ref:`example data <load_example_data>`
     ↪ :ref:`Z-score data <zscore_data>` (*mega only*)
     
.. tabs::

   .. code-tab:: py **Python** | meta

        >>> from enigmatoolbox.utils.parcellation import parcel_to_surface
        >>> from enigmatoolbox.plotting import plot_cortical

        >>> # Map parcellated data to the surface
        >>> CT_d_fsa5 = parcel_to_surface(CT_d, 'aparc_fsa5')

        >>> # Project the results on the surface brain
        >>> plot_cortical(array_name=CT_d_fsa5, surface_name="fsa5", size=(800, 400),
        ...               cmap='RdBu_r', color_bar=True, color_range=(-0.5, 0.5))

   .. code-tab:: matlab **Matlab** | meta

        % Map parcellated data to the surface
        CT_d_fsa5 = parcel_to_surface(CT_d, 'aparc_fsa5');

        % Project the results on the surface brain
        f = figure,
            plot_cortical(CT_d_fsa5, 'surface_name', 'fsa5', 'color_range', ...
                          [-0.5 0.5], 'cmap', 'RdBu_r') 

   .. tab:: ⤎ ⤏

          | ⤎ If you have **meta**-analysis data (*e.g.*, summary statistics)
          | ⤏ If you have individual site or **mega**-analysis data

   .. code-tab:: py **Python** | mega
       
        >>> from enigmatoolbox.utils.parcellation import parcel_to_surface
        >>> from enigmatoolbox.plotting import plot_cortical

        >>> # Before visualizing the data, we need to map the parcellated data to the surface
        >>> CT_z_mean_fsa5 = parcel_to_surface(CT_z_mean, 'aparc_fsa5')

        >>> # Project the results on the surface brain
        >>> plot_cortical(array_name=CT_z_mean_fsa5, surface_name="fsa5", size=(800, 400),
        >>>               cmap='Blues_r', color_bar=True, color_range=(-2, 0))

   .. code-tab:: matlab **Matlab** | mega

        % Map parcellated data to the surface
        CT_d_fsa5 = parcel_to_surface(CT_z_mean{:, :}, 'aparc_fsa5');

        % Project the results on the surface brain
        f = figure,
            plot_cortical(CT_z_mean_fsa5, 'surface_name', 'fsa5', 'color_range', ...
                          [-2 0], 'cmap', 'Blues_r')

.. image:: ./examples/example_figs/d_ctx.png
    :align: center


|


Subcortical surface visualization
---------------------------------------
The **ENIGMA TOOLBOX**'s subcortical viewer includes 16 segmented subcortical structures obtained from the Desikan-Killiany atlas (aparc+aseg.mgz). 
Subcortical regions include bilateral accumbens, amygdala, caudate, hippocampus (technically not subcortical but considered as such by FreeSurfer), 
pallidum, putamen, thalamus, and ventricles. In the following example,
we will display subcortical atrophy in individuals with left TLE.

.. admonition:: We've mentioned this already, but don't forget that...

     Subcortical input values are ordered as follows: left-accumbens, left-amygdala, left-caudate, left-hippocampus, 
     left-pallidum, left-putamen, left-thalamus, left-ventricles, right-accumbens, right-amygdala, right-caudate, right-hippocampus, 
     right-pallidum, right-putamen, right-thalamus, right-ventricles! You can re-order your subcortical dataset using our ``reorder_sctx()`` function. 
     \*Ventricles are optional.

.. parsed-literal:: 

     **Prerequisites**
     ↪ Load :ref:`summary statistics <load_sumstats>` **or** :ref:`example data <load_example_data>`
     ↪ :ref:`Re-order subcortical data <reorder_sctx>` (*mega only*)
     ↪ :ref:`Z-score data <zscore_data>` (*mega only*)

.. tabs::

   .. code-tab:: py **Python** | meta

        >>> from enigmatoolbox.plotting import plot_subcortical

        >>> # Project the results on the surface brain
        >>> plot_subcortical(array_name=SV_d, size=(800, 400),
        ...                  cmap='RdBu_r', color_bar=True, color_range=(-0.5, 0.5))

   .. code-tab:: matlab **Matlab** | meta

        % Project the results on the surface brain
        f = figure,
            plot_subcortical(SV_d, 'color_range', [-0.5 0.5], 'cmap', 'RdBu_r')

   .. tab:: ⤎ ⤏

          | ⤎ If you have **meta**-analysis data (*e.g.*, summary statistics)
          | ⤏ If you have individual site or **mega**-analysis data

   .. code-tab:: py **Python** | mega

        >>> from enigmatoolbox.plotting import plot_subcortical

        >>> # Project the results on the surface brain
        >>> plot_subcortical(array_name=SV_z_mean, size=(800, 400),
        >>>                  cmap='Blues_r', color_bar=True, color_range=(-3, 0))

   .. code-tab:: matlab **Matlab** | meta

        % Project the results on the surface brain
        f = figure,
            plot_subcortical(SV_z_mean{:, :}, 'color_range', [-2 1], 'cmap', 'Blues_r')

.. image:: ./examples/example_figs/d_sctx.png
    :align: center
