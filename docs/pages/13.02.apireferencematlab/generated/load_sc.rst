.. _apireferencelist_mat_load_sc:

.. title:: Matlab API | load_sc

.. _load_sc_mat:

load_sc()
------------------------------

**Usage** [`source <https://github.com/MICA-MNI/ENIGMA/blob/master/matlab/scripts/load_connectivity/load_sc.m>`_]:
    .. function:: 
        [strucMatrix_ctx, strucLabels_ctx, strucMatrix_sctx, strucLabels_sctx] = load_sc()

**Description:**
    Load structural connectivity data parcellated using Desikan Killiany (author: @saratheriver)

**Outputs:**
    - **strucMatrix_ctx** (*double array*) – Cortico-cortical connectivity, size = [68 x 68]
    - **strucLabels_ctx** (*cell array*) – Cortical labels, size = [1 x 68]
    - **strucMatrix_sctx** (*double array*) –  Subcortico-cortical connectivity, size = [14 x 68]
    - **strucLabels_sctx** (*cell array*) – Subcortical labels, size = [1 x 14]