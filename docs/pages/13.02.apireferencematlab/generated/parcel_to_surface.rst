.. _apireferencelist_parcel_to_surface:

.. title:: Matlab API | parcel_to_surface

.. _parcel_to_surface_mat:

parcel_to_surface()
------------------------------------

**Usage** [`source <https://github.com/MICA-MNI/ENIGMA/blob/master/matlab/scripts/useful/parcel_to_surface.m>`_]:
    .. function:: 
        parcel2surf = parcel_to_surface(parcel_data, parcellation, fill)

**Description**:
    Map parcellated data to the surface (authors : @MICA-MNI, @saratheriver)

**Inputs**:
    - **parcel_data** (*double array*) - Parcel vector, size = [p x 1]. For example, if Desikan Killiany from ENIGMA data, then parcel_data is size =  [68 x 1].
    - **parcellation** (*string, optional*) - Default is 'aparc_fsa5'
    - **fill** (*double, optional*) - Value for mask. Default is 0.

**Outputs**:
    - **parcel2surf** (*double array*) – Vector of values mapped from a parcellation to the surface