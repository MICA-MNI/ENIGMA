.. _apireferencelist_mat_load_fc:

.. title:: Matlab API | load_fc

.. _load_fc_mat:

load_fc()
------------------------------

**Usage** [`source <https://github.com/MICA-MNI/ENIGMA/blob/master/matlab/scripts/load_connectivity/load_fc.m>`_]:
    .. function:: 
        [funcMatrix_ctx, funcLabels_ctx, funcMatrix_sctx, funcLabels_sctx] = load_fc()

**Description:**
    Load functional connectivity data parcellated using Desikan Killiany (author: @saratheriver)

**Outputs:**
    - **funcMatrix_ctx** (*double array*) – Cortico-cortical connectivity, size = [68 x 68]
    - **funcLabels_ctx** (*cell array*) – Cortical labels, size = [1 x 68]
    - **funcMatrix_sctx** (*double array*) –  Subcortico-cortical connectivity, size = [14 x 68]
    - **funcLabels_sctx** (*cell array*) – Subcortical labels, size = [1 x 14]