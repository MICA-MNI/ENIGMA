.. _load_sumstats:

.. title:: Load summary statistics! 📂

Load summary statistics
======================================

This page contains descriptions and examples to load case-control datasets from 
several ENIGMA Working Groups!

.. admonition:: Can't find the data you're searching for? 🙈

     Let us know what's missing and we'll try and fetch that data for you and implement it in our toolbox! 
     Get in touch with us `here <https://github.com/MICA-MNI/ENIGMA/issues>`_!


|


22q11.2 deletion syndrome
-----------------------------------------

.. tabs::

   .. code-tab:: py **Python** | meta

        >>> from enigmatoolbox.datasets import load_summary_stats

        >>> # Load summary statistics for ENIGMA-22q
        >>> sum_stats = load_summary_stats('22q')

        >>> # List available summary statistic tables
        >>> for table_name in sum_stats:
        >>>     print(table_name)

        CortThick_case_vs_controls
        CortSurf_case_vs_controls
        CortThick_psychP_vs_psychN
        CortSurf_psychP_vs_psychN

   .. code-tab:: matlab **Matlab** | meta

        % Add the path to the ENIGMA TOOLBOX matlab folder
        addpath(genpath('/path/to/ENIGMA/matlab/'));

        % Load summary statistics for ENIGMA-22q
        sum_stats = load_summary_stats('22q');

        % List available summary statistic tables
        sum_stats

        CortThick_case_vs_controls: [68×10 table]
        CortSurf_case_vs_controls: [68×10 table]
        CortThick_psychP_vs_psychN: [68×10 table]
        CortSurf_psychP_vs_psychN: [68×10 table]


|


Attention deficit hyperactivity disorder
------------------------------------------------------

.. tabs::

   .. code-tab:: py **Python** | meta

        >>> from enigmatoolbox.datasets import load_summary_stats

        >>> # Load summary statistics for ENIGMA-ADHD
        >>> sum_stats = load_summary_stats('adhd')

        >>> # List available summary statistic tables
        >>> for table_name in sum_stats:
        >>>     print(table_name)

        CortThick_case_vs_controls_allages
        CortSurf_case_vs_controls_allages
        CortThick_case_vs_controls_adult
        CortSurf_case_vs_controls_adult
        CortThick_case_vs_controls_adolescent
        CortSurf_case_vs_controls_adolescent
        CortThick_case_vs_controls_pediatric
        CortSurf_case_vs_controls_pediatric

   .. code-tab:: matlab **Matlab** | meta

        % Add the path to the ENIGMA TOOLBOX matlab folder
        addpath(genpath('/path/to/ENIGMA/matlab/'));

        % Load summary statistics for ENIGMA-ADHD
        sum_stats = load_summary_stats('adhd');

        % List available summary statistic tables
        sum_stats

        CortThick_case_vs_controls_allages: [68×10 table]
        CortSurf_case_vs_controls_allages: [68×10 table]
        CortThick_case_vs_controls_adult: [68×10 table]
        CortSurf_case_vs_controls_adult: [68×10 table]
        CortThick_case_vs_controls_adolescent: [68×10 table]
        CortSurf_case_vs_controls_adolescent: [68×10 table]
        CortThick_case_vs_controls_pediatric: [68×10 table]
        CortSurf_case_vs_controls_pediatric: [68×10 table]


|


Autism spectrum disorder
-------------------------------------

.. tabs::

   .. code-tab:: py **Python** | meta

        >>> from enigmatoolbox.datasets import load_summary_stats

        >>> # Load summary statistics for ENIGMA-Autism
        >>> sum_stats = load_summary_stats('asd')

        >>> # List available summary statistic tables
        >>> for table_name in sum_stats:
        >>>     print(table_name)

        CortThick_case_vs_controls_meta_analysis
        CortThick_case_vs_controls_mega_analysis

   .. code-tab:: matlab **Matlab** | meta

        % Add the path to the ENIGMA TOOLBOX matlab folder
        addpath(genpath('/path/to/ENIGMA/matlab/'));

        % Load summary statistics for ENIGMA-Autism
        sum_stats = load_summary_stats('asd');

        % List available summary statistic tables
        sum_stats

        CortThick_case_vs_controls_meta_analysis: [68×10 table]
        CortThick_case_vs_controls_mega_analysis: [68×10 table]


|


Bipolar disorder
----------------------------

.. tabs::

   .. code-tab:: py **Python** | meta

        >>> from enigmatoolbox.datasets import load_summary_stats

        >>> # Load summary statistics for ENIGMA-BD
        >>> sum_stats = load_summary_stats('bipolar')

        >>> # List available summary statistic tables
        >>> for table_name in sum_stats:
        >>>     print(table_name)

        CortSurf_case_vs_controls

   .. code-tab:: matlab **Matlab** | meta

        % Add the path to the ENIGMA TOOLBOX matlab folder
        addpath(genpath('/path/to/ENIGMA/matlab/'));

        % Load summary statistics for ENIGMA-BD
        sum_stats = load_summary_stats('bipolar');

        % List available summary statistic tables
        sum_stats

        CortSurf_case_controls: [68×10 table]


|


Epilepsy
----------------------------

.. tabs::

   .. code-tab:: py **Python** | meta

        >>> from enigmatoolbox.datasets import load_summary_stats

        >>> # Load summary statistics for ENIGMA-Epilepsy
        >>> sum_stats = load_summary_stats('epilepsy')

        >>> # List available summary statistic tables
        >>> for table_name in sum_stats:
        >>>     print(table_name)

        CortThick_case_vs_controls_allepilepsy
        SubVol_case_vs_controls_allepilepsy
        CortThick_case_vs_controls_gge
        SubVol_case_vs_controls_gge
        CortThick_case_vs_controls_ltle
        SubVol_case_vs_controls_ltle
        CortThick_case_vs_controls_rtle
        SubVol_case_vs_controls_rtle

   .. code-tab:: matlab **Matlab** | meta

        % Add the path to the ENIGMA TOOLBOX matlab folder
        addpath(genpath('/path/to/ENIGMA/matlab/'));

        % Load summary statistics for ENIGMA-Epilepsy
        sum_stats = load_summary_stats('epilepsy');

        % List available summary statistic tables
        sum_stats

        CortThick_case_vs_controls_allepilepsy: [68×10 table]
        SubVol_case_vs_controls_allepilepsy: [16×10 table]
        CortThick_case_vs_controls_gge: [68×10 table]
        SubVol_case_vs_controls_gge: [16×10 table]
        CortThick_case_vs_controls_ltle: [68×10 table]
        SubVol_case_vs_controls_ltle: [16×10 table]
        CortThick_case_vs_controls_rtle: [68×10 table]
        SubVol_case_vs_controls_rtle: [16×10 table]


|


Major depressive disorder
----------------------------------

.. tabs::

   .. code-tab:: py **Python** | meta

        >>> from enigmatoolbox.datasets import load_summary_stats

        >>> # Load summary statistics for ENIGMA-MDD
        >>> sum_stats = load_summary_stats('depression')

        >>> # List available summary statistic tables
        >>> for table_name in sum_stats:
        >>>     print(table_name)

        CortThick_case_vs_controls_adult
        CortSurf_case_vs_controls_adult
        CortThick_case_vs_controls_adolescent
        CortSurf_case_vs_controls_adolescent

   .. code-tab:: matlab **Matlab** | meta

        % Add the path to the ENIGMA TOOLBOX matlab folder
        addpath(genpath('/path/to/ENIGMA/matlab/'));

        % Load summary statistics for ENIGMA-MDD
        sum_stats = load_summary_stats('depression');

        % List available summary statistic tables
        sum_stats

        CortThick_case_vs_controls_adult: [68×10 table]
        CortSurf_case_vs_controls_adult: [68×10 table]
        CortThick_case_vs_controls_adolescent: [68×10 table]
        CortSurf_case_vs_controls_adolescent: [68×10 table]


|


Obsessive-compulsive disorder
-----------------------------------------

.. tabs::

   .. code-tab:: py **Python** | meta

        >>> from enigmatoolbox.datasets import load_summary_stats

        >>> # Load summary statistics for ENIGMA-OCD
        >>> sum_stats = load_summary_stats('ocd')

        >>> # List available summary statistic tables
        >>> for table_name in sum_stats:
        >>>     print(table_name)

        CortThick_case_vs_controls_adult
        CortSurf_case_vs_controls_adult
        CortThick_medicatedcase_vs_controls_adult
        CortSurf_medicatedcase_vs_controls_adult
        CortThick_case_vs_controls_pediatric
        CortSurf_case_vs_controls_pediatric
        CortThick_medicatedcase_vs_controls_pediatric
        CortSurf_medicatedcase_vs_controls_pediatric

   .. code-tab:: matlab **Matlab** | meta

        % Add the path to the ENIGMA TOOLBOX matlab folder
        addpath(genpath('/path/to/ENIGMA/matlab/'));

        % Load summary statistics for ENIGMA-OCD
        sum_stats = load_summary_stats('ocd');

        % List available summary statistic tables
        sum_stats

        CortThick_case_vs_controls_adult: [68×10 table]
        CortSurf_case_vs_controls_adult: [68×10 table]
        CortThick_medicatedcase_vs_controls_adult: [68×10 table]
        CortSurf_medicatedcase_vs_controls_adult: [68×10 table]
        CortThick_case_vs_controls_pediatric: [68×10 table]
        CortSurf_case_vs_controls_pediatric: [68×10 table]
        CortThick_medicatedcase_vs_controls_pediatric: [68×10 table]
        CortSurf_medicatedcase_vs_controls_pediatric: [68×10 table]


|


Schizophrenia
----------------------------

.. tabs::

   .. code-tab:: py **Python** | meta

        >>> from enigmatoolbox.datasets import load_summary_stats

        >>> # Load summary statistics for ENIGMA-Schizophrenia
        >>> sum_stats = load_summary_stats('schizophrenia')

        >>> # List available summary statistic tables
        >>> for table_name in sum_stats:
        >>>     print(table_name)

        CortThick_case_vs_controls
        CortSurf_case_vs_controls

   .. code-tab:: matlab **Matlab** | meta

        % Add the path to the ENIGMA TOOLBOX matlab folder
        addpath(genpath('/path/to/ENIGMA/matlab/'));

        % Load summary statistics for ENIGMA-Schizophrenia
        sum_stats = load_summary_stats('schizophrenia');

        % List available summary statistic tables
        sum_stats

        CortThick_case_vs_controls: [68×10 table]
        CortSurf_case_vs_controls: [68×10 table]
