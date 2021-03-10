.. _apireferencelist_nfaces:

.. title:: Matlab API | nfaces

.. _nfaces_mat:

nfaces()
------------------------------

**Usage** [`source <https://github.com/MICA-MNI/ENIGMA/blob/master/matlab/scripts/surface_viewer/nfaces.m>`_]:
    .. function:: 
        M = nfaces(surface_name, hemisphere)

**Description:**
    Returns number of faces/triangles for a surface (author: @saratheriver)

**Inputs:**
    - **surface_name** (*string*) - Name of surface {'fsa5', 'conte69'}
    - **hemisphere** (*string*) - Name of hemisphere {'lh', 'rh', 'both'}

**Outputs:**
    - **numfaces** (*double*) – Number of faces/triangles