.. _export_data:

.. title:: Export data

Export data results
============================================

This page contains descriptions and examples to export data results across a range of file formats compatible with several neuroimaging software.
These include: :ref:`.txt/.csv <e_txt_csv>`, :ref:`FreeSurfer/"curv" <e_fs_curv>`, :ref:`.mgh/.mgz <e_mgh_mgz>`,
:ref:`GIfTI/.gii <e_gifti>`

As an example, we will export the vertexwise data from the :ref:`previous tutorial <parc_to_vw>`. The examples below can 
be easily modified to export any vertexwise (all formats) or parcellated (.txt/.csv format) data results by simply changing the data array to be saved, 
the data export path, and the filenames. Here, we exported cortical thickness data to the ENIGMA's import_export datasets directory.

.. admonition:: What about exporting brain surfaces? 🏄🏼‍♀️

     Exported data results can be mapped to the surface templates using several other neuroimaging software. Cortical and subcortical surfaces 
     are available `here <https://github.com/MICA-MNI/ENIGMA/tree/master/matlab/shared/surfaces>`_ in different file formats 
     (FreeSurfer/surface, GIfTI/.gii, .vtk, .obj).

.. _e_txt_csv:

.txt / .csv
---------------------------------------------------

If you want to export your data as text (.txt) or comma-separated values files, then you may use the ``writetable()`` (*Matlab*) or ``np.savetxt()`` (*Python*) 
functions. If your input data are in a table or dataframe, then you may remove the ``array2table()`` function  (*Matlab*) or use the ``.to_csv()`` function (*Python*) 
functions. 

.. tabs::

   .. code-tab:: py

        >>> import enigmatoolbox 
        >>> import numpy as np

        >>> # Specify data to be exported 
        >>> data = CT_schaefer_200_c69
        
        >>> # Define export path
        >>> data_path = os.path.join(os.path.dirname(enigmatoolbox.__file__) + "/datasets/import_export/")

        >>> # Define filenames for left and right hemisphere data
        >>> filename_lh = 'lh.schaefer_200_c69_thickness.txt'
        >>> filename_rh = 'rh.schaefer_200_c69_thickness.txt'

        >>> # Export cortical thickness data as .txt / .csv
        >>> np.savetxt(data_path + filename_lh, data[:len(data)//2])
        >>> np.savetxt(data_path + filename_rh, data[len(data)//2:])

   .. code-tab:: matlab

        % Specify data to be exported 
        data = CT_schaefer_200_c69

        % Define export path
        data_path = what('import_export'); data_path = data_path.path;
        
        % Define filenames for left and right hemisphere data
        filename_lh = 'lh.schaefer_200_c69_thickness.txt'
        filename_rh = 'rh.schaefer_200_c69_thickness.txt'

        % Export cortical thickness data as .txt / .csv
        writetable(array2table(data(1:end/2)), [data_path, filename_lh], 'WriteVariableNames', 0)
        writetable(array2table(datta(end/2+1:end)), [data_path, filename_rh], 'WriteVariableNames', 0)


|


.. _e_fs_curv:

FreeSurfer / "curv"
---------------------------------------------------

If you want to export your data as FreeSurfer "curv" format (*e.g.*, ?h.thickness), then you may use the ``write_curv()`` (*Matlab*) or 
``nib.freesurfer.io.write_morph_data()`` (*Python*) functions to load your data. 
You can get the Matlab function from `here <https://github.com/neurodebian/freesurfer>`_.

.. admonition:: What is this nfaces business? 🤖

     In the ``write_curv()`` and ``nib.freesurfer.io.write_morph_data()`` functions, users are required 
     to specify the number of faces (or triangles) in the associated surface file. To simplify things, 
     we built a simple function, ``nfaces()``, in which users can specify the surface name ('*conte69*', '*fsa5*') 
     and the hemisphere ('*lh*', '*rh*', '*both*') to obtain the appropriate number of faces.

.. tabs::

   .. code-tab:: py

        >>> import enigmatoolbox 
        >>> from enigmatoolbox.datasets import nfaces
        >>> import nibabel as nib

        >>> # Specify data to be exported 
        >>> data = CT_schaefer_200_c69
        
        >>> # Define export path
        >>> data_path = os.path.join(os.path.dirname(enigmatoolbox.__file__) + "/datasets/import_export/")

        >>> # Define filenames for left and right hemisphere data
        >>> filename_lh = 'lh.schaefer_200_c69_thickness'
        >>> filename_rh = 'rh.schaefer_200_c69_thickness'
        
        >>> # Export cortical thickness data as FreeSurfer "curv"
        >>> nib.freesurfer.io.write_morph_data(data_path + filename_lh, data[:len(data)//2], nfaces('conte69', 'lh'))
        >>> nib.freesurfer.io.write_morph_data(data_path + filename_rh, data[len(data)//2:], nfaces('conte69', 'rh'))


   .. code-tab:: matlab

        % Specify data to be exported 
        data = CT_schaefer_200_c69

        % Define export path
        data_path = what('import_export'); data_path = data_path.path;
        
        % Define filenames for left and right hemisphere data
        filename_lh = 'lh.schaefer_200_c69_thickness'
        filename_rh = 'rh.schaefer_200_c69_thickness'
        
        % Export cortical thickness data as FreeSurfer "curv"
        write_curv([data_path, filename_lh], data(1:end/2), nfaces('conte69', 'lh'));
        write_curv([data_path filename_rh], data(end/2+1:end), nfaces('conte69', 'rh'));


|


.. _e_mgh_mgz:

.mgh / .mgz
---------------------------------------------------

If you want to export your data as .mgh or .mgz formats, then you may use the ``load_mgh()`` (*Matlab*) or ``nib.freesurfer.mghformat.MGHImage()`` (*Python*) 
functions to load your data. You can get the Matlab function from `here <https://surfer.nmr.mgh.harvard.edu/fswiki/FsTutorial/MghFormat>`_. 

.. admonition:: What is this getaffine business? 🧜🏼‍♀️

     In the ``save_mgh()`` and ``nib.freesurfer.mghformat.MGHImage()`` functions, users are required 
     to specify a vox2ras transform matrix. To simplify things, 
     we built a simple function, ``getaffine()``, in which users can specify the surface name ('*conte69*', '*fsa5*') 
     and the hemisphere ('*lh*', '*rh*', '*both*') to obtain the appropriate transform.

.. tabs::

   .. code-tab:: py

        >>> import enigmatoolbox 
        >>> from enigmatoolbox.datasets import getaffine
        >>> import nibabel as nib
        >>> import numpy as np 

        >>> # Specify data to be exported 
        >>> data = CT_schaefer_200_c69
        
        >>> # Define export path
        >>> data_path = os.path.join(os.path.dirname(enigmatoolbox.__file__) + "/datasets/import_export/")

        >>> # Define filenames for left and right hemisphere data
        >>> filename_lh = 'lh.schaefer_200_c69_thickness.mgh'
        >>> filename_rh = 'rh.schaefer_200_c69_thickness.mgh'

        >>> # Export cortical thickness data as .mgh / .mgz 
        >>> nib.freesurfer.mghformat.MGHImage(np.float32(data[:len(data)//2]),
        ...                                   getaffine('conte69', 'lh')).to_filename(data_path + filename_lh)
        >>> nib.freesurfer.mghformat.MGHImage(np.float32(data[len(data)//2:]),
        ...                                   getaffine('conte69', 'lh')).to_filename(data_path + filename_rh)

   .. code-tab:: matlab

        % Specify data to be exported 
        data = CT_schaefer_200_c69

        % Define export path
        data_path = what('import_export'); data_path = data_path.path;
        
        % Define filenames for left and right hemisphere data
        filename_lh = 'lh.schaefer_200_c69_thickness.mgh'
        filename_rh = 'rh.schaefer_200_c69_thickness.mgh'

        % Export cortical thickness data as .mgh / .mgz 
        save_mgh(data(1:end/2), [data_path, filename_lh], getaffine('conte69', 'lh'));
        save_mgh(data(end/2+1:end), [data_path, filename_rh], getaffine('conte69', 'rh'));


|


.. _e_gifti:

GIfTI / .gii
---------------------------------------------------

If you want to export your data as GIfTI/.gii format, then you may use the ``savegifti()`` (*Matlab*) or ``nib.load`` (*Python*) 
functions to load your data. You can get the Matlab function from `here <https://github.com/gllmflndn/gifti>`_.

.. admonition:: Script name change 📛

     To avoid confusion with *Matlab's* function ``save()``, we renamed the GIfTI Toolbox's save function as 
     ``savegifti()``.

.. tabs::

   .. code-tab:: py

        >>> import enigmatoolbox
        >>> import nibabel as nib
        >>> import os  

        >>> # Specify data to be exported 
        >>> data = CT_schaefer_200_c69

        >>> # Convert left and right hemisphere data to GIfTI image
        >>> data_lh = nib.gifti.gifti.GiftiImage()
        >>> data_lh.add_gifti_data_array(nib.gifti.gifti.GiftiDataArray(data=data[:len(data)//2]))
        >>> data_rh = nib.gifti.gifti.GiftiImage()
        >>> data_rh.add_gifti_data_array(nib.gifti.gifti.GiftiDataArray(data=data[len(data)//2:]))

        >>> # Define export path
        >>> data_path = os.path.join(os.path.dirname(enigmatoolbox.__file__) + "/datasets/import_export/")

        >>> # Define filenames for left and right hemisphere data
        >>> filename_lh = 'lh.schaefer_200_c69_thickness.gii'
        >>> filename_rh = 'rh.schaefer_200_c69_thickness.gii'

        >>> # Export cortical thickness data as GIfTI / .gii 
        >>> nib.save(data_lh, data_path + filename_lh)
        >>> nib.save(data_rh, data_path + filename_rh)

   .. code-tab:: matlab

        % Specify data to be exported 
        data = gifti(CT_schaefer_200_c69);
        data_lh = data; data_lh.cdata = data_lh.cdata(1:end/2);
        data_rh = data; data_rh.cdata = data_rh.cdata(end/2+1:end);

        % Define export path
        data_path = what('import_export'); data_path = data_path.path;
        
        % Define filenames for left and right hemisphere data
        filename_lh = 'lh.schaefer_200_c69_thickness.gii'
        filename_rh = 'rh.schaefer_200_c69_thickness.gii'

         % Export cortical thickness data as GIfTI / .gii 
        savegifti(data_lh, [data_path, filename_lh], 'Base64Binary');
        savegifti(data_rh, [data_path, filename_rh], 'Base64Binary');


|


.. _e_cifti:

CIfTI / .dscalar.nii / .dtseries.nii
---------------------------------------------------

If you want to export your data as CIfTI/.dscalar.nii/.dtseries.nii format, then you may use the ``ciftisave()`` (*Matlab*) or ``write_cifti`` (*Python*) 
functions to load your data. You can get the Matlab function from `here <https://github.com/Washington-University/cifti-matlab>`_.

.. tabs::

   .. code-tab:: py

        >>> from enigmatoolbox.datasets import write_cifti

        >>> # Define output path and filenames
        >>> dpath='/Users/saratheriver/Desktop/McGill_PhD/ENIGMA/enigmatoolbox/datasets/import_export/'
        >>> fname_lh='lh.schaefer_200_c69_thickness.dscalar.nii'
        >>> fname_rh='rh.schaefer_200_c69_thickness.dscalar.nii'
        
        >>> # Write left and right files as CIfTI
        >>> write_cifti(data[:len(data)//2], dpath=dpath, fname=fname_lh, labels=None, surface_name='conte69', hemi='lh')
        >>> write_cifti(data[len(data)//2:], dpath=dpath, fname=fname_rh, labels=None, surface_name='conte69', hemi='rh')

   .. code-tab:: matlab

        % Specify data to be exported 
        data = gifti(CT_schaefer_200_c69);
        data_lh = data; data_lh.cdata = data_lh.cdata(1:end/2);
        data_rh = data; data_rh.cdata = data_rh.cdata(end/2+1:end);

        % Define export path
        data_path = what('import_export'); data_path = data_path.path;
        
        % Define filenames for left and right hemisphere data
        filename_lh = 'lh.schaefer_200_c69_thickness.gii'
        filename_rh = 'rh.schaefer_200_c69_thickness.gii'

         % Export cortical thickness data as GIfTI / .gii 
        savegifti(data_lh, [data_path, filename_lh], 'Base64Binary');
        savegifti(data_rh, [data_path, filename_rh], 'Base64Binary');