.. _cross_disorder:

.. title:: Cross-disorder effect

Cross-disorder effect
======================================

This page contains descriptions and examples to perform cross-disorder analyses to explore 
brain structural abnormalities that are common or different across disorders.



Principal component analysis
-----------------------------------------
Users can explore shared and disease-specific morphometric signatures by applying a principal component 
analysis (PCA) to any combination of disease-specific summary statistics (or other pre-loaded ENIGMA-type data), 
resulting in shared latent components that can be used for further analysis.

.. tabs::

   .. code-tab:: py **Python** | meta

        >>> from enigmatoolbox.datasets import load_summary_stats

        >>> # Explore
        >>> sum_stats = load_summary_stats('22q')

   .. code-tab:: matlab **Matlab** | meta

        % Load summary statistics for ENIGMA-22q
        sum_stats = load_summary_stats('22q');


|


Cross-correlation
------------------------------------------------------
Users can also explore shared and disease-specific morphometric signatures by 
systematically cross-correlating patterns of brain structural abnormalities 
with any combination of summary statistics (or other pre-loaded ENIGMA-type data), 
resulting in a correlation matrix 

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



