.. _apireferencelist_load_summary_stats:

.. title:: Matlab API | load_summary_stats

.. _load_sumstats_mat:

load_summary_stats(disorder)
------------------------------------

**Usage** [`source <https://github.com/MICA-MNI/ENIGMA/blob/master/matlab/scripts/summary_statistics/load_summary_stats.m>`_]:
    .. function:: 
        summary_stats = load_summary_stats(disorder)

**Description**:
    Outputs summary statistics for a given disorder (author: @saratheriver)

**Inputs**:
    - **disorder** ({'22q', 'adhd', 'asd', 'bipolar', 'depression', 'epilepsy', 'ocd', 'schizophrenia'}) – Disorder name, must pick one.

**Outputs**:
    - **summary_stats** (*table*) – Available summary statistics