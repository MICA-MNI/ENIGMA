.. _apireferencelist_rotate_parcellation:

.. title:: Matlab API | rotate_parcellation

.. _rotate_parcellation_mat:

rotate_parcellation()
------------------------------------

**Usage** [`source <https://github.com/MICA-MNI/ENIGMA/blob/master/matlab/scripts/permutation_testing/rotate_parcellation.m>`_]:
    .. function:: 
        perm_id = rotate_parcellation(coord_l, coord_r, nrot)

**Description**:
    Rotate parcellation (authors: @frantisekvasa, @saratheriver)

**Inputs**:
    - **coord_l** (*double array*) – Coordinates of left hemisphere regions on the sphere, size = [m x 3]
    - **coord_r** (*double array*) – Coordinates of right hemisphere regions on the sphere, size = [m x 3]
    - **nrot** (*int, optional*) – Number of rotations. Default is 100.

**Outputs**:
    - **perm_id** (*double array*) – Array of permutations, size = [m x nrot]

**References**:
    - Alexander-Bloch A, Shou H, Liu S, Satterthwaite TD, Glahn DC, Shinohara RT, Vandekar SN and Raznahan A (2018). On testing for spatial correspondence between maps of human brain structure and function. NeuroImage, 178:540-51.
    - Váša F, Seidlitz J, Romero-Garcia R, Whitaker KJ, Rosenthal G, Vértes PE, Shinn M, Alexander-Bloch A, Fonagy P, Dolan RJ, Goodyer IM, the NSPN consortium, Sporns O, Bullmore ET (2017). Adolescent tuning of association cortex in human structural brain networks. Cerebral Cortex, 28(1):281–294.