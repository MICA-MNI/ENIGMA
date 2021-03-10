.. _apireferencelist_mat_load_sc_ws:

.. title:: Matlab API | load_sc_as_one

.. _load_sc_as_one_mat:

load_sc_as_one()
------------------------------

**Usage** [`source <https://github.com/MICA-MNI/ENIGMA/blob/master/matlab/scripts/load_connectivity/load_sc_as_one.m>`_]:
    .. function:: 
        [strucMatrix, strucLabels] = load_sc_as_one(parcellation)

**Description:**
    Load structural connectivity data (cortical + subcortical in one matrix; author: @saratheriver)

**Inputs:**
    - **parcellation** (*string, optional*) - Name of parcellation (with n cortical parcels). Default is
    'aparc'. Other options are 'schaefer_100', 'schaefer_200', 'schaefer_300',
    'schaefer_400'.

**Outputs:**
    - **strucMatrix** (*double array*) – Structural connectivity, size = [n+14 x n+14]
    - **strucLabels** (*cell array*) – Region labels, size = [1 x n+14]
