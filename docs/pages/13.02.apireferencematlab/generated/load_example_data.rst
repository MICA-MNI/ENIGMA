.. _apireferencelist_mat_load_example_data:

.. title:: Matlab API | load_example_data

.. _load_example_data_mat:

load_example_data()
------------------------------

**Usage** [`source <https://github.com/MICA-MNI/ENIGMA/blob/master/matlab/scripts/example_data/load_example_data.m>`_]:
    .. function:: 
        [cov, metr1_SubVol, metr2_CortThick, metr3_CortSurf] = load_example_data()

**Description:**
    Loads the ENIGMA example dataset (from one site - MICA-MNI Montreal; author: @saratheriver)

**Outputs:**
    - **cov** (*table*) – Contains information on covariates
    - **metr1** (*table*) – Contains information on subcortical volume
    - **metr2** (*table*) – Contains information on cortical thickness
    - **metr3** (*table*) – Contains information on surface area