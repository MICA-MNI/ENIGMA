.. _apireferencelist_spin_test:

.. title:: Matlab API | spin_test

.. _spin_test_mat:

spin_test()
------------------------------------

**Usage** [`source <https://github.com/MICA-MNI/ENIGMA/blob/master/matlab/scripts/permutation_testing/spin_test.m>`_]:
    .. function:: 
        [p_spin, r_dist] = spin_test(map1, map2, varargin)

**Description**:
    Spin permutation (author: @saratheriver)

**Inputs**:
    - **map1** (*double array*) – One of two map to be correlated
    - **map2** (*double array*) – The other map to be correlated

**Name/value pairs**:
    - **surface_name** (*string, optional*) – Surface name {‘fsa5’, ‘fsa5_with_sctx’}. Use 'fsa5' for Conte69. Default is ‘fsa5’.
    - **parcellation_name** (*string, optional*) – Parcellation name {‘aparc’, ‘aparc_aseg’}. Default is ‘aparc’.
    - **n_rot** (*int, optional*) – Number of spin rotations. Default is 100.
    - **type** (*string, optional*) – Correlation type {‘pearson’, ‘spearman’}. Default is ‘pearson’.
    - **ventricles** (*string, optional*) – Whether ventricles are present in map1, map2. Only used when ``parcellation_name is 'aparc_aseg'``. Default is 'False' (other option is 'True')

**Outputs**:
    - **p_spin** (*double*) – Permutation p-value
    - **r_dist** (*double array*) - Null correlations, size = [n_rot*2 x 1].

**References**:
    - Alexander-Bloch A, Shou H, Liu S, Satterthwaite TD, Glahn DC, Shinohara RT, Vandekar SN and Raznahan A (2018). On testing for spatial correspondence between maps of human brain structure and function. NeuroImage, 178:540-51.
    - Váša F, Seidlitz J, Romero-Garcia R, Whitaker KJ, Rosenthal G, Vértes PE, Shinn M, Alexander-Bloch A, Fonagy P, Dolan RJ, Goodyer IM, the NSPN consortium, Sporns O, Bullmore ET (2017). Adolescent tuning of association cortex in human structural brain networks. Cerebral Cortex, 28(1):281–294.