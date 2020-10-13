.. _apireferencelist_load_summary_stats:

.. title:: Matlab API | load_summary_stats

.. _load_sumstats_mat:

load_summary_stats(disorder)
------------------------------------

**Usage:**
    :mod:`summary_stats = load_summary_stats(disorder)`
    [`source <https://github.com/MICA-MNI/ENIGMA/blob/master/matlab/scripts/summary_statistics/load_summary_stats.m>`_]

**Description:**
    Outputs summary statistics for a given disorder (author: @saratheriver)

**Inputs:**
    **disorder** ({'22q', 'adhd', 'asd', 'bipolar', 'depression', 'epilepsy', 'ocd', 'schizophrenia'}) – Disorder name, default is None

**Outputs:**
    - **summary_stats** (*table*) – Available summary statistics