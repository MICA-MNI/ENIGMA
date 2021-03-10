.. _apireferencelist_zscore_matrix:

.. title:: Matlab API | zscore_matrix

.. _zscore_matrix_mat:

zscore_matrix()
------------------------------------

**Usage** [`source <https://github.com/MICA-MNI/ENIGMA/blob/master/matlab/scripts/useful/zscore_matrix.m>`_]:
    .. function:: 
        Z = zscore_matrix(data, group, controlCode)

**Description**:
    Z-score data relative to a given group (author: @saratheriver)

**Inputs**:
    - **data** (*double array*) - Data matrix (e.g., thickness data), size = [n_subject x n_region]
    - **group** (*double array*) - Vector of values for group assignment (e.g, [0 0 0 1 1 1], same length as n_subject. 
    - **controlCode** (*int*) - Value that corresponds to "baseline" group.

**Outputs**:
    - **Z** (*doule array*) – Z-scored data relative to control code