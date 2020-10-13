.. _apireferencelist_shuf_test:

.. title:: Matlab API | shuf_test

.. _shuf_test_mat:

shuf_test()
------------------------------------

**Usage** [`source <https://github.com/MICA-MNI/ENIGMA/blob/master/matlab/scripts/permutation_testing/shuf_test.m>`_]:
    .. function:: 
        [p_shuf, r_dist] = shuf_test(map1, map2, varargin)

**Description**:
    Shuf permuation (author: @saratheriver)

**Inputs**:
    - **map1** (*double array*) – One of two map to be correlated
    - **map2** (*double array*) – The other map to be correlated

**Name/value pairs**:
    - **n_rot** (*int, optional*) – Number of shuffles. Default is 100.
    - **type** (*string, optional*) – Correlation type {‘pearson’, ‘spearman’}. Default is ‘pearson’.

**Outputs**:
    - **p_shuf** (*double*) – Permutation p-value
    - **r_dist** (*double array*) - Null correlations, size = [n_rot*2 x 1].