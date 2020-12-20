.. _cross_disorder:

.. title:: Cross-disorder effect

Cross-disorder effect
======================================

This page contains descriptions and examples to perform cross-disorder analyses to explore 
brain structural abnormalities that are common or different across disorders.



Principal component analysis
-----------------------------------------
We can explore shared and disease-specific morphometric signatures by applying a principal component 
analysis (PCA) to any combination of disease-specific summary statistics (or other pre-loaded ENIGMA-type data), 
resulting in shared latent components that can be used for further analysis.

.. tabs::

   .. code-tab:: py **Python** | meta

        >>> from enigmatoolbox.cross_disorder import cross_disorder_effect
        >>> import matplotlib.pyplot as plt

        >>> # Extract and visualize shared disorder effects
        >>> components, variance, names = cross_disorder_effect()

        >>> # Visualize eigenvalues in a scree plot
        >>> fig, ax = plt.subplots(1, figsize=(7, 6))
        >>> ax.plot(variance, lw=2, color='#A8221C', zorder=1)
        >>> ax.scatter(range(variance.size), variance, s=78, color='#A8221C',
        >>>            linewidth=1.5, edgecolor='w', zorder=3)
        >>> ax.set_xlabel('Components')
        >>> ax.set_ylabel('Eigenvalues')
        >>> ax.spines['top'].set_visible(False)
        >>> ax.spines['right'].set_visible(False)

        >>> plt.show()

   .. code-tab:: matlab **Matlab** | meta

        % Extract and visualize shared disorder effects
        [components, variance, ~, names] = cross_disorder_effect();

.. image:: ./examples/example_figs/pca.png
    :align: center


|


Cross-correlation matrix
------------------------------------------------------
We can also explore shared and disease-specific morphometric signatures by 
systematically cross-correlating patterns of brain structural abnormalities 
with any combination of summary statistics (or other pre-loaded ENIGMA-type data), 
resulting in a correlation matrix 

.. tabs::

   .. code-tab:: py **Python** | meta

        >>> from enigmatoolbox.cross_disorder import cross_disorder_effect

        >>> # Extract and visualize shared disorder effects
        >>> correlation_matrix, names = cross_disorder_effect(method='correlation')

   .. code-tab:: matlab **Matlab** | meta

        % Extract and visualize shared disorder effects
        [~, ~, correlation_matrix, names] = cross_disorder_effect('method', 'correlation');

.. image:: ./examples/example_figs/ccmatrix.png
    :align: center


