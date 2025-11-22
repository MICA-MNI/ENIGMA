.. _load_sumstats:

.. title:: Load summary statistics

Summary statistics
======================================

This page contains descriptions and examples to load case-control datasets from 
several ENIGMA Working Groups. These ENIGMA summary statistics contain the following data: **effect sizes 
for case-control differences** (d_icv), **standard error** (se_icv), **lower bound of the confidence interval** 
(low_ci_icv), **upper bound of the confidence interval** (up_ci_icv), **number of controls** (n_controls), 
**number of patiens** (n_patients), **observed p-values** (pobs), **false discovery rate (FDR)-corrected p-value** (fdr_p).

ENIGMA’s standardized protocols for data processing, quality assurance, and meta-analysis of individual subject data were 
conducted at each site. For site-level meta-analysis, all research centres within a given specialized Working Group tested 
for case *vs*. control differences using multiple linear regressions, where diagnosis (*e.g.*, healthy controls vs. individuals 
with epilepsy) was the predictor of interest, and subcortical volume, cortical thickness, or surface area of a given brain region 
was the outcome measure. Case-control differences were computed across all regions using either Cohen’s *d* effect sizes or *t*-values, 
after adjusting for different combinations of age, sex, site/scan/dataset, intracranial volume, IQ (see below for disease-specific 
models).  

.. admonition:: Can't find the data you're searching for? 🙈

     Let us know what's missing and we'll try and fetch that data for you and implement it in our toolbox. 
     Get in touch with us `here <https://github.com/MICA-MNI/ENIGMA/issues>`_. If you have locally stored 
     summary statistics on your computer, check out our tutorials on :ref:`how to import data <import_data>`
     and accordingly take advantage of all the **ENIGMA TOOLBOX** functions.


\* 📸 *indicates case-control tables used in the code snippets.*

22q11.2 deletion syndrome
-----------------------------------------
Available summary statistics tables
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

| **From** `Sun et al., 2020, Mol Psychiatry <https://www.nature.com/articles/s41380-018-0078-5>`_  |  **age, sex, data set/site, and ICV\* correction; FDR correction available**
| *\*only for surface area measures*
|    ↪ CortThick_case_vs_controls 📸
|    ↪ CortSurf_case_vs_controls 📸
|    ↪ CortThick_psychP_vs_psychN  (+/- psychosis)
|    ↪ CortSurf_psychP_vs_psychN  (+/- psychosis)
|
| **From** `Ching et al., 2020, Am J Psychiatry <https://ajp.psychiatryonline.org/doi/10.1176/appi.ajp.2019.19060583>`_  |  **age, age^2, sex, scan site, and ICV correction; FDR correction available**
|    ↪ SubVol_case_vs_controls
|    ↪ SubVol_case_vs_controls_AD (A-D deletion)
|    ↪ SubVol_case_vs_controls_AB (A-B deletion)
|    ↪ SubVol_AB_vs_AD 
|    ↪ SubVol_psychP_vs_psychN (+/- psychosis)

.. tabs::

   .. code-tab:: py **Python** | meta

        >>> from enigmatoolbox.datasets import load_summary_stats

        >>> # Load summary statistics for ENIGMA-22q
        >>> sum_stats = load_summary_stats('22q')

        >>> # Get case-control cortical thickness and surface area tables
        >>> CT = sum_stats['CortThick_case_vs_controls']
        >>> SA = sum_stats['CortSurf_case_vs_controls']

        >>> # Extract Cohen's d values
        >>> CT_d = CT['d_icv']
        >>> SA_d = SA['d_icv']

   .. code-tab:: matlab **Matlab** | meta

        % Load summary statistics for ENIGMA-22q
        sum_stats = load_summary_stats('22q');

        % Get case-control cortical thickness and surface area tables
        CT = sum_stats.CortThick_case_vs_controls;
        SA = sum_stats.CortSurf_case_vs_controls;

        % Extract Cohen's d values
        CT_d = CT.d_icv;
        SA_d = SA.d_icv;


|

Attention deficit hyperactivity disorder
------------------------------------------------------
Available summary statistics tables
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

| **From** `Hoogman et al., 2019, Am J Psychiatry <https://ajp.psychiatryonline.org/doi/full/10.1176/appi.ajp.2019.18091033>`_  |  **mega-analysis; age, sex, and ICV\* correction; FDR correction available**
| *\*only for surface area measures*
|    **ALL AGES**
|    ↪ CortThick_case_vs_controls_allages 
|    ↪ CortSurf_case_vs_controls_allages
|
|    **ADULTS** (*age 22-63 years*)
|    ↪ CortThick_case_vs_controls_adult 📸
|    ↪ CortSurf_case_vs_controls_adult 📸
|
|    **ADOLESCENTS** (*age 15-21 years*)
|    ↪ CortThick_case_vs_controls_adolescent
|    ↪ CortSurf_case_vs_controls_adolescent
|
|    **CHILDREN** (*age 4-14 years*)
|    ↪ CortThick_case_vs_controls_pediatric
|    ↪ CortSurf_case_vs_controls_pediatric
|
| **From** `Hoogman et al., 2017, Lancet Psychiatry <https://www.thelancet.com/journals/lanpsy/article/PIIS2215-0366(17)30049-4/fulltext>`_  |  **mega-analysis; age, sex, ICV, and site correction; p<0.0156 for FDR correction at q=0.05; mean [(left+right)/2] region of interest volume**
|    **ALL AGES**
|    ↪ SubVol_case_vs_controls_allages 
|
|    **ADULTS** (*age≥22 years*)
|    ↪ SubVol_case_vs_controls_adult
|
|    **ADOLESCENTS** (*age 15-21 years*)
|    ↪ SubVol_case_vs_controls_adolescent
|
|    **CHILDREN** (*age⩽14 years*)
|    ↪ SubVol_case_vs_controls_pediatric

.. tabs::

   .. code-tab:: py **Python** | meta

        >>> from enigmatoolbox.datasets import load_summary_stats

        >>> # Load summary statistics for ENIGMA-ADHD
        >>> sum_stats = load_summary_stats('adhd')

        >>> # Get case-control cortical thickness and surface area tables
        >>> CT = sum_stats['CortThick_case_vs_controls_adult']
        >>> SA = sum_stats['CortSurf_case_vs_controls_adult']

        >>> # Extract Cohen's d values
        >>> CT_d = CT['d_icv']
        >>> SA_d = SA['d_icv']

   .. code-tab:: matlab **Matlab** | meta

        % Load summary statistics for ENIGMA-ADHD
        sum_stats = load_summary_stats('adhd');

        % Get case-control cortical thickness and surface area tables
        CT = sum_stats.CortThick_case_vs_controls_adult;
        SA = sum_stats.CortSurf_case_vs_controls_adult;

        % Extract Cohen's d values
        CT_d = CT.d_icv;
        SA_d = SA.d_icv;

|

Anorexia Nervosa
-------------------------------------
Available summary statistics tables
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

| **From** `Walton et al., 2022, Biological Psychiatry <https://www.biologicalpsychiatryjournal.com/article/S0006-3223(22)01290-2/abstract>`_  |  **See paper for specific model corrections; FDR correction available**
|    **ANOREXIA VS CONTROLS**
|    ↪ CortThick_anorexia_case_controls 📸
|    ↪ CortSurf_anorexia_case_controls
|    ↪ SubVol_anorexia_case_controls
|
|    **ANOREXIA VS CONTROLS, INCLUDING GLOBAL MEAN CT OR TOTAL SA AS COVARIATES**
|    ↪ CortThick_anorexia_case_controls_wGlo
|    ↪ CortSurf_anorexia_case_controls_wGlo
|
|    **ACUTELY ILL WITH ANOREXIA NERVOSA (acAN) VS CONTROLS**
|    ↪ CortThick_anorexia_acAN_controls
|    ↪ CortSurf_anorexia_acAN_controls
|    ↪ SubVol_anorexia_acAN_controls
|
|    **ACUTELY ILL WITH ANOREXIA NERVOSA (acAN) VS CONTROLS, INCLUDING GLOBAL MEAN CT OR TOTAL SA AS COVARIATES**
|    ↪ CortThick_anorexia_acAN_controls_wGlo
|    ↪ CortSurf_anorexia_acAN_controls_wGlo
|
|    **ACUTELY ILL WITH ANOREXIA NERVOSA (acAN) VS PARTIALLY WEIGHT-RESTORED PATIENTS WITH ANOREXIA NERVOSA (pwrAN)**
|    ↪ CortSurf_anorexia_acANpwrAN
|    ↪ CortThick_anorexia_acANpwrAN
|    ↪ SubVol_anorexia_acAN_pwrAN
|
|    **ACUTELY ILL WITH ANOREXIA NERVOSA (acAN) VS PARTIALLY WEIGHT-RESTORED PATIENTS WITH ANOREXIA NERVOSA (pwrAN), INCLUDING GLOBAL MEAN CT OR TOTAL SA AS COVARIATES**
|    ↪ CortThick_anorexia_acANpwrAN_wGlo
|    ↪ CortSurf_anorexia_acANpwrAN_wGlo
|
|    **PARTIALLY WEIGHT-RESTORED PATIENTS WITH ANOREXIA NERVOSA (pwrAN) VS CONTROLS**
|    ↪ CortSurf_anorexia_pwrAN_controls
|    ↪ CortThick_anorexia_pwrAN_controls
|    ↪ SubVol_anorexia_pwrAN_controls
|
|    **PARTIALLY WEIGHT-RESTORED PATIENTS WITH ANOREXIA NERVOSA (pwrAN) VS CONTROLS, INCLUDING GLOBAL MEAN CT OR TOTAL SA AS COVARIATES**
|    ↪ CortSurf_anorexia_pwrANcontrols_wGlo
|    ↪ CortThick_anorexia_pwrAN_controls_wGlo

.. tabs::

   .. code-tab:: py **Python** | meta

        >>> from enigmatoolbox.datasets import load_summary_stats

        >>> # Load summary statistics for ENIGMA-Eating Disorder (Anorexia Nervosa)
        >>> sum_stats = load_summary_stats('anorexia')

        >>> # Get case-control cortical thickness table
        >>> CT = sum_stats['CortThick_anorexia_case_controls']

        >>> # Extract Cohen's d values
        >>> CT_d = CT['d_icv']

   .. code-tab:: matlab **Matlab** | meta

        % Load summary statistics for ENIGMA-Eating Disorder (Anorexia Nervosa)
        sum_stats = load_summary_stats('anorexia');

        % Get case-control cortical thickness table
        CT = sum_stats.CortThick_anorexia_case_controls;

        % Extract Cohen's d values
        CT_d = CT.d_icv;

|

Antisocial
-------------------------------------
Available summary statistics tables
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

| **From** `Gao et al., 2024, The Lancet Psychiatry <https://www.thelancet.com/journals/lanpsy/article/PIIS2215-0366(24)00187-1/fulltext>`_  |  **age and sex correction (ICV correction in surface area and subcortical volume analyses); FDR correction available (q=0.05); mean\* [(left+right)/ 2)] region of interest measures**
| ↪ CortThick_case_controls_antisocial 📸
| ↪ CortSurf_case_controls_antisocial
| ↪ SubVol_case_controls_antisocial

.. tabs::

   .. code-tab:: py **Python** | meta

        >>> from enigmatoolbox.datasets import load_summary_stats

        >>> # Load summary statistics for ENIGMA-Antisocial Behavior
        >>> sum_stats = load_summary_stats('antisocial')

        >>> # Get case-control cortical thickness table
        >>> CT = sum_stats['CortThick_case_controls_antisocial']

        >>> # Extract Cohen's d values
        >>> CT_d = CT['d_icv']

   .. code-tab:: matlab **Matlab** | meta

        % Load summary statistics for ENIGMA-Antisocial Behavior
        sum_stats = load_summary_stats('antisocial');

        % Get case-control cortical thickness table
        CT = sum_stats.CortThick_case_controls_antisocial;

        % Extract Cohen's d values
        CT_d = CT.d_icv;

|

Autism spectrum disorder
-------------------------------------
Available summary statistics tables
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

| **From** `van Rooij et al., 2018, Am J Psychiatry <https://ajp.psychiatryonline.org/doi/10.1176/appi.ajp.2017.17010100>`_  |  **age, sex, IQ, and ICV\* correction; FDR correction available (uncorrected p-values not provided); mean\* [(left+right)/ 2)] region of interest volume**
| *\*only for subcortical volume measures*
| ↪ CortThick_case_vs_controls_meta_analysis 📸
| ↪ CortThick_case_vs_controls_mega_analysis
| ↪ SubVol_case_vs_controls_meta_analysis

.. tabs::

   .. code-tab:: py **Python** | meta

        >>> from enigmatoolbox.datasets import load_summary_stats

        >>> # Load summary statistics for ENIGMA-Autism
        >>> sum_stats = load_summary_stats('asd')

        >>> # Get case-control cortical thickness table
        >>> CT = sum_stats['CortThick_case_vs_controls_meta_analysis']

        >>> # Extract Cohen's d values
        >>> CT_d = CT['d_icv']

   .. code-tab:: matlab **Matlab** | meta

        % Load summary statistics for ENIGMA-Autism
        sum_stats = load_summary_stats('asd');

        % Get case-control cortical thickness table
        CT = sum_stats.CortThick_case_vs_controls_meta_analysis;

        % Extract Cohen's d values
        CT_d = CT.d_icv;

|

Bipolar disorder
----------------------------
Available summary statistics tables
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

| **From** `Hibar al., 2018, Mol Psychiatry <https://www.nature.com/articles/mp201773>`_   |  **age, sex, and ICV\* correction; FDR correction available**
| *\*only for surface area measures*
|    **ADULTS** (*age⩾25 years*)
|    ↪ CortThick_case_vs_controls_adult 📸
|    ↪ CortSurf_case_vs_controls_adult 📸
|    ↪ CortThick_typeI_vs_typeII_adult 
|    ↪ CortSurf_typeI_vs_typeII_adult 
|
|    **ADOLESCENTS/YOUNG ADULTS** (*age<25 years*)
|    ↪ CortThick_case_vs_controls_adolescent
|    ↪ CortSurf_case_vs_controls_adolescent
|    ↪ CortThick_typeI_vs_typeII_adolescent
|    ↪ CortSurf_typeI_vs_typeII_adolescent
|
| **From** `Hibar al., 2016, Mol Psychiatry <https://www.nature.com/articles/mp2015227>`_   |  **age, sex, and ICV correction; p<4.91E-3 for FDR correction at q=0.05; mean [(left+right)/2] region of interest volume**
|    ↪ SubVol_case_vs_controls_typeI
|    ↪ SubVol_case_vs_controls_typeII
|    ↪ SubVol_typeII_vs_typeI

.. tabs::

   .. code-tab:: py **Python** | meta

        >>> from enigmatoolbox.datasets import load_summary_stats

        >>> # Load summary statistics for ENIGMA-BD
        >>> sum_stats = load_summary_stats('bipolar')

        >>> # Get case-control surface area table
        >>> CT = sum_stats['CortThick_case_vs_controls_adult']
        >>> SA = sum_stats['CortSurf_case_vs_controls_adult']
        
        >>> # Extract Cohen's d values
        >>> CT_d = CT['d_icv']
        >>> SA_d = SA['d_icv']

   .. code-tab:: matlab **Matlab** | meta

        % Load summary statistics for ENIGMA-BD
        sum_stats = load_summary_stats('bipolar');

        % Get case-control surface area table
        CT = sum_stats.CortThick_case_vs_controls_adult;
        SA = sum_stats.CortSurf_case_vs_controls_adult;

        % Extract Cohen's d values
        CT_d = CT.d_icv;
        SA_d = SA.d_icv;

|

Brain Asymmetry
-------------------------------------
Available summary statistics tables
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

| **From** `Kong et al., 2018, PNAS <https://www.pnas.org/doi/full/10.1073/pnas.1718418115#supplementary-materials>`_  |  **See paper for specific model corrections; Same values are used in each hemisphere for visualization purposes**
|    **POPULATION LEVEL** 
|    ↪ CortThick_asymm_population_level 📸
|    ↪ CortSurf_asymm_population_level
|
|    **Effects of ICV** 
|    ↪ CortThick_asymm_ICVeffects 
|    ↪ CortSurf_asymm_ICVeffects
|
|    **Effects of handedness** 
|    ↪ CortThick_asymm_handedness-diff
|    ↪ CortSurf_asymm_handedness-diff
|
|    **Effects of age** 
|    ↪ CortThick_asymm_ageeffects
|    ↪ CortSurf_asymm_ageeffects
|    ↪ CortThick_asymm_ageeffects_20years
|    ↪ CortSurf_asymm_ageeffects_20years
|
|    **Effects of sex** 
|    ↪ CortThick_asymm_sexeffects
|    ↪ CortSurf_asymm_sexeffects

.. tabs::

   .. code-tab:: py **Python** | meta

        >>> from enigmatoolbox.datasets import load_summary_stats

        >>> # Load summary statistics for ENIGMA-Lateralization
        >>> sum_stats = load_summary_stats('asymmetry')

        >>> # Get case-control cortical thickness table
        >>> CT = sum_stats['CortThick_asymm_population_level']

        >>> # Extract Cohen's d values
        >>> CT_d = CT['d_icv']

   .. code-tab:: matlab **Matlab** | meta

        % Load summary statistics for ENIGMA-Lateralization
        sum_stats = load_summary_stats('asymmetry');

        % Get case-control cortical thickness table
        CT = sum_stats.CortThick_asymm_population_level;

        % Extract Cohen's d values
        CT_d = CT.d_icv;


|

Epilepsy
----------------------------
Available summary statistics tables
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

| **From** `Whelan al., 2018, Brain <https://academic.oup.com/brain/article/141/2/391/4818311>`_   |  **age, sex, and ICV correction; Bonferroni correction p<1.49E-4; FDR correction also available**
|    ↪ CortThick_case_vs_controls_allepilepsy
|    ↪ SubVol_case_vs_controls_allepilepsy
|    ↪ CortThick_case_vs_controls_gge
|    ↪ SubVol_case_vs_controls_gge
|    ↪ CortThick_case_vs_controls_ltle 📸
|    ↪ SubVol_case_vs_controls_ltle 📸
|    ↪ CortThick_case_vs_controls_rtle
|    ↪ SubVol_case_vs_controls_rtle
|    ↪ CortThick_case_vs_controls_allotherepilepsy
|    ↪ SubVol_case_vs_controls_allotherepilepsy

.. tabs::

   .. code-tab:: py **Python** | meta

        >>> from enigmatoolbox.datasets import load_summary_stats

        >>> # Load summary statistics for ENIGMA-Epilepsy
        >>> sum_stats = load_summary_stats('epilepsy')

        >>> # Get case-control subcortical volume and cortical thickness tables
        >>> SV = sum_stats['SubVol_case_vs_controls_ltle']
        >>> CT = sum_stats['CortThick_case_vs_controls_ltle']

        >>> # Extract Cohen's d values
        >>> SV_d = SV['d_icv']
        >>> CT_d = CT['d_icv']

   .. code-tab:: matlab **Matlab** | meta

        % Load summary statistics for ENIGMA-Epilepsy
        sum_stats = load_summary_stats('epilepsy');

        % Get case-control subcortical volume and cortical thickness tables
        SV = sum_stats.SubVol_case_vs_controls_ltle;
        CT = sum_stats.CortThick_case_vs_controls_ltle;

        % Extract Cohen's d values
        SV_d = SV.d_icv;
        CT_d = CT.d_icv;

|

Lifespan
-------------------------------------
Available summary statistics tables
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

| **From** `Frangou et al., 2021, Human Brain Mapping <https://onlinelibrary.wiley.com/doi/full/10.1002/hbm.25364>`_  |  **See paper for specific model corrections; Only Pearson's correlations are reported (not Cohen's d).**
|    **ALL** 
|    ↪ CortThick_agevsthick_all_3to29 📸
|    ↪ CortThick_agevsthick_all_30to59
|    ↪ CortThick_agevsthick_all_60to90
|
|    **FEMALES** 
|    ↪ CortThick_agevsthick_F_3to29
|    ↪ CortThick_agevsthick_F_30to59
|    ↪ CortThick_agevsthick_F_60to90
|
|    **MALES** 
|    ↪ CortThick_agevsthick_M_3to29
|    ↪ CortThick_agevsthick_M_30to59
|    ↪ CortThick_agevsthick_M_60to90

.. tabs::

   .. code-tab:: py **Python** | meta

        >>> from enigmatoolbox.datasets import load_summary_stats

        >>> # Load summary statistics for ENIGMA-Lifespan
        >>> sum_stats = load_summary_stats('lifespan')

        >>> # Get case-control cortical thickness table
        >>> CT = sum_stats['CortThick_agevsthick_all_3to29']

        >>> # Extract Pearson's correlation values
        >>> CT_d = CT['d_icv']

   .. code-tab:: matlab **Matlab** | meta

        % Load summary statistics for ENIGMA-Lifespan 
        sum_stats = load_summary_stats('lifespan');

        % Get case-control cortical thickness table
        CT = sum_stats.CortThick_agevsthick_all_3to29;

        % Extract Pearson's correlation values
        CT_d = CT.d_icv;

|

Major depressive disorder
----------------------------------
Available summary statistics tables
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

| **From** `Schmaal et al., 2017, Mol Psychiatry <https://www.nature.com/articles/mp201660#Sec2>`_   |  **age, sex, and scan site correction; FDR correction available**
|    **ADULTS** (*age>21 years*)
|    ↪ CortThick_case_vs_controls_adult 📸
|    ↪ CortSurf_case_vs_controls_adult 📸
|    ↪ CortThick_case_vs_controls_adult_firstepisode
|    ↪ CortSurf_case_vs_controls_adult_firstepisode
|    ↪ CortThick_case_vs_controls_adult_recurrent
|    ↪ CortSurf_case_vs_controls_adult_recurrent
|    ↪ CortThick_firstepisode_vs_recurrent_adult
|    ↪ CortSurf_firstepisode_vs_recurrent_adult
|    ↪ CortThick_case_vs_controls_adult_early (age of onset⩽21 years)
|    ↪ CortSurf_case_vs_controls_adult_early (age of onset⩽21 years)
|    ↪ CortThick_case_vs_controls_adult_late (age of onset>21 years)
|    ↪ CortSurf_case_vs_controls_adult_late (age of onset>21 years)
|    ↪ CortThick_early_vs_late_adult
|    ↪ CortSurf_early_vs_late_adult
|   
|    **ADOLESCENTS** (*age⩽21 years*)
|    ↪ CortThick_case_vs_controls_adolescent
|    ↪ CortSurf_case_vs_controls_adolescent
|    ↪ CortThick_case_vs_controls_adolescent_firstepisode
|    ↪ CortSurf_case_vs_controls_adolescent_firstepisode
|    ↪ CortThick_case_vs_controls_adolescent_recurrent
|    ↪ CortSurf_case_vs_controls_adolescent_recurrent
|    ↪ CortThick_firstepisode_vs_recurrent_adolescent
|    ↪ CortSurf_firstepisode_vs_recurrent_adolescent
|
| **From** `Schmaal et al., 2016, Mol Psychiatry <https://www.nature.com/articles/mp201569>`_  |  **age, sex, ICV, and scanner differences correction; Bonferroni correction p<5.6E-3; mean [(left+right)/2] region of interest volume**
|    ↪ SubVol_case_vs_controls
|    ↪ SubVol_case_vs_controls_late (age of onset>21 years)
|    ↪ SubVol_case_vs_controls_early (age of onset⩽21 years)
|    ↪ SubVol_late_vs_early
|    ↪ SubVol_case_vs_controls_firstepisode
|    ↪ SubVol_case_vs_controls_recurrent
|    ↪ SubVol_recurrrent_vs_firstepisode


.. tabs::

   .. code-tab:: py **Python** | meta

        >>> from enigmatoolbox.datasets import load_summary_stats

        >>> # Load summary statistics for ENIGMA-MDD
        >>> sum_stats = load_summary_stats('depression')

        >>> # Get case-control cortical thickness and surface area tables
        >>> CT = sum_stats['CortThick_case_vs_controls_adult']
        >>> SA = sum_stats['CortSurf_case_vs_controls_adult']

        >>> # Extract Cohen's d values
        >>> CT_d = CT['d_icv']
        >>> SA_d = SA['d_icv']

   .. code-tab:: matlab **Matlab** | meta

        % Load summary statistics for ENIGMA-MDD
        sum_stats = load_summary_stats('depression');

        % Get case-control cortical thickness and surface area tables
        SV = sum_stats.SubVol_case_vs_controls_adult;
        CT = sum_stats.CortThick_case_vs_controls_adult;
        SA = sum_stats.CortSurf_case_vs_controls_adult;

        % Extract Cohen's d values
        SV_d = SV.d_icv;
        CT_d = CT.d_icv;
        SA_d = SA.d_icv;


|


Obsessive-compulsive disorder
-----------------------------------------
Available summary statistics tables
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

| **From** `Boedhoe et al., 2018, Am J Psychiatry <https://ajp.psychiatryonline.org/doi/10.1176/appi.ajp.2017.17050485?url_ver=Z39.88-2003&rfr_id=ori:rid:crossref.org&rfr_dat=cr_pub%20%200pubmed>`_   |  **age, sex, scan site, and ICV\* correction; FDR correction available**
| *\*only for surface area measures*
|    **ADULTS** (*age≥18 years*)
|    ↪ CortThick_case_vs_controls_adult 📸
|    ↪ CortSurf_case_vs_controls_adult 📸
|    ↪ CortThick_medicatedcase_vs_controls_adult
|    ↪ CortSurf_medicatedcase_vs_controls_adult
|
|    **PEDIATRIC** (*age<18 years*)
|    ↪ CortThick_case_vs_controls_pediatric
|    ↪ CortSurf_case_vs_controls_pediatric
|    ↪ CortThick_medicatedcase_vs_controls_pediatric
|    ↪ CortSurf_medicatedcase_vs_controls_pediatric

| **From** `Boedhoe et al., 2017, Am J Psychiatry <https://ajp.psychiatryonline.org/doi/10.1176/appi.ajp.2016.16020201>`_   |  **age, sex, scan site, and ICV correction; Bonferroni correction p<5.6E-3; mean [(left+right)/2] region of interest volume**
|    **ADULTS** (*age≥18 years*)
|    ↪ SubVol_case_vs_controls_adult
|    ↪ SubVol_medicatedcase_vs_controls_adult
|    ↪ SubVol_unmedicatedcase_vs_controls_adult
|    ↪ SubVol_medicatedcase_vs_unmedicated_adult
|    ↪ SubVol_case_vs_controls_adult_late (age of onset≥18 years)
|    ↪ SubVol_case_vs_controls_adult_early (age of onset<18 years)
|    ↪ SubVol_late_vs_early_adult
|    ↪ SubVol_case_vs_controls_adult_depression (as comorbidity)
|    ↪ SubVol_case_vs_controls_adult_nodepression
|    ↪ SubVol_depression_vs_nodepression_adult
|    ↪ SubVol_case_vs_controls_adult_anxiety (as comorbidity)
|    ↪ SubVol_case_vs_controls_adult_noanxiety
|    ↪ SubVol_anxiety_vs_noanxiety_adult
|
|    **PEDIATRIC** (*age<18 years*)
|    ↪ SubVol_case_vs_controls_pediatric
|    ↪ SubVol_medicatedcase_vs_controls_pediatric
|    ↪ SubVol_unmedicatedcase_vs_controls_pediatric
|    ↪ SubVol_medicatedcase_vs_unmedicated_pediatric

.. tabs::

   .. code-tab:: py **Python** | meta

        >>> from enigmatoolbox.datasets import load_summary_stats

        >>> # Load summary statistics for ENIGMA-OCD
        >>> sum_stats = load_summary_stats('ocd')

        >>> # Get case-control cortical thickness and surface area tables
        >>> CT = sum_stats['CortThick_case_vs_controls_adult']
        >>> SA = sum_stats['CortSurf_case_vs_controls_adult']

        >>> # Extract Cohen's d values
        >>> CT_d = CT['d_icv']
        >>> SA_d = SA['d_icv']

   .. code-tab:: matlab **Matlab** | meta

        % Load summary statistics for ENIGMA-OCD
        sum_stats = load_summary_stats('ocd');

        % Get case-control cortical thickness and surface area tables
        CT = sum_stats.CortThick_case_vs_controls_adult;
        SA = sum_stats.CortSurf_case_vs_controls_adult;

        % Extract Cohen's d values
        CT_d = CT.d_icv;
        SA_d = SA.d_icv;


|


Schizophrenia
----------------------------
Available summary statistics tables
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

| **From** `van Erp et al., 2018, Biol Psychiatry <https://www.biologicalpsychiatryjournal.com/article/S0006-3223(18)31517-8/fulltext>`_   |  **age and sex correction; FDR correction available**
|    ↪ CortThick_case_vs_controls 📸
|    ↪ CortSurf_case_vs_controls 📸

| **From** `van Erp et al., 2016, Mol Psychiatry <https://www.nature.com/articles/mp201563#Tab1>`_   |  **age, sex, scan site, and ICV correction; Bonferroni correction p<5.6E-3**
|    ↪ SubVol_case_vs_controls
|    ↪ SubVol_case_vs_controls_mean (mean [(left+right)/ 2)] region of interest volume)

.. tabs::

   .. code-tab:: py **Python** | meta

        >>> from enigmatoolbox.datasets import load_summary_stats

        >>> # Load summary statistics for ENIGMA-Schizophrenia
        >>> sum_stats = load_summary_stats('schizophrenia')

        >>> # Get case-control cortical thickness and surface area tables
        >>> CT = sum_stats['CortThick_case_vs_controls']
        >>> SA = sum_stats['CortSurf_case_vs_controls']

        >>> # Extract Cohen's d values
        >>> CT_d = CT['d_icv']
        >>> SA_d = SA['d_icv']

   .. code-tab:: matlab **Matlab** | meta

        % Load summary statistics for ENIGMA-schizophrenia
        sum_stats = load_summary_stats('schizophrenia');
        
        % Get case-control cortical thickness and surface area tables
        CT = sum_stats.CortThick_case_vs_controls;
        SA = sum_stats.CortSurf_case_vs_controls;

        % Extract Cohen's d values
        CT_d = CT.d_icv;
        SA_d = SA.d_icv;

