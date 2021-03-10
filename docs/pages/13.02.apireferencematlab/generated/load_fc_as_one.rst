.. _apireferencelist_mat_load_fc_ws:

.. title:: Matlab API | load_fc_as_one

.. _load_fc_as_one_mat:

load_fc_as_one()
------------------------------

**Usage** [`source <https://github.com/MICA-MNI/ENIGMA/blob/master/matlab/scripts/load_connectivity/load_fc_as_one.m>`_]:
    .. function:: 
        [funcMatrix, funcLabels] = load_fc_as_one(parcellation)

**Description:**
    Load functional connectivity data (cortical + subcortical in one matrix; author: @saratheriver)

**Inputs:**
    - **parcellation** (*string, optional*) - Name of parcellation (with n cortical parcels). Default is
    'aparc'. Other options are 'schaefer_100', 'schaefer_200', 'schaefer_300',
    'schaefer_400'.

**Outputs:**
    - **funcMatrix** (*double array*) – Functional connectivity, size = [n+14 x n+14]
    - **funcLabels** (*cell array*) – Region labels, size = [1 x n+14]
