.. _apireferencelist_mat:

.. title:: Matlab API


.. raw:: html

   <style type="text/css">
      hr {
      width: 100%;
      height: 1px;
      background-color: #259595;
      margin-top: 24px;
      }
   </style>



Matlab API
==============

.. raw:: html

   <hr>

.. _matlabref_datasets:

:mod:`enigma datasets`
------------------------------------

.. toctree::
   :maxdepth: 1
   :hidden:

   generated/load_example_data.rst
   generated/load_summary_stats.rst

.. list-table::
   :widths: 50 400
   :header-rows: 0

   * - :ref:`load_example_data()<load_example_data_mat>`
     - Loads the ENIGMA example dataset (from one site - MICA-MNI Montreal; author: @saratheriver)
   * - :ref:`load_summary_stats(disorder)<load_sumstats_mat>`
     - Outputs summary statistics for a given disorder (author: @saratheriver)


.. _matlabref_connmatrix:

:mod:`connectivity matrices`
------------------------------------

.. toctree::
   :maxdepth: 1
   :hidden:

   generated/load_fc.rst
   generated/load_sc.rst

.. list-table::
   :widths: 25 400
   :header-rows: 0

   * - :ref:`load_fc()<load_fc_mat>`
     - Load functional connectivity data parcellated using Desikan Killiany (author: @saratheriver)
   * - :ref:`load_sc()<load_sc_mat>`
     - Load structural connectivity data parcellated using Desikan Killiany (author: @saratheriver)


.. _matlabref_genedata:

:mod:`gene co-expression data`
------------------------------------

.. toctree::
   :maxdepth: 1
   :hidden:

   generated/fetch_ahba.rst
   generated/risk_genes.rst

.. list-table::
   :widths: 25 400
   :header-rows: 0

   * - :ref:`fetch_ahba()<fetch_ahba_mat>`
     - Fetch Allen Human Brain Atlas microarray expression data from all donors and all genes (author: @saratheriver)
   * - :ref:`risk_genes()<risk_genes_mat>`
     - Outputs names of GWAS-derived risk genes for a given disorder


.. 
   .. _matlabref_surfdata:
   :mod:`surface data`
   ------------------------------------
   .. toctree::
      :maxdepth: 1
      :hidden:
      generated/load_mask.rst
   .. list-table::
      :widths: 100 200
      :header-rows: 0
      * - :ref:`load_mask()<load_mask_mat>`
      - Load mask for surface template (authors: @OualidBenkarim, @saratheriver)

.. 
   .. _matlabref_surftemplate:
   :mod:`surface templates`
   ------------------------------------
   .. toctree::
      :maxdepth: 1
      :hidden:
      generated/load_fsa5.rst
      generated/load_conte69.rst
      generated/load_subcortical.rst
   .. list-table::
      :widths: 50 400
      :header-rows: 0
      * - :ref:`load_fsa5()<load_fsa5_mat>`
      - Load fsaverage5 surfaces (author: @saratheriver)
      * - :ref:`load_conte69()<load_conte69_mat>`
      - Load conte69 surfaces (author: @OualidBenkarim)
      * - :ref:`load_subcortical()<load_subcortical_mat>`
      - Load subcortical surfaces (author: @saratheriver)


.. 
   .. raw:: html
      <hr>
   .. _matlabref_readwrite:
   :mod:`read/write functionality`
   ------------------------------------
   ...
   .. raw:: html
      <hr>

.. _matlabref_spinperm:

:mod:`spin permutations`
------------------------------------

.. toctree::
   :maxdepth: 1
   :hidden:

   generated/spin_test.rst
   generated/centroid_extraction_sphere.rst
   generated/rotate_parcellation.rst
   generated/perm_sphere_p.rst

.. list-table::
   :widths: 50 400
   :header-rows: 0

   * - :ref:`spin_test(...)<spin_test_mat>`
     - Spin permutation (author: @saratheriver)
   * - :ref:`centroid_extraction_sphere(...)<centroid_extraction_sphere_mat>`
     - Extract centroids of a cortical parcellation on a surface sphere (author: @saratheriver)
   * - :ref:`rotate_parcellation(...)<rotate_parcellation_mat>`
     - Rotate parcellation (author: @saratheriver)
   * - :ref:`perm_sphere_p(...)<perm_sphere_p_mat>`
     - Generate a p-value for the spatial correlation between two parcellated cortical surface maps (author: @saratheriver)


.. _matlabref_shufperm:

:mod:`shuf permutations`
------------------------------------

.. toctree::
   :maxdepth: 1
   :hidden:

   generated/shuf_test.rst

.. list-table::
   :widths: 50 400
   :header-rows: 0

   * - :ref:`shuf_test(...)<shuf_test_mat>`
     - Shuf permuation (author: @saratheriver)


.. raw:: html

   <hr>

.. _matlabref_surfplot:

:mod:`surface plotting`
------------------------------------

.. toctree::
   :maxdepth: 1
   :hidden:

   generated/plot_cortical.rst
   generated/plot_subcortical.rst

.. list-table::
   :widths: 50 400
   :header-rows: 0

   * - :ref:`plot_cortical()<plot_cortical_mat>`
     - Plot cortical surface with lateral and medial views (authors: @MICA-MNI, @saratheriver)
   * - :ref:`plot_subcortical()<plot_subcortical_mat>`
     - Plot subcortical surface with lateral and medial views (author: @saratheriver)

.. raw:: html

   <hr>

.. _matlabref_zscore:

:mod:`z-score data matrix`
------------------------------------

.. toctree::
   :maxdepth: 1
   :hidden:

   generated/zscore_matrix.rst

.. list-table::
   :widths: 50 400
   :header-rows: 0

   * - :ref:`zscore_matrix()<zscore_matrix_mat>`
     - Z-score data relative to a given group (author: @saratheriver)


.. _matlabref_reordsctx:

:mod:`re-order subcortical data matrix`
---------------------------------------------

.. toctree::
   :maxdepth: 1
   :hidden:

   generated/reorder_sctx.rst

.. list-table::
   :widths: 50 400
   :header-rows: 0

   * - :ref:`reorder_sctx()<reorder_sctx_mat>`
     - Re-order subcortical volume data alphabetically and by hemisphere (left then rightl; author: @saratheriver)


.. _matlabref_parcellation:

:mod:`parcellation`
------------------------------------

.. toctree::
   :maxdepth: 1
   :hidden:

   generated/parcel_to_surface.rst
   generated/surface_to_parcel.rst

.. list-table::
   :widths: 50 400
   :header-rows: 0

   * - :ref:`parcel_to_surface()<parcel_to_surface_mat>`
     - Map data in source to target according to their labels (author: @MICA-MNI)
   * - :ref:`surface_to_parcel()<surface_to_parcel_mat>`
     - Summarize data in values according to labels (author: @MICA-MNI)



