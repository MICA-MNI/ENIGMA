.. _apireferencelist_risk_genes:

.. title:: Matlab API | risk_genes

.. _risk_genes_mat:

risk_genes(disorder)
------------------------------------

**Usage** [`source <https://github.com/MICA-MNI/ENIGMA/blob/master/matlab/scripts/ahba/risk_genes.m>`_]:
    .. function:: 
        risk_genes = risk_genes(disorder)

**Description**:
    Outputs names of GWAS-derived risk genes for a given disorder (author: @saratheriver)

**Inputs**:
    - **disorder** ({'adhd', 'asd', 'bipolar', 'depression', 'epilepsy', 'hippocampal_volume', 'ocd', 'schizophrenia', 'tourette'}) – 
    Disorder name, must pick one.

**Outputs**:
    - **risk_genes** (*cell array*) – Names of genes for a given disorder