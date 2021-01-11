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
    - **disorder** (**cell array, optional**) - Any combination of disorder name. Default is all available disorders, except 'adhd' due to NaNs. Options are any combination of {'22q', 'adhd', 'asd', 'bipolar', 'depression', 'epilepsy', 'ocd', 'schizophrenia'}.
    - **measure** (*cell array, optional*) - Any combination of measure names. Default is {'CortThick', 'CortSurf'}.
    - **additional_data_cortex** (*double array, optional*) - Name for additional cortical ENIGMA-type data. Must also provide 'additional_name_cortex'.
    - **additional_name_cortex** (*cell array, optional*) - Additional cortical ENIGMA-type data (n, 68). Must also provide 'additional_data_cortex'.
    - **additional_data_subcortex** (*double array, optional*) - Name for additional subcortical ENIGMA-type data. Must also provide 'additional_name_subcortex'.
    - **additional_name_subcortex** (*cell array, optional*) - Additional subcortical ENIGMA-type data (n, 16). Must also provide 'additional_data_subcortex'.
    - **ignore** (*cell array, optional*) - Ignore summary statistics with these expressions. Default is ('mega') as it contains NaNs.
    - **include** (c*ell array, optional*) - Include only summary statistics with these expressions. Default is empty.
    - **method** (*string, optional*) - Analysis method {'pca', 'correlation'}. Default is 'pca'.

**Outputs**:
    - **components** (*structure*) - Principal components of shared effects in descending order in terms of component variance. Only is method is 'pca'.
    - **variance** (*structure*) - Variance of components. Only is method is 'pca'.
    - **correlation_matrix** (*structure*) - Correlation matrix of for every pair of shared effect maps. Only is method is 'correlation'.
    - **names** (*structure*) - Name of disorder and case-control effect maps included in analysis.