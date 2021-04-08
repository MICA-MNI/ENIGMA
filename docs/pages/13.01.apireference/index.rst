.. _apireferencelist:

.. title:: List of every function


.. raw:: html

   <style type="text/css">
      hr {
      width: 100%;
      height: 1px;
      background-color: #259595;
      margin-top: 24px;
      }
   </style>


Python API
======================

This is the function reference of the **ENIGMA TOOLBOX**

.. raw:: html

   <hr>

.. _pyref_datasets:

:mod:`enigmatoolbox.datasets`
-------------------------------------------------
.. automodule:: enigmatoolbox.datasets
   :no-members:
   :no-inherited-members:

.. currentmodule:: enigmatoolbox.datasets

ENIGMA datasets
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autosummary::
   :template: function.rst
   :toctree: generated/

   enigmatoolbox.datasets.load_example_data
   enigmatoolbox.datasets.load_summary_stats


Export functions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autosummary::
   :template: function.rst
   :toctree: generated/

   enigmatoolbox.datasets.nfaces
   enigmatoolbox.datasets.getaffine
   enigmatoolbox.datasets.write_cifti


Connectivity matrices
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autosummary::
   :template: function.rst
   :toctree: generated/

   enigmatoolbox.datasets.load_fc
   enigmatoolbox.datasets.load_fc_as_one
   enigmatoolbox.datasets.load_sc
   enigmatoolbox.datasets.load_sc_as_one

Gene co-expression data
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autosummary::
   :template: function.rst
   :toctree: generated/

   enigmatoolbox.datasets.fetch_ahba
   enigmatoolbox.datasets.risk_genes

.. Surface data
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
   .. autosummary::
      :template: function.rst
      :toctree: generated/
      enigmatoolbox.datasets.load_mask

Surface templates
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autosummary::
   :template: function.rst
   :toctree: generated/

   enigmatoolbox.datasets.load_fsa5
   enigmatoolbox.datasets.load_conte69
   enigmatoolbox.datasets.load_subcortical

.. raw:: html

   <hr>

.. _pyref_crossdis:

:mod:`enigmatoolbox.cross_disorder`
-------------------------------------------------
.. automodule:: enigmatoolbox.cross_disorder
   :no-members:
   :no-inherited-members:

.. currentmodule:: enigmatoolbox.cross_disorder

Cross-disorder effect
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autosummary::
   :template: function.rst
   :toctree: generated/

   enigmatoolbox.cross_disorder.cross_disorder_effect

.. raw:: html

   <hr>

.. _pyref_mesh:

:mod:`enigmatoolbox.mesh`
-------------------------------------------------
.. automodule:: enigmatoolbox.mesh
   :no-members:
   :no-inherited-members:

.. currentmodule:: enigmatoolbox.mesh

Read/write functionality
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autosummary::
   :template: function.rst
   :toctree: generated/

   enigmatoolbox.mesh.mesh_io.read_surface
   enigmatoolbox.mesh.mesh_io.write_surface

.. raw:: html

   <hr>

.. _pyref_permtesting:

:mod:`enigmatoolbox.permutation_testing`
-------------------------------------------------
.. automodule:: enigmatoolbox.permutation_testing
   :no-members:
   :no-inherited-members:

.. currentmodule:: enigmatoolbox.permutation_testing

Spin permutations
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autosummary::
   :template: function.rst
   :toctree: generated/

   enigmatoolbox.permutation_testing.spin_test
   enigmatoolbox.permutation_testing.centroid_extraction_sphere
   enigmatoolbox.permutation_testing.rotate_parcellation
   enigmatoolbox.permutation_testing.perm_sphere_p

Shuf permutations
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autosummary::
   :template: function.rst
   :toctree: generated/

   enigmatoolbox.permutation_testing.shuf_test
 
.. raw:: html

   <hr>


.. _pyref_surfplot:

:mod:`enigmatoolbox.plotting.surface_plotting`
-------------------------------------------------
.. automodule:: enigmatoolbox.plotting.surface_plotting
   :no-members:
   :no-inherited-members:

.. currentmodule:: enigmatoolbox.plotting.surface_plotting

Surface plotting
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autosummary::
   :template: function.rst
   :toctree: generated/

   enigmatoolbox.plotting.surface_plotting.plot_cortical
   enigmatoolbox.plotting.surface_plotting.plot_subcortical
   enigmatoolbox.plotting.surface_plotting.build_plotter
   enigmatoolbox.plotting.surface_plotting.plot_surf

.. raw:: html

   <hr>


.. _pyref_contextmod:

:mod:`enigmatoolbox.histology`
-------------------------------------------------
.. automodule:: enigmatoolbox.histology
   :no-members:
   :no-inherited-members:

.. currentmodule:: enigmatoolbox.histology


BigBrain stratification
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autosummary::
   :template: function.rst
   :toctree: generated/

   enigmatoolbox.histology.bb_moments_raincloud
   enigmatoolbox.histology.bb_gradient_plot


von Economo-Koskinas stratification
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autosummary::
   :template: function.rst
   :toctree: generated/

   enigmatoolbox.histology.economo_koskinas_spider


.. _pyref_utils:

:mod:`enigmatoolbox.utils`
-------------------------------------------------
.. automodule:: enigmatoolbox.utils
   :no-members:
   :no-inherited-members:

.. currentmodule:: enigmatoolbox.utils


Re-order subcortical data matrix
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autosummary::
   :template: function.rst
   :toctree: generated/

   enigmatoolbox.utils.useful.reorder_sctx


Z-score data matrix
^^^^^^^^^^^^^^^^^^^^^^^

.. autosummary::
   :template: function.rst
   :toctree: generated/

   enigmatoolbox.utils.useful.zscore_matrix


Parcellation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autosummary::
   :template: function.rst
   :toctree: generated/

   enigmatoolbox.utils.parcellation.parcel_to_surface
   enigmatoolbox.utils.parcellation.surface_to_parcel
   enigmatoolbox.utils.parcellation.subcorticalvertices


.. raw:: html

   <hr>
