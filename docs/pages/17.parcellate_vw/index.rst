.. _parc_vw:

.. title:: Vertexwise ↔ parcellated data

Vertexwise ↔ parcellated data 
============================================

This page contains descriptions and examples to (*i*) parcellate vertexwise data (sampled on fsaverage5 or conte69), allowing 
users to take advantage of every function within the **ENIGMA TOOLBOX**, and (*ii*) map parcellated data back to vertexwise 
space, allowing surface visualization of data and cross-software compatibility. 

.. _vw_to_parc:

Vertexwise → parcellated data
---------------------------------------------------

As an example, we parcellate vertexwise cortical thickness data imported in the :ref:`previous tutorial <import_data>` 
according to the Schaefer-200 atlas. Users can use this function to parcellate (fsaverage5 or conte69) vertexwise data using different parcellations, 
including: aparc_fsa5, glasser_fsa5, schaefer_100_fsa5, schaefer_200_fsa5, schaefer_300_fsa5, schaefer_400_fsa5, 
aparc_conte69, glasser_conte69, schaefer_100_conte69, schaefer_200_conte69, schaefer_300_conte69, schaefer_400_conte69.

.. tabs::

   .. code-tab:: py

        >>> from enigmatoolbox.utils.parcellation import surface_to_parcel

        >>> # Parcellate vertexwise data
        >>> CT_schaefer_200 = surface_to_parcel(CT, 'schaefer_200_conte69')

   .. code-tab:: matlab

        % Parcellate vertexwise data
        CT_schaefer_200 = surface_to_parcel(CT, 'schaefer_200_conte69');


|


.. _parc_to_vw:

Parcellated → vertexwise data
---------------------------------------------------

Mapping parcellated data to the surface has never been easier! Our ``parcel_to_surface()`` function works with ENIGMA- and non-ENIGMA datasets.
This function is especially useful for visualizing parcellated data on cortical surface templates using our :ref:`visualization tools <surf_visualization>` 
or other popular neuroimaging softwares (check out our tutorials on :ref:`how to export data <export_data>`).

As an example, we map the parcellated data from the :ref:`above tutorial <vw_to_parc>` back to the Conte69 surface. 

.. admonition:: Don't like conte69? Relax, we got you covered! 🛀🏾

     The same approach can be used to map parcellated data to the fsaverage5 surface template; simply replace every 'conte69' with 'fsa5'!

.. tabs::

   .. code-tab:: py

        >>> from enigmatoolbox.utils.parcellation import parcel_to_surface

        >>> # Map parcellated data to the surface
        >>> CT_schaefer_200_c69 = parcel_to_surface(CT_schaefer_200, 'schaefer_200_conte69')

   .. code-tab:: matlab

        % Map parcellated data to the surface
        CT_schaefer_200_c69 = parcel_to_surface(CT_schaefer_200, 'schaefer_200_conte69');