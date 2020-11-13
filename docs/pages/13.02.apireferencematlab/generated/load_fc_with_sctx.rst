.. _apireferencelist_mat_load_fc_ws:

.. title:: Matlab API | load_fc_as_one

.. _load_fc_as_one_mat:

load_fc_as_one()
------------------------------

**Usage** [`source <https://github.com/MICA-MNI/ENIGMA/blob/master/matlab/scripts/load_connectivity/load_fc_as_one.m>`_]:
    .. function:: 
        [funcMatrix, funcLabels] = load_fc_as_one()

**Description:**
    Load functional connectivity data (cortical + subcortical in one matrix) parcellated using Desikan Killiany (author: @saratheriver)

**Outputs:**
    - **funcMatrix** (*double array*) – Functional connectivity, size = [82 x 82]
    - **funcLabels** (*cell array*) – Region labels, size = [1 x 82]
