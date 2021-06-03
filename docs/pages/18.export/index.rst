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
        >>> import os

        >>> # Specify data to be exported 
        >>> data = CT_schaefer_200_c69
        
        >>> # Define output path and filenames
        >>> dpath = os.path.join(os.path.dirname(enigmatoolbox.__file__) + "/datasets/import_export/")
        >>> fname_lh = 'lh.schaefer_200_c69_thickness.txt'
        >>> fname_rh = 'rh.schaefer_200_c69_thickness.txt'

        >>> # Export data as .txt / .csv
        >>> np.savetxt(dpath + fname_lh, data[:len(data)//2])
        >>> np.savetxt(dpath + fname_rh, data[len(data)//2:])

   .. code-tab:: matlab

        % Specify data to be exported 
        data = CT_schaefer_200_c69

        % Define output path and filenames
        dpath = what('import_export'); dpath = dpath.path;
        fname_lh = 'lh.schaefer_200_c69_thickness.txt'
        fname_rh = 'rh.schaefer_200_c69_thickness.txt'

        % Export data as .txt / .csv
        writetable(array2table(data(1:end/2)), [dpath, fname_lh], 'WriteVariableNames', 0)
        writetable(array2table(data(end/2+1:end)), [dpath, fname_rh], 'WriteVariableNames', 0)


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
        >>> import os

        >>> # Specify data to be exported 
        >>> data = CT_schaefer_200_c69
        
        >>> # Define output path and filenames
        >>> dpath = os.path.join(os.path.dirname(enigmatoolbox.__file__) + "/datasets/import_export/")
        >>> fname_lh = 'lh.schaefer_200_c69_thickness'
        >>> fname_rh = 'rh.schaefer_200_c69_thickness'
        
        >>> # Export data as FreeSurfer "curv"
        >>> nib.freesurfer.io.write_morph_data(dpath + fname_lh, data[:len(data)//2], nfaces('conte69', 'lh'))
        >>> nib.freesurfer.io.write_morph_data(dpath + fname_rh, data[len(data)//2:], nfaces('conte69', 'rh'))


   .. code-tab:: matlab

        % Specify data to be exported 
        data = CT_schaefer_200_c69

        % Define output path and filenames
        dpath = what('import_export'); dpath = dpath.path;
        fname_lh = 'lh.schaefer_200_c69_thickness'
        fname_rh = 'rh.schaefer_200_c69_thickness'
        
        % Export data as FreeSurfer "curv"
        write_curv([dpath, fname_lh], data(1:end/2), nfaces('conte69', 'lh'));
        write_curv([dpath fname_rh], data(end/2+1:end), nfaces('conte69', 'rh'));


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
        >>> import os

        >>> # Specify data to be exported 
        >>> data = CT_schaefer_200_c69
        
        >>> # Define output path and filenames
        >>> dpath = os.path.join(os.path.dirname(enigmatoolbox.__file__) + "/datasets/import_export/")
        >>> fname_lh = 'lh.schaefer_200_c69_thickness.mgh'
        >>> fname_rh = 'rh.schaefer_200_c69_thickness.mgh'

        >>> # Export data as .mgh / .mgz 
        >>> nib.freesurfer.mghformat.MGHImage(np.float32(data[:len(data)//2]),
        ...                                   getaffine('conte69', 'lh')).to_filename(dpath + fname_lh)
        >>> nib.freesurfer.mghformat.MGHImage(np.float32(data[len(data)//2:]),
        ...                                   getaffine('conte69', 'lh')).to_filename(dpath + fname_rh)

   .. code-tab:: matlab

        % Specify data to be exported 
        data = CT_schaefer_200_c69

        % Define output path and filenames
        dpath = what('import_export'); dpath = dpath.path;
        fname_lh = 'lh.schaefer_200_c69_thickness.mgh'
        fname_rh = 'rh.schaefer_200_c69_thickness.mgh'

        % Export data as .mgh / .mgz 
        save_mgh(data(1:end/2), [dpath, fname_lh], getaffine('conte69', 'lh'));
        save_mgh(data(end/2+1:end), [dpath, fname_rh], getaffine('conte69', 'rh'));


|


.. _e_gifti:

GIfTI / .gii
---------------------------------------------------

If you want to export your data as GIfTI/.gii format, then you may use the ``savegifti()`` (*Matlab*) or ``nib.save`` (*Python*) 
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

        >>> # Define output path and filenames
        >>> dpath = os.path.join(os.path.dirname(enigmatoolbox.__file__) + "/datasets/import_export/")
        >>> fname_lh = 'lh.schaefer_200_c69_thickness.gii'
        >>> fname_rh = 'rh.schaefer_200_c69_thickness.gii'

        >>> # Export data as GIfTI / .gii 
        >>> nib.save(data_lh, dpath + fname_lh)
        >>> nib.save(data_rh, dpath + fname_rh)

   .. code-tab:: matlab

        % Specify data to be exported 
        data = gifti(CT_schaefer_200_c69);
        data_lh = data; data_lh.cdata = data_lh.cdata(1:end/2);
        data_rh = data; data_rh.cdata = data_rh.cdata(end/2+1:end);

        % Define output path and filenames
        dpath = what('import_export'); dpath = dpath.path;
        fname_lh = 'lh.schaefer_200_c69_thickness.gii'
        fname_rh = 'rh.schaefer_200_c69_thickness.gii'

        % Export data as GIfTI / .gii 
        savegifti(data_lh, [dpath, fname_lh], 'Base64Binary');
        savegifti(data_rh, [dpath, fname_rh], 'Base64Binary');


|


.. _e_cifti:

CIfTI / .dscalar.nii / .dtseries.nii
---------------------------------------------------

If you want to export your data as CIfTI/.dscalar.nii/.dtseries.nii format, then you may use the ``write_cifti()`` (*Matlab* and *Python*)  
functions to load your data. The *Matlab* function, however, relies on this toolbox right `here <https://github.com/Washington-University/cifti-matlab>`_.

.. tabs::

   .. code-tab:: py

        >>> from enigmatoolbox.datasets import write_cifti
        >>> import os

        >>> # Specify data to be exported 
        >>> data = CT_schaefer_200_c69;

        >>> # Define output path and filenames
        >>> dpath = os.path.join(os.path.dirname(enigmatoolbox.__file__) + "/datasets/import_export/")
        >>> fname_lh = 'lh.schaefer_200_c69_thickness.dscalar.nii'
        >>> fname_rh = 'rh.schaefer_200_c69_thickness.dscalar.nii'
        
        >>> # Export data as CIfTI / .dscalar.nii / .dtseries.nii
        >>> write_cifti(data[:len(data)//2], dpath=dpath, fname=fname_lh, labels=None, surface_name='conte69', hemi='lh')
        >>> write_cifti(data[len(data)//2:], dpath=dpath, fname=fname_rh, labels=None, surface_name='conte69', hemi='rh')

   .. code-tab:: matlab

        % Specify data to be exported 
        data = CT_schaefer_200_c69;

        % Define output path and filenames
        dpath = what('import_export'); dpath = dpath.path;
        fname_lh = 'lh.schaefer_200_c69_thickness.dscalar.nii'
        fname_rh = 'rh.schaefer_200_c69_thickness.dscalar.nii'

        % Export data as CIfTI / .dscalar.nii / .dtseries.nii
        write_cifti(data(1:end/2), 'dpath', dpath, 'fname', fname_lh, 'surface_name', 'conte69', 'hemi', 'lh')
        write_cifti(data(end/2+1:end), 'dpath', dpath, 'fname', fname_rh, 'surface_name', 'conte69', 'hemi', 'rh')
