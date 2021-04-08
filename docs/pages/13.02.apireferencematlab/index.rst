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


.. _matlabref_importexport:

:mod:`import / export`
------------------------------------

.. toctree::
   :maxdepth: 1
   :hidden:

   generated/nfaces.rst
   generated/getaffine.rst
   generated/write_cifti.rst

.. list-table::
   :widths: 50 400
   :header-rows: 0

   * - :ref:`nfaces(surface_name, hemisphere)<nfaces_mat>`
     - Returns number of faces/triangles for a surface (author: @saratheriver)
   * - :ref:`getaffine(surface_name, hemisphere)<get_affine_mat>`
     - Returns vox2ras transform for a surface (author: @saratheriver)
   * - :ref:`write_cifti(data, varargin)<write_cifti_mat>`
     - Writes cifti file (authors: @NicoleEic, @saratheriver) 
  

.. _matlabref_connmatrix:

:mod:`connectivity matrices`
------------------------------------

.. toctree::
   :maxdepth: 1
   :hidden:

   generated/load_fc.rst
   generated/load_fc_as_one.rst
   generated/load_sc.rst
   generated/load_sc_as_one.rst

.. list-table::
   :widths: 25 400
   :header-rows: 0

   * - :ref:`load_fc()<load_fc_mat>`
     - Load functional connectivity data (author: @saratheriver)
   * - :ref:`load_fc_as_one()<load_fc_as_one_mat>`
     - Load functional connectivity data (cortical + subcortical in one matrix; author: @saratheriver)
   * - :ref:`load_sc()<load_sc_mat>`
     - Load structural connectivity data (author: @saratheriver)
   * - :ref:`load_sc_as_one()<load_sc_as_one_mat>`
     - Load structural connectivity data (cortical + subcortical in one matrix; author: @saratheriver)


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
   * - :ref:`risk_genes(disease)<risk_genes_mat>`
     - Outputs names of GWAS-derived risk genes for a given disorder


.. _matlabref_crossdisord:

:mod:`cross-disorder effect`
------------------------------------

.. toctree::
   :maxdepth: 1
   :hidden:

   generated/cross_disorder.rst

.. list-table::
   :widths: 25 400
   :header-rows: 0

   * - :ref:`cross_disorder_effect()<cross_disorder_mat>`
     - Cross-disorder effect (authors: @boyongpark, @saratheriver)  

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

   * - :ref:`spin_test(map1, map2, varargin)<spin_test_mat>`
     - Spin permutation (author: @saratheriver)
   * - :ref:`centroid_extraction_sphere(sphere_coords, annotfile)<centroid_extraction_sphere_mat>`
     - Extract centroids of a cortical parcellation on a surface sphere (authors: @frantisekvasa, @saratheriver)
   * - :ref:`rotate_parcellation(coord_l, coord_r, nrot)<rotate_parcellation_mat>`
     - Rotate parcellation (authors: @frantisekvasa, @saratheriver)
   * - :ref:`perm_sphere_p(x, y, perm_id, corr_type)<perm_sphere_p_mat>`
     - Generate a p-value for the spatial correlation between two parcellated cortical surface maps (authors: @frantisekvasa, @saratheriver)


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

   * - :ref:`shuf_test(map1, map2, varargin)<shuf_test_mat>`
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

   * - :ref:`plot_cortical(data, varargin)<plot_cortical_mat>`
     - Plot cortical surface with lateral and medial views (authors: @MICA-MNI, @saratheriver)
   * - :ref:`plot_subcortical(data, varargin)<plot_subcortical_mat>`
     - Plot subcortical surface with lateral and medial views (author: @saratheriver)

.. raw:: html

   <hr>


.. _matlabref_histology:

:mod:`histology`
------------------------------------

.. toctree::
   :maxdepth: 1
   :hidden:

   generated/bb_moments_raincloud.rst
   generated/bb_gradient_plot.rst
   generated/economo_koskinas_spider.rst

.. list-table::
   :widths: 50 400
   :header-rows: 0

   * - :ref:`bb_moments_raincloud(region_idx, title)<bb_moments_raincloud_mat>`
     - Stratify regional data according to BigBrain statistical moments (authors: @caseypaquola, @saratheriver)
   * - :ref:`bb_gradient_plot(data, varargin)<bb_gradient_plot_mat>`
     - Stratify parcellated data according to the BigBrain gradient (authors: @caseypaquola, @saratheriver)
   * - :ref:`economo_koskinas_spider(parcel_data, varargin)<economo_koskinas_spider_mat>`
     - Stratify parcellated data according to von Economo-Koskinas cytoarchitectonic classes (authors: @caseypaquola, @saratheriver)

.. raw:: html

   <hr>


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

   * - :ref:`reorder_sctx(data)<reorder_sctx_mat>`
     - Re-order subcortical volume data alphabetically and by hemisphere (left then rightl; author: @saratheriver)


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

   * - :ref:`zscore_matrix(data, group, controlCode)<zscore_matrix_mat>`
     - Z-score data relative to a given group (author: @saratheriver)


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

   * - :ref:`parcel_to_surface(parcel_data, parcellation, fill)<parcel_to_surface_mat>`
     - Map parcellated data to the surface (authors : @MICA-MNI, @saratheriver)
   * - :ref:`surface_to_parcel(surf_data, parcellation)<surface_to_parcel_mat>`
     - Map surface data to a parcellation (authors : @MICA-MNI, @saratheriver)



