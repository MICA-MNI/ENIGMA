.. _apireferencelist_mat_load_sc_ws:

.. title:: Matlab API | load_sc_as_one

.. _load_sc_as_one_mat:

load_sc_as_one()
------------------------------

**Usage** [`source <https://github.com/MICA-MNI/ENIGMA/blob/master/matlab/scripts/load_connectivity/load_sc_as_one.m>`_]:
    .. function:: 
        [strucMatrix, strucLabels] = load_sc_as_one()

**Description:**
    Load structural connectivity data (cortical + subcortical in one matrix) parcellated using Desikan Killiany (author: @saratheriver)

**Outputs:**
    - **strucMatrix** (*double array*) – Structural connectivity, size = [82 x 82]
    - **strucLabels** (*cell array*) – Region labels, size = [1 x 82]
