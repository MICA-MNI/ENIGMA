.. _load_sumstats:

.. title:: Load summary statistics

Summary statistics
======================================

This page contains descriptions and examples to load case-control datasets from 
several ENIGMA Working Groups. These ENIGMA summary statistics contain the following data: **effect sizes 
for case-control differences** (d_icv), **standard error** (se_icv), **lower bound of the confidence interval** 
(low_ci_icv), **upper bound of the confidence interval** (up_ci_icv), **number of controls** (n_controls), 
**number of patiens** (n_patients), **observed p-values** (pobs), **false discovery rate (FDR)-corrected p-value** (fdr_p).

.. admonition:: Can't find the data you're searching for? 🙈

     Let us know what's missing and we'll try and fetch that data for you and implement it in our toolbox. 
     Get in touch with us `here <https://github.com/MICA-MNI/ENIGMA/issues>`_.


\* 📸 *indicates case-control tables used in the code snippets.*

22q11.2 deletion syndrome
-----------------------------------------
| **Available summary statistics tables**
| ↪ CortThick_case_vs_controls 📸
| ↪ CortSurf_case_vs_controls 📸
| ↪ CortThick_psychP_vs_psychN
| ↪ CortSurf_psychP_vs_psychN

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
| **Available summary statistics tables**
| ↪ CortThick_case_vs_controls_allages 
| ↪ CortSurf_case_vs_controls_allages
| ↪ CortThick_case_vs_controls_adult 📸
| ↪ CortSurf_case_vs_controls_adult 📸
| ↪ CortThick_case_vs_controls_adolescent
| ↪ CortSurf_case_vs_controls_adolescent
| ↪ CortThick_case_vs_controls_pediatric
| ↪ CortSurf_case_vs_controls_pediatric

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


Autism spectrum disorder
-------------------------------------
| **Available summary statistics tables**
| ↪ CortThick_case_vs_controls_meta_analysis 📸
| ↪ CortThick_case_vs_controls_mega_analysis

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
| **Available summary statistics tables**
| ↪ CortSurf_case_vs_controls 📸

.. tabs::

   .. code-tab:: py **Python** | meta

        >>> from enigmatoolbox.datasets import load_summary_stats

        >>> # Load summary statistics for ENIGMA-BD
        >>> sum_stats = load_summary_stats('bipolar')

        >>> # Get case-control surface area table
        >>> SA = sum_stats['CortSurf_case_vs_controls']

        >>> # Extract Cohen's d values
        >>> SA_d = SA['d_icv']

   .. code-tab:: matlab **Matlab** | meta

        % Load summary statistics for ENIGMA-BD
        sum_stats = load_summary_stats('bipolar');

        % Get case-control surface area table
        SA = sum_stats.CortSurf_case_vs_controls;

        % Extract Cohen's d values
        SA_d = SA.d_icv;


|


Epilepsy
----------------------------
| **Available summary statistics tables**
| ↪ CortThick_case_vs_controls_allepilepsy
| ↪ SubVol_case_vs_controls_allepilepsy
| ↪ CortThick_case_vs_controls_gge
| ↪ SubVol_case_vs_controls_gge
| ↪ CortThick_case_vs_controls_ltle 📸
| ↪ SubVol_case_vs_controls_ltle 📸
| ↪ CortThick_case_vs_controls_rtle
| ↪ SubVol_case_vs_controls_rtle

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


Major depressive disorder
----------------------------------
| **Available summary statistics tables**
| ↪ CortThick_case_vs_controls_adult 📸
| ↪ CortSurf_case_vs_controls_adult 📸
| ↪ CortThick_case_vs_controls_adolescent
| ↪ CortSurf_case_vs_controls_adolescent

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
        CT = sum_stats.CortThick_case_vs_controls_adult;
        SA = sum_stats.CortSurf_case_vs_controls_adult;

        % Extract Cohen's d values
        CT_d = CT.d_icv;
        SA_d = SA.d_icv;


|


Obsessive-compulsive disorder
-----------------------------------------
| **Available summary statistics tables**
| ↪ CortThick_case_vs_controls_adult 📸
| ↪ CortSurf_case_vs_controls_adult 📸
| ↪ CortThick_medicatedcase_vs_controls_adult
| ↪ CortSurf_medicatedcase_vs_controls_adult
| ↪ CortThick_case_vs_controls_pediatric
| ↪ CortSurf_case_vs_controls_pediatric
| ↪ CortThick_medicatedcase_vs_controls_pediatric
| ↪ CortSurf_medicatedcase_vs_controls_pediatric

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
| **Available summary statistics tables**
| ↪ CortThick_case_vs_controls 📸
| ↪ CortSurf_case_vs_controls 📸

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

