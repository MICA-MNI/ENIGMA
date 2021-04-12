.. _import_data:

.. title:: Import data

Import vertexwise or parcellated data 
============================================

This page contains descriptions and examples to import your own data, stored as different file format types.
Compatible import file formats are: :ref:`.txt/.csv <i_txt_csv>`, :ref:`FreeSurfer/"curv" <i_fs_curv>`, :ref:`.mgh/.mgz <i_mgh_mgz>`,
:ref:`GIfTI/.gii <i_gifti>`, :ref:`CIfTI/.dscalar.nii/.dtseries.nii <i_cifti>`

As an example, we will import vertexwise cortical thickness data sampled on the Conte69 surface template (available within the **ENIGMA Toolbox**). 
The examples below can be easily modified to import any vertexwise or parcellated data by simply changing the path to the data and the filenames. 
Here, we imported data from ENIGMA's import_export directory.

.. _i_txt_csv:

.txt / .csv
---------------------------------------------------

If your data are stored as text (.txt) or comma-separated values (.csv) files, then you may use the ``dlmread()`` (*Matlab*) or ``np.loadtxt()`` (*Python*) 
functions to load your data.

.. admonition:: Table please 🍴

     Should you prefer to upload your data as a table (*e.g.*, when importing ENIGMA-type summary statistics stored in your local computer),
     then you may use the ``readtable()`` (*Matlab*) or ``pd.readcsv()`` (*Python*) functions.

.. tabs::

   .. code-tab:: py

        >>> import enigmatoolbox 
        >>> import numpy as np 
        >>> import os

        >>> # Define path to your data
        >>> dpath = os.path.join(os.path.dirname(enigmatoolbox.__file__) + "/datasets/import_export/")

        >>> # Import data stored as .txt / .csv
        >>> CT = []
        >>> for _, h in enumerate(['lh', 'rh']):
        >>>     CT = np.append(CT, np.loadtxt(dpath + '{}.conte69_32k_thickness.txt'.format(h)))

   .. code-tab:: matlab

        % Define path to your data
        dpath = what('import_export'); dpath = data_path.path;

        % Import data stored as .txt / .csv
        data_lh = dlmread([dpath '/lh.conte69_32k_thickness.txt']);
        data_rh = dlmread([dpath '/rh.conte69_32k_thickness.txt']);
        CT = [data_lh data_rh];


|


.. _i_fs_curv:

FreeSurfer / "curv"
---------------------------------------------------

If your data are stored as FreeSurfer "curv" format (*e.g.*, ?h.thickness), then you may use the ``read_curv()`` (*Matlab*) or ``nib.freesurfer.io.read_morph_data()`` (*Python*) 
functions to load your data. You can get the Matlab function from `here <https://github.com/neurodebian/freesurfer>`_.

.. tabs::

   .. code-tab:: py

        >>> import enigmatoolbox 
        >>> import nibabel as nib
        >>> import numpy as np 
        >>> import os

        >>> # Define path to your data
        >>> dpath = os.path.join(os.path.dirname(enigmatoolbox.__file__) + "/datasets/import_export/")

        >>> # Import data stored as FreeSurfer "curv"
        >>> CT = []
        >>> for _, h in enumerate(['lh', 'rh']):
        >>>     CT = np.append(CT, nib.freesurfer.io.read_morph_data(dpath + '{}.conte69_32k_thickness'.format(h)))

   .. code-tab:: matlab

        % Define path to your data
        dpath = what('import_export'); dpath = dpath.path;

        % Import data stored as FreeSurfer "curv"
        data_lh = read_curv([dpath '/lh.conte69_32k_thickness']);
        data_rh = read_curv([dpath '/rh.conte69_32k_thickness']);
        CT = [data_lh; data_rh].';


|


.. _i_mgh_mgz:

.mgh / .mgz
---------------------------------------------------

If your data are stored as .mgh or .mgz formats, then you may use the ``load_mgh()`` (*Matlab*) or ``nib.load`` (*Python*) 
functions to load your data. You can get the Matlab function from `here <https://surfer.nmr.mgh.harvard.edu/fswiki/FsTutorial/MghFormat>`_.

.. tabs::

   .. code-tab:: py

        >>> import enigmatoolbox 
        >>> import nibabel as nib
        >>> import numpy as np 
        >>> import os

        >>> # Define path to your data
        >>> dpath = os.path.join(os.path.dirname(enigmatoolbox.__file__) + "/datasets/import_export/")

        >>> # Import data stored as .mgh / .mgz
        >>> CT = []
        >>> for _, h in enumerate(['lh', 'rh']):
        >>>     CT = np.append(CT, nib.load(dpath + '{}.conte69_32k_thickness.mgh'.format(h)).get_fdata().squeeze())

   .. code-tab:: matlab

        % Define path to your data
        dpath = what('import_export'); dpath = dpath.path;

        % Import data stored as .mgh / .mgz
        data_lh = load_mgh([dpath '/lh.conte69_32k_thickness.mgh']);
        data_rh = load_mgh([dpath '/rh.conte69_32k_thickness.mgh']);
        CT = [data_lh; data_rh].';


|


.. _i_gifti:

GIfTI / .gii
---------------------------------------------------

If your data are stored as GIfTI/.gii format, then you may use the ``gifti()`` (*Matlab*) or ``nib.load`` (*Python*) 
functions to load your data. You can get the Matlab function from `here <https://github.com/gllmflndn/gifti>`_.

.. tabs::

   .. code-tab:: py

        >>> import enigmatoolbox 
        >>> import nibabel as nib
        >>> import numpy as np 
        >>> import os

        >>> # Define path to your data
        >>> dpath = os.path.join(os.path.dirname(enigmatoolbox.__file__) + "/datasets/import_export/")

        >>> # Import data stored as GIfTI / .gii
        >>> CT = []
        >>> for _, h in enumerate(['lh', 'rh']):
        >>>     CT = np.append(CT, nib.load(dpath + '{}.conte69_32k_thickness.gii'.format(h)).darrays[0].data)

   .. code-tab:: matlab

        % Define path to your data
        dpath = what('import_export'); dpath = dpath.path;

        % Import data stored as GIfTI / .gii
        data_lh = gifti([dpath '/lh.conte69_32k_thickness.gii']);
        data_rh = gifti([dpath '/rh.conte69_32k_thickness.gii']);
        CT = [data_lh.cdata; data_rh.cdata].';


|


.. _i_cifti:

CIfTI / .dscalar.nii / .dtseries.nii
---------------------------------------------------

If your data are stored as CIfTI/.dscalar.nii/dtseries.nii format, then you may use the ``cifti_read()`` (*Matlab*) or ``nib.load`` (*Python*) 
functions to load your data. You can get the Matlab function from `here <https://github.com/Washington-University/cifti-matlab>`_.
        
     .. tabs::
     
          .. code-tab:: py
     
               >>> import enigmatoolbox 
               >>> import nibabel as nib
               >>> import numpy as np 
               >>> import os
     
               >>> # Define path to your data
               >>> dpath = os.path.join(os.path.dirname(enigmatoolbox.__file__) + "/datasets/import_export/")
     
               >>> # Import data stored as CIfTI / .dscalar.nii / .dtseries.nii
               >>> CT = []
               >>> for _, h in enumerate(['lh', 'rh']):
               >>>     CT = np.append(CT, np.asarray(nib.load(dpath + '{}.conte69_32k_thickness.dscalar.nii'.format(h)).get_data()))
     
          .. code-tab:: matlab
     
               % Define path to your data
               dpath = what('import_export'); dpath = dpath.path;
     
               % Import data stored as CIfTI / .dscalar.nii / .dtseries.nii
               data_lh = cifti_read([dpath '/lh.conte69_32k_thickness.dscalar.nii']);
               data_rh = cifti_read([dpath '/rh.conte69_32k_thickness.dscalar.nii']);
               CT = [data_lh.cdata; data_rh.cdata].';
     
     
