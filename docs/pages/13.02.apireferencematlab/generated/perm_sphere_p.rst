.. _apireferencelist_perm_sphere_p:

.. title:: Matlab API | perm_sphere_p

.. _perm_sphere_p_mat:

perm_sphere_p()
------------------------------------

**Usage** [`source <https://github.com/MICA-MNI/ENIGMA/blob/master/matlab/scripts/permutation_testing/perm_sphere_p.m>`_]:
    .. function:: 
        [p_perm, null_dist] = perm_sphere_p(x, y, perm_id, corr_type)

**Description**:
    Generate a p-value for the spatial correlation between two parcellated cortical surface maps (authors: @frantisekvasa, @saratheriver)

**Inputs**:
    - **x** (*double array*) – One of two map to be correlated
    - **y** (*double array*) – The other map to be correlated
    - **perm_id** (*double array*) – Array of permutations, size = [m x nrot]
    - **corr_type** (*string, optional*) - Correlation type {‘pearson’, ‘spearman’}. Default is ‘pearson’.

**Outputs**:
    - **p_perm** (*double*) – Permutation p-value
    - **null_dist** (*double array*) - Null correlations, size = [n_rot*2 x 1].

**References**:
    - Alexander-Bloch A, Shou H, Liu S, Satterthwaite TD, Glahn DC, Shinohara RT, Vandekar SN and Raznahan A (2018). On testing for spatial correspondence between maps of human brain structure and function. NeuroImage, 178:540-51.
    - Váša F, Seidlitz J, Romero-Garcia R, Whitaker KJ, Rosenthal G, Vértes PE, Shinn M, Alexander-Bloch A, Fonagy P, Dolan RJ, Goodyer IM, the NSPN consortium, Sporns O, Bullmore ET (2017). Adolescent tuning of association cortex in human structural brain networks. Cerebral Cortex, 28(1):281–294.