.. _apireferencelist_write_cifti:

.. title:: Matlab API | write_cifti

.. _write_cifti_mat:

write_cifti()
------------------------------------

**Usage** [`source <https://github.com/MICA-MNI/ENIGMA/blob/master/matlab/scripts/import_export/write_cifti.m>`_]:
    .. function:: 
        write_cifti(data, varargin)

**Description**:
    Writes cifti file (authors: @NicoleEic, @saratheriver)

**Inputs**:
    - **data** (*double* or *single*) – Data to be saved
  
**Name/value pairs**:
    - **dpath** (*string, optional*) – Path to location for saving file (e.g., '/Users/bonjour/'). Default is ''.
    - **fname** (*string, optional*) – Name of file (e.g., 'ello.dscalar.nii'). Default is ''.
    - **surface_name** (*string, optional*) – Surface name {'fsa5', 'conte69'}. Default is 'conte69'.
    - **hemi** (*string, optional*) – Name of hemisphere {'lh', 'rh'}. Default is 'lh'.
