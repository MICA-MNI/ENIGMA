.. _load_ct:

.. title:: Load example data

Individual site data
======================================

This page contains descriptions and examples to load our example data, re-order subcortical labels, and z-score values!


.. _load_example_data:

Load example data
---------------------------

This is an example dataset that includes 10 healthy controls (7 females, age±SD=33.3±8.8 years) and 10 individuals with 
epilepsy (7 females, age±SD=39.8±14.8 years).

**Covariates** | As per ENIGMA-Epilepsy protocol, covariate information includes **SubjID** (subjectID),
**Dx** (diagnosis, 0=controls, 1=patients), **SDx** (sub-diagnosis, 0=controls,
1=non-lesional patients, 2=genetic generalized epilepsy (IGE/GGE) patients, 3=left TLE,
4=right TLE), **Age** (in years), **Sex** (1=males, 2=females), **Handedness** (1=right, 2=left),
**AO** (age at onset in years, patients only), **DURILL** (duration of illness in years, patients only),
and **ICV** (intracranial volume).

**Subcortical volume** | Subcortical grey matter volumes regroup data from 12 subcortical regions, bilateral hippocampus, and bilateral ventricles.


**Cortical thickness** | Cortical thickness was measured at each vertex as the Euclidean distance between white and pial surfaces,
and subsequently averaged within each of the Desikan-Killiany parcels.

**Cortical surface area** | The cortical surface area of every Desikan-Killiany parcel is also provided as part of ENIGMA imaging protocols;
this morphological measure is defined by the sum of the area of each of the triangles within the parcel.

.. tabs::

   .. code-tab:: py **Python** | mega
       
        >>> from enigmatoolbox.datasets import load_example_data

        >>> # Load all example data from an individual site
        >>> cov, metr1_SubVol, metr2_CortThick, metr3_CortSurf = load_example_data()

   .. code-tab:: matlab **Matlab** | mega

        % Load all example data from an individual site
        [cov, metr1_SubVol, metr2_CortThick, metr3_CortSurf] = load_example_data();


|


.. _reorder_sctx:

Re-order subcortical regions
------------------------------------
The column order from ENIGMA-derived subcortical volume matrices does not match the order in the connectivity matrices nor
the pre-requisite for our subcortical visualization tools. But, hey, don't you worry! To re-order ENIGMA-derived subcortical volume data, you may use 
our ``reorder_sctx()`` function, which will re-order the columns of the subcortical volume dataset accordingly (*i.e.*, alphabetically,
with all left hemisphere structures first followed by all right hemisphere structures). 

.. tabs::

   .. code-tab:: py **Python** | mega
       
        >>> from enigmatoolbox.utils.useful import reorder_sctx
        
        >>> # Re-order the subcortical data alphabetically and by hemisphere
        >>> metr1_SubVol_r = reorder_sctx(metr1_SubVol)

   .. code-tab:: matlab **Matlab** | mega

        % Re-order the subcortical data alphabetically and by hemisphere
        metr1_SubVol_r = reorder_sctx(metr1_SubVol);

     
|


.. _zscore_data:

Z-score data
------------------------------------
With our example data loaded and re-ordered, we can then z-score data in patients, relative to controls,
so that lower values correspond to greater atrophy. For simplicity, we also compute the mean z-score across
all left TLE patients. These mean, z-scored vectors will be used in subsequent tutorials as measures of subcortical 
and cortical atrophy!

.. parsed-literal:: 

    **Prerequisites**
    ↪ :ref:`Re-order subcortical data <reorder_sctx>`

.. tabs::

   .. code-tab:: py **Python** | mega
       
        >>> from enigmatoolbox.utils.useful import zscore_matrix
        
        >>> # Z-score patients' data relative to controls (lower z-score = more atrophy)
        >>> group = cov['Dx'].to_list()
        >>> controlCode = 0
        >>> SV_z = zscore_matrix(metr1_SubVol_r.iloc[:, 1:-1], group, controlCode)
        >>> CT_z = zscore_matrix(metr2_CortThick.iloc[:, 1:-5], group, controlCode)
        >>> SA_z = zscore_matrix(metr3_CortSurf.iloc[:, 1:-5], group, controlCode)

        >>> # Mean z-score values across individuals with from a specific group (e.g., left TLE, that is SDx == 3)
        >>> SV_z_mean = SV_z.iloc[cov[cov['SDx'] == 3].index, :].mean(axis=0)
        >>> CT_z_mean = CT_z.iloc[cov[cov['SDx'] == 3].index, :].mean(axis=0)
        >>> SA_z_mean = SA_z.iloc[cov[cov['SDx'] == 3].index, :].mean(axis=0)

   .. code-tab:: matlab **Matlab** | mega

        % Z-score patients' data relative to controls (lower z-score = more atrophy)
        group        = cov.Dx;
        controlCode  = 0;
        SV_z         = zscore_matrix(metr1_SubVol_r(:, 2:end-1), group, controlCode);
        CT_z         = zscore_matrix(metr2_CortThick(:, 2:end-5), group, controlCode);
        SA_z         = zscore_matrix(metr3_CortSurf(:, 2:end-5), group, controlCode);

        % Mean z-score values across individuals with from a specific group (e.g., left TLE, that is SDx == 3)
        SV_z_mean    = array2table(mean(SV_z{find(cov.SDx == 3), :}, 1), ...
                                   'VariableNames', SV_z.Properties.VariableNames);
        CT_z_mean    = array2table(mean(CT_z{find(cov.SDx == 3), :}, 1), ...
                                   'VariableNames', CT_z.Properties.VariableNames);
        SA_z_mean    = array2table(mean(SA_z{find(cov.SDx == 3), :}, 1), ...
                                   'VariableNames', SA_z.Properties.VariableNames);