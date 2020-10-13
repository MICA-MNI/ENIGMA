.. _apireferencelist_plot_cortical:

.. title:: Matlab API | plot_cortical

.. _plot_cortical_mat:

plot_cortical()
------------------------------------

**Usage** [`source <https://github.com/MICA-MNI/ENIGMA/blob/master/matlab/scripts/surface_viewer/plot_cortical.m>`_]:
    .. function:: 
        [a, cb] = plot_cortical(data, varargin);

**Description**:
    Plot cortical surface with lateral and medial views (authors: @MICA-MNI, @saratheriver)

**Inputs**:
    - **data** (*double array*) – vector of data, size = [1 x v]

**Name/value pairs**:
    - **surface_name** (*string, optional*) – Name of surface {‘fsa5’, ‘conte69}. Default is ‘fsa5’.
    - **label_text** (*string, optional*) – Label text for colorbar. Default is empty.
    - **background** (*string, double array, optional*) – Background color. Default is 'white'.
    - **color_range** (*double array, optional*) – Range of colorbar. Default is [min(data) max(data)].
    - **cmap** (*string, double array, optional*) – Colormap name. Default is ‘RdBu_r’.

**Outputs**:
    - **a** (*axes*) – vector of handles to the axes, left to right, top to bottom
    - **cb** (*colorbar*) - colorbar handle