.. _apireferencelist_cross_disorder:

.. title:: Matlab API | cross_disorder_effect

.. _cross_disorder_mat:

cross_disorder_effect()
------------------------------------

**Usage** [`source <https://github.com/MICA-MNI/ENIGMA/blob/master/matlab/scripts/summary_statistics/cross_disorder_effect.m>`_]:
    .. function:: 
        [components, variance, ~, names] = cross_disorder_effect(varargin)
        [~, ~, correlation_matrix, names] = cross_disorder_effect(varargin)

**Description**:
    Cross-disorder effect (authors: @boyongpark, @saratheriver) 

**Name/value pairs**:
    - **disorder** (**cell array, optional**) - Any combination of disorder name. Default is all available disorders {'22q', 'adhd', 'asd', 'bipolar', 'depression', 'epilepsy', 'ocd', 'schizophrenia'}.
    - **measure** (*cell array, optional*) - Any combination of measure names. Default is {'CortThick', 'CortSurf'}.
    - **additional_data** (*double array, optional*) - Name for additional ENIGMA-type data. Must also provide 'additional_name'.
    - **additional_name** (*cell array, optional*) - Additional ENIGMA-type data (n, 68). Must also provide 'additional_data'.
    - **ignore** (*cell array, optional*) - Ignore summary statistics with these expressions. Default is ('mega') as it contains NaNs.
    - **method** (*string, optional*) - Analysis method {'pca', 'correlation'}. Default is 'pca'.
    - **figure** (*string, optional*) - Whether to output figures {'True', 'False'}. Default is 'True'.

**Outputs**:
    - **components** (*double array*) - Principal components of shared effects in descending order in terms of component variance. Only is method is 'pca'.
    - **variance** (*double array*) - Variance of components. Only is method is 'pca'.
    - **correlation_matrix** (*double array*) - Correlation matrix of for every pair of shared effect maps. Only is method is 'correlation'.
    - **names** (*cell array*) - Name of disorder and case-control effect maps included in analysis.