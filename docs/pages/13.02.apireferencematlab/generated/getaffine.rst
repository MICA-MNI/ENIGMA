.. _apireferencelist_get_affine:

.. title:: Matlab API | getaffine

.. _get_affine_mat:

getaffine()
------------------------------

**Usage** [`source <https://github.com/MICA-MNI/ENIGMA/blob/master/matlab/scripts/surface_viewer/getaffine.m>`_]:
    .. function:: 
        M = getaffine(surface_name, hemisphere)

**Description:**
    Returns vox2ras transform for a surface (author: @saratheriver)

**Inputs:**
    - **surface_name** (*string*) - Name of surface {'fsa5', 'conte69'}
    - **hemisphere** (*string*) - Name of hemisphere {'lh', 'rh', 'both'}

**Outputs:**
    - **M** (*double*) – Vox2ras transform, size = [4 x 4]