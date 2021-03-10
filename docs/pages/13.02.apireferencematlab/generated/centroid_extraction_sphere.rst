.. _apireferencelist_centroid_extraction_sphere:

.. title:: Matlab API | centroid_extraction_sphere

.. _centroid_extraction_sphere_mat:

centroid_extraction_sphere()
------------------------------------

**Usage** [`source <https://github.com/MICA-MNI/ENIGMA/blob/master/matlab/scripts/permutation_testing/centroid_extraction_sphere.m>`_]:
    .. function:: 
        centroid = centroid_extraction_sphere(sphere_coords, annotfile)

**Description**:
    Extract centroids of a cortical parcellation on a surface sphere (authors: @frantisekvasa, @saratheriver)

**Inputs**:
    - **sphere_coords** (*double array*) – Sphere coordinates, size = [n x 3]
    - **annotfile** (*string*) – Name of annotation file {‘fsa5_lh_aparc.annot’, ‘fsa5_rh_aparc.annot, ‘fsa5_with_sctx_lh_aparc_aseg.csv’, etc.}
    - **ventricles** (*string, optional*) – Whether ventricle data are present. Only used when ‘annotfile’ is fsa5_with_sctx_lh_aparc_aseg or fsa5_with_sctx_lh_aparc_aseg. Default is 'False'.

**Outputs**:
    - **coord** (*double array*) – Coordinates of the centroid of each region on the sphere, size = [m x 3].

**References**:
    - Alexander-Bloch A, Shou H, Liu S, Satterthwaite TD, Glahn DC, Shinohara RT, Vandekar SN and Raznahan A (2018). On testing for spatial correspondence between maps of human brain structure and function. NeuroImage, 178:540-51.
    - Váša F, Seidlitz J, Romero-Garcia R, Whitaker KJ, Rosenthal G, Vértes PE, Shinn M, Alexander-Bloch A, Fonagy P, Dolan RJ, Goodyer IM, the NSPN consortium, Sporns O, Bullmore ET (2017). Adolescent tuning of association cortex in human structural brain networks. Cerebral Cortex, 28(1):281–294.