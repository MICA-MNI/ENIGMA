.. _apireferencelist_bb_moments:

.. title:: Matlab API | bb_moments_raincloud

.. _bb_moments_raincloud_mat:

bb_moments_raincloud()
------------------------------------

**Usage** [`source <https://github.com/MICA-MNI/ENIGMA/blob/master/matlab/scripts/histology/bb_moments_raincloud.m>`_]:
    .. function:: 
        bb_moments_raincloud(region_idx, title)

**Description**:
    Stratify regional data according to BigBrain statistical moments (authors: @caseypaquola, @saratheriver)

**Inputs**:
    - **region_idx** (*double array*) - Vector of data. Indices of regions to be included in analysis
    - **parcellation** (*string, optional*) - Name of parcellation. Options are 'aparc', 'schaefer_100', 'schaefer_200', 'schaefer_300', 'schaefer_400', 'glasser_360'. Default is 'aparc'.
    - **title** (*string, optional*) - Title of raincloud plot. Default is empty.

**Outputs**:
    - **figure** (*figure*) – Raincloud plot.