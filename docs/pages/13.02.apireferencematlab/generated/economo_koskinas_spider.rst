.. _apireferencelist_eco_kos:

.. title:: Matlab API | economo_koskinas_spider

.. _economo_koskinas_spider_mat:

economo_koskinas_spider()
------------------------------------

**Usage** [`source <https://github.com/MICA-MNI/ENIGMA/blob/master/matlab/scripts/histology/economo_koskinas_spider.m>`_]:
    .. function:: 
        class_mean = economo_koskinas_spider(parcel_data, varargin)

**Description**:
    Stratify parcellated data according to von Economo-Koskinas cytoarchitectonic classes (authors: @caseypaquola, @saratheriver)

**Inputs**:
    - **parcel_data** (*double array*) – vector of data. Parcellated data.

**Name/value pairs**:
    - **parcellation** (*string, optional*) - Parcellation to go from parcel_data to surface. Default is 'aparc_fsa5'.
    - **fill** (*double, optional*) - Value for mask. Default is 0.
    - **title** (*string, optional*) – Title of spider plot. Default is empty.
    - **axis_range** (*double array, optional*) - Range of spider plot axes. Default is (min, max).
    - **label** (*cell array, optional*) - List of axis labels. Length = 5. Default is names of von Economo-Koskinas cytoarchitectonic classes.
    - **color** (*double array, optional*) - Color of line. Default is [0 0 0].

**Outputs**:
    - **figure** (*figure*) – Spider plot.