.. _apireferencelist_bb_gradient:

.. title:: Matlab API | bb_gradient_plot

.. _bb_gradient_plot_mat:

bb_gradient_plot()
------------------------------------

**Usage** [`source <https://github.com/MICA-MNI/ENIGMA/blob/master/matlab/scripts/histology/bb_gradient_plot.m>`_]:
    .. function:: 
        bb_gradient_plot(data, varargin)

**Description**:
    Stratify parcellated data according to the BigBrain gradient (authors: @caseypaquola, @saratheriver)

**Inputs**:
    - **data** (*double array*) – vector of data. Parcellated data.

**Name/value pairs**:
    - **parcellation** (*string, optional*) - Name of parcellation. Options are: 'aparc', 'schaefer_100', 'schaefer_200', 'schaefer_300', 'schaefer_400', 'glasser_360'. Default is 'aparc'.
    - **title** (*string, optional*) – Title of spider plot. Default is empty.
    - **axis_range** (*double array, optional*) - Range of spider plot axes. Default is (min, max).
    - **yaxis_label** (*string, optional*) - Label for y-axis. Default is empty.
    - **xaxis_label** (*string, optional*) - Label for x-axis. Default is empty.

**Outputs**:
    - **figure** (*figure*) – Gradient plot.