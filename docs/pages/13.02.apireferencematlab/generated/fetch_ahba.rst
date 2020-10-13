.. _apireferencelist_fetch_ahba:

.. title:: Matlab API | fetch_ahba

.. _fetch_ahba_mat:

fetch_ahba()
------------------------------------

**Usage** [`source <https://github.com/MICA-MNI/ENIGMA/blob/master/matlab/scripts/ahba/fetch_ahba.m>`_]:
    .. function:: 
        genes = fetch_ahba();

**Description**:
    Fetch Allen Human Brain Atlas microarray expression data from all donors and all genes (author: @saratheriver)

**Inputs**:
    **csvfile** (empty or string) – Path to downloaded csvfile. If empty (default), fetches microarray 
    expression data from the internet.

**Outputs**:
    **genes** (*table*) - Gene co-expression data, size = [82 x 15634]