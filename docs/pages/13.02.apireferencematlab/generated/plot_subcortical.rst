.. _apireferencelist_plot_subcortical:

.. title:: Matlab API | plot_subcortical

.. _plot_subcortical_mat:

plot_subcortical()
------------------------------------

**Usage** [`source <https://github.com/MICA-MNI/ENIGMA/blob/master/matlab/scripts/surface_viewer/plot_subcortical.m>`_]:
    .. function:: 
       [a, cb] = plot_subcortical(data, varargin);

**Description**:
    Plot subcortical surface with lateral and medial views (author: @saratheriver)

**Inputs**:
    - **data** (*double array*) – vector of data, size = [1 x v]. One value per subcortical structure, in this order: L-accumbens, L-amygdala, L-caudate, L-hippocampus, L-pallidum L-putamen, L-thalamus, L-ventricle, R-accumbens, R-amygdala, R-caudate, R-hippocampus, R-pallidum, R-putamen, R-thalamus, R-ventricle

**Name/value pairs**:
    - **ventricles** (*string, optional*) – If 'True' (default) shows the ventricles (``data must be size = [1 x 16]``). If 'False', then ventricles are not shown and ``data must be size = [1 x 14]``.
    - **label_text** (*string, optional*) – Label text for colorbar. Default is empty.
    - **background** (*string, double array, optional*) – Background color. Default is 'white'.
    - **color_range** (*double array, optional*) – Range of colorbar. Default is [min(data) max(data)].
    - **cmap** (*string, double array, optional*) – Colormap name. Default is ‘RdBu_r’.

**Outputs**:
    - **a** (*axes*) – vector of handles to the axes, left to right, top to bottom
    - **cb** (*colorbar*) - colorbar handle