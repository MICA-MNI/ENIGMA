.. _apireferencelist_surface_to_parcel:

.. title:: Matlab API | surface_to_parcel

.. _surface_to_parcel_mat:

surface_to_parcel()
------------------------------------

**Usage** [`source <https://github.com/MICA-MNI/ENIGMA/blob/master/matlab/scripts/useful/surface_to_parcel.m>`_]:
    .. function:: 
        surf2parcel = surface_to_parcel(surf_data, parcellation)

**Description**:
    Map surface data to a parcellation (authors : @MICA-MNI, @saratheriver)

**Inputs**:
    - **surf_data** (*double array*) - Surface vector, size = [v x 1].
    - **parcellation** (*string, optional*) - Default is 'aparc_fsa5'

**Outputs**:
    - **surf2parcel** (*double array*) – Vector of values mapped from a surface to a parcellation