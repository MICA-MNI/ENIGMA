.. _apireferencelist_mat_load_fc:

.. title:: Matlab API | load_fc

.. _load_fc_mat:

load_fc()
------------------------------

**Usage** [`source <https://github.com/MICA-MNI/ENIGMA/blob/master/matlab/scripts/load_connectivity/load_fc.m>`_]:
    .. function:: 
        [funcMatrix_ctx, funcLabels_ctx, funcMatrix_sctx, funcLabels_sctx] = load_fc(parcellation)

**Description:**
    Load functional connectivity data (author: @saratheriver)

**Inputs:**
    - **parcellation** (*string, optional*) - Name of parcellation (with n cortical parcels). Default is
    'aparc'. Other options are 'schaefer_100', 'schaefer_200', 'schaefer_300',
    'schaefer_400'.

**Outputs:**
    - **funcMatrix_ctx** (*double array*) – Cortico-cortical connectivity, size = [n x n]
    - **funcLabels_ctx** (*cell array*) – Cortical labels, size = [1 x n]
    - **funcMatrix_sctx** (*double array*) –  Subcortico-cortical connectivity, size = [14 x n]
    - **funcLabels_sctx** (*cell array*) – Subcortical labels, size = [1 x 14]
