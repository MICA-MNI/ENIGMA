"""
Permutation functions
"""

import os
import nibabel as nb
import numpy as np
import pandas as pd
import warnings
from scipy.spatial.distance import cdist

from ..datasets import load_fsa5, load_conte69


def centroid_extraction_sphere(sphere_coords, annotfile, ventricles=False):
    """
    Extract centroids of a cortical parcellation on a surface sphere (author: @saratheriver)

    Parameters
    ----------
    sphere_coords : ndarray
        Sphere coordinates, shape = (n, 3)
    annotfile : string
        Name of annotation file {'fsa5_lh_aparc.annot', 'fsa5_rh_aparc.annot, 'fsa5_with_sctx_lh_aparc_aseg.csv', etc.}
    ventricles : bool, optional
        Whether ventricle data are present. Only used when 'annotfile' is fsa5_with_sctx_lh_aparc_aseg or
        fsa5_with_sctx_lh_aparc_aseg``. Default is False.

    Returns
    -------
    coord : ndarray
        Coordinates of the centroid of each region on the sphere, shape = (m, 3).

    See Also
    --------
    :func:`spin_test`

    References
    ----------
    * Alexander-Bloch A, Shou H, Liu S, Satterthwaite TD, Glahn DC,
      Shinohara RT, Vandekar SN and Raznahan A (2018). On testing for spatial
      correspondence between maps of human brain structure and function.
      NeuroImage, 178:540-51.
    * Váša F, Seidlitz J, Romero-Garcia R, Whitaker KJ, Rosenthal G, Vértes PE,
      Shinn M, Alexander-Bloch A, Fonagy P, Dolan RJ, Goodyer IM, the NSPN consortium,
      Sporns O, Bullmore ET (2017). Adolescent tuning of association cortex in human
      structural brain networks. Cerebral Cortex, 28(1):281–294.
    """

    # for cortical annotation files only
    if "aparc_aseg" not in annotfile:
        labels, ctab, names = nb.freesurfer.io.read_annot(annotfile, orig_ids=True)

        centroid = np.empty((0, 3))
        for ic in range(ctab.shape[0]):
            if not names[ic].decode("utf-8") == 'unknown' and not names[ic].decode("utf-8") == 'corpuscallosum':
                label = ctab[ic, -1]
                centroid = np.vstack((centroid, np.array(np.mean(sphere_coords[labels == label, :], axis=0))))

    elif "aparc_aseg" in annotfile and ventricles is not True:
        annot = pd.read_csv(annotfile)

        centroid = np.empty((0, 3))
        for ic in range(annot['structure'][:44].shape[0]):
            if not annot['structure'][:44][ic] == "'unknown'" and not annot['structure'][:44][ic] == "'corpuscallosum'" and not annot['structure'][:44][ic] == "'vent'":
                label = annot['label'][ic]
                centroid = np.vstack((centroid, np.array(np.mean(sphere_coords[annot[annot['label_annot'] ==
                                                                                     label].index.values, :], axis=0))))

    elif "aparc_aseg" in annotfile and ventricles is True:
        annot = pd.read_csv(annotfile)

        centroid = np.empty((0, 3))
        for ic in range(annot['structure'][:44].shape[0]):
            if not annot['structure'][:44][ic] == "'unknown'" and not annot['structure'][:44][ic] == "'corpuscallosum'":
                label = annot['label'][ic]
                centroid = np.vstack((centroid, np.array(np.mean(sphere_coords[annot[annot['label_annot'] ==
                                                                                     label].index.values, :], axis=0))))

    return centroid


def rotate_parcellation(coord_l, coord_r, nrot=100):
    """
    Rotate parcellation (author: @saratheriver)

    Parameters
    ----------
    coord_l : ndarray
        Coordinates of left hemisphere regions on the sphere, shape = (m, 3)
    coord_l : ndarray
        Coordinates of right hemisphere regions on the sphere, shape = (m, 3)
    nrot : int, optional
        Number of rotations. Default is 100.

    Returns
    -------
    perm_id : ndarray
        Array of permutations, shape = (m, nrot)

    See Also
    --------
    :func:`spin_test`

    References
    ----------
    * Alexander-Bloch A, Shou H, Liu S, Satterthwaite TD, Glahn DC,
      Shinohara RT, Vandekar SN and Raznahan A (2018). On testing for spatial
      correspondence between maps of human brain structure and function.
      NeuroImage, 178:540-51.
    * Váša F, Seidlitz J, Romero-Garcia R, Whitaker KJ, Rosenthal G, Vértes PE,
      Shinn M, Alexander-Bloch A, Fonagy P, Dolan RJ, Goodyer IM, the NSPN consortium,
      Sporns O, Bullmore ET (2017). Adolescent tuning of association cortex in human
      structural brain networks. Cerebral Cortex, 28(1):281–294.
    """
    warnings.filterwarnings('ignore')

    # check that coordinate dimensions are correct
    if coord_l.shape[1] is not 3 or coord_r.shape[1] is not 3:
        print('transposing coordinates to be of dimensions nROI x 3')
        coord_l = np.transpose(coord_l)
        coord_r = np.transpose(coord_r)

    nroi_l = coord_l.shape[0]  # n(regions) in the left hemisphere
    nroi_r = coord_r.shape[0]  # n(regions) in the right hemisphere
    nroi = nroi_l + nroi_r     # total n(regions)

    perm_id = np.zeros((nroi, nrot))  # initialise output array
    r = 0                             # count successful (r) iterations unsuccessful (c) iterations
    c = 0                             # count unsuccessful (c) iterations

    I1 = np.array([[-1, 0, 0], [0, 1, 0], [0, 0, 1]])

    # main loop -  use of "while" is to ensure any rotation that maps to itself is excluded (this is rare, but can happen)
    while (r < nrot):
        A = np.random.normal(loc=0, scale=1, size=(3, 3))
        TL, temp = np.linalg.qr(A)
        TL = np.matmul(TL, np.diag(np.sign(np.diag(temp))))
        if np.linalg.det(TL) < 0:
            TL[:, 0] = -TL[:, 0]

        # reflect across the Y-Z plane for right hemisphere
        TR =  np.matmul(np.matmul(I1, TL), I1)
        coord_l_rot = np.matmul(coord_l, TL)
        coord_r_rot = np.matmul(coord_r, TR)

        # after rotation, find "best" match between rotated and unrotated coordinates
        # first, calculate distance between initial coordinates and rotated ones
        # left hemisphere
        dist_l = cdist(coord_l, coord_l_rot)

        # right hemisphere
        dist_r = cdist(coord_r, coord_r_rot)

        # LEFT
        # calculate distances, proceed in order of "most distant minimum"
        # -> for each unrotated region find closest rotated region (minimum), then assign the most distant pair (maximum of the minima),
        # as this region is the hardest to match and would only become harder as other regions are assigned
        temp_dist_l = dist_l
        rot_l = []
        ref_l = []
        for ii in range(nroi_l):
            # max(min) (described above)
            ref_ix = np.argwhere(np.nanmin(temp_dist_l, axis=1) == np.nanmax(np.nanmin(temp_dist_l, axis=1)))[0]
            rot_ix = np.argwhere(temp_dist_l[ref_ix, :][0] == np.nanmin(temp_dist_l[ref_ix, :], axis=1))[0]
            #ref_ix = [i for i, e in enumerate(np.nanmin(temp_dist_l, axis=1)) if e == np.nanmax(np.nanmin(temp_dist_l, axis=1))]  # "furthest" row
            #rot_ix = [i for i, e in enumerate(temp_dist_l[ref_ix, :][0]) if e == np.nanmin(temp_dist_l[ref_ix, :], axis=1)]    # closest region
            ref_l = np.append(ref_l, ref_ix)                                           # store reference and rotated indices
            rot_l = np.append(rot_l, rot_ix)
            temp_dist_l[:, rot_ix] = np.nan                                            # set temporary indices to NaN, to be disregarded in next iteration
            temp_dist_l[ref_ix, :] = np.nan

        # RIGHT
        # calculate distances, proceed in order of "most distant minimum"
        # -> for each unrotated region find closest rotated region (minimum), then assign the most distant pair (maximum of the minima),
        # as this region is the hardest to match and would only become harder as other regions are assigned
        temp_dist_r = dist_r
        rot_r = []
        ref_r = []
        for ii in range(nroi_r):
            # max(min) (described above)
            ref_ix = np.argwhere(np.nanmin(temp_dist_r, axis=1) == np.nanmax(np.nanmin(temp_dist_r, axis=1)))[0]
            rot_ix = np.argwhere(temp_dist_r[ref_ix, :][0] == np.nanmin(temp_dist_r[ref_ix, :], axis=1))[0]
            #ref_ix = [i for i, e in enumerate(np.nanmin(temp_dist_r, axis=1)) if e == np.nanmax(np.nanmin(temp_dist_r, axis=1))]  # "furthest" row
            #rot_ix = [i for i, e in enumerate(temp_dist_r[ref_ix, :][0]) if e == np.nanmin(temp_dist_r[ref_ix, :], axis=1)]    # closest region
            ref_r = np.append(ref_r, ref_ix)                                           # store reference and rotated indices
            rot_r = np.append(rot_r, rot_ix)
            temp_dist_r[:, rot_ix] = np.nan                                            # set temporary indices to NaN, to be disregarded in next iteration
            temp_dist_r[ref_ix, :] = np.nan

        # mapping is x->y
        # collate vectors from both hemispheres + sort mapping according to "reference" vector
        ref_lr = np.append(ref_l, nroi_l + ref_r)
        rot_lr = np.append(rot_l, nroi_l + rot_r)
        ix = np.argsort(ref_lr)
        rot_lr_sort = rot_lr[ix]

        # verify that permutation does not map to itself
        if np.all(rot_lr_sort == range(nroi)) is not True:
            perm_id[:, r] = rot_lr_sort
            r = r + 1
        elif np.all(rot_lr_sort == range(nroi)) is True:
            c = c + 1
            print('map to itself n.' + str(c))

        # track progress
        if np.mod(r, 100) == 0:
            print('permutation ' + str(r) + ' of ' + str(nrot))

    return perm_id


def perm_sphere_p(x, y, perm_id, corr_type='pearson', null_dist=False):
    """
    Generate a p-value for the spatial correlation between two parcellated cortical surface maps (author: @saratheriver)

    Parameters
    ----------
    x : narray, ndarray, or pandas.Series
        One of two map to be correlated
    y : narray, ndarray, or pandas.Series
        The other map to be correlated
    perm_id : ndarray
        Array of permutations, shape = (m, nrot)
    corr_type : string, optional
        Correlation type {'pearson', 'spearman'}. Default is 'pearson'.
    null_dist = bool, optional
        Output null correlations. Default is False.

    Returns
    -------
    p_perm : float
        Permutation p-value
    r_dist : 1D ndarray
        Null correlations, shape = (n_rot*2,). Only if ``null_dist is True``.

    See Also
    --------
    :func:`spin_test`

    References
    ----------
    * Alexander-Bloch A, Shou H, Liu S, Satterthwaite TD, Glahn DC,
      Shinohara RT, Vandekar SN and Raznahan A (2018). On testing for spatial
      correspondence between maps of human brain structure and function.
      NeuroImage, 178:540-51.
    * Váša F, Seidlitz J, Romero-Garcia R, Whitaker KJ, Rosenthal G, Vértes PE,
      Shinn M, Alexander-Bloch A, Fonagy P, Dolan RJ, Goodyer IM, the NSPN consortium,
      Sporns O, Bullmore ET (2017). Adolescent tuning of association cortex in human
      structural brain networks. Cerebral Cortex, 28(1):281–294.
    """

    nroi = perm_id.shape[0]   # number of regions
    nperm = perm_id.shape[1]  # number of permutations

    # empirical correlation
    rho_emp = pd.Series(x).corr(pd.Series(y), method=corr_type)

    # permutation of measures
    x_perm = np.empty((0, nroi))
    y_perm = np.empty((0, nroi))
    for rr in range(nperm):
        x_perm2 = []
        y_perm2 =[]
        for ii in range(nroi):
            x_perm2 = np.append(x_perm2, x[int(perm_id[ii, rr])])
            y_perm2 = np.append(y_perm2, y[int(perm_id[ii, rr])])
        x_perm = np.vstack((x_perm, x_perm2))
        y_perm = np.vstack((y_perm, y_perm2))

    x_perm = np.transpose(x_perm)
    y_perm = np.transpose(y_perm)

    # correlation to unpermuted measures
    rho_null_xy = []
    rho_null_yx = []
    for rr in range(nperm):
        rho_null_xy = np.append(rho_null_xy, pd.Series(x_perm[:, rr]).corr(pd.Series(y), method=corr_type))
        rho_null_yx = np.append(rho_null_yx, pd.Series(x).corr(pd.Series(y_perm[:, rr]), method=corr_type))

    # p-value definition depends on the sign of the empirical correlation
    if rho_emp >= 0:
        p_perm_xy = np.sum((rho_null_xy > rho_emp).astype(int)) / nperm
        p_perm_yx = np.sum((rho_null_yx > rho_emp).astype(int)) / nperm
    elif rho_emp < 0:
        p_perm_xy = np.sum((rho_null_xy < rho_emp).astype(int)) / nperm
        p_perm_yx = np.sum((rho_null_yx < rho_emp).astype(int)) / nperm

    # average p-values
    p_perm = (p_perm_xy + p_perm_yx) / 2

    if null_dist is True:
        return p_perm, np.append(rho_null_xy, rho_null_yx)
    elif null_dist is not True:
        return p_perm


def spin_test(map1, map2, surface_name='fsa5', parcellation_name='aparc', n_rot=100,
              type='pearson', null_dist=False, ventricles=False):
    """
    Spin permutation (author: @saratheriver)

    Parameters
    ----------
    map1 : narray, ndarray, or pandas.Series
        One of two map to be correlated
    map2 : narray, ndarray, or pandas.Series
        The other map to be correlated
    surface_name : string, optional
        Surface name {'fsa5', 'fsa5_with_sctx', 'conte69'}. Default is 'fsa5'.
    parcellation_name : string, optional
        Parcellation name {'aparc', 'aparc_aseg'}. Default is 'aparc'.
    n_rot : int, optional
        Number of spin rotations. Default is 100.
    type : string, optional
        Correlation type {'pearson', 'spearman'}. Default is 'pearson'.
    null_dist : bool, optional
        Output null correlations. Default is False.
    ventricles : bool, optional
        Whether ventricles are present in map1, map2. Only used when ``parcellation_name is 'aparc_aseg'``.
        Default is False.

    Returns
    -------
    p_spin : float
        Permutation p-value
    r_dist : 1D ndarray
        Null correlations, shape = (n_rot*2,). Only if ``null_dist is True``.

    See Also
    --------
    :func:`centroid_extraction_sphere`
    :func:`rotate_parcellation`
    :func:`perm_sphere_p`

    References
    ----------
    * Alexander-Bloch A, Shou H, Liu S, Satterthwaite TD, Glahn DC,
      Shinohara RT, Vandekar SN and Raznahan A (2018). On testing for spatial
      correspondence between maps of human brain structure and function.
      NeuroImage, 178:540-51.
    * Váša F, Seidlitz J, Romero-Garcia R, Whitaker KJ, Rosenthal G, Vértes PE,
      Shinn M, Alexander-Bloch A, Fonagy P, Dolan RJ, Goodyer IM, the NSPN consortium,
      Sporns O, Bullmore ET (2017). Adolescent tuning of association cortex in human
      structural brain networks. Cerebral Cortex, 28(1):281–294.
    """

    if surface_name is "fsa5":
        sphere_lh, sphere_rh = load_fsa5(as_sphere=True)
    elif surface_name is "fsa5_with_sctx":
        sphere_lh, sphere_rh = load_fsa5(as_sphere=True, with_sctx=True)
    elif surface_name is "conte69":
        raise ValueError('Not yet implemented :/')
        sphere_lh, sphere_rh = load_conte69(as_sphere=True)

    root_pth = os.path.dirname(__file__)
    # get sphere coordinates of parcels
    if surface_name is "fsa5_with_sctx" and parcellation_name is "aparc_aseg":
        annotfile_lh = os.path.join(root_pth, 'annot', surface_name + '_lh_' + parcellation_name + '.csv')
        annotfile_rh = os.path.join(root_pth, 'annot', surface_name + '_rh_' + parcellation_name + '.csv')

        lh_centroid = centroid_extraction_sphere(sphere_lh.Points, annotfile_lh, ventricles=ventricles)
        rh_centroid = centroid_extraction_sphere(sphere_rh.Points, annotfile_rh, ventricles=ventricles)
    else:
        annotfile_lh = os.path.join(root_pth, 'annot', surface_name + '_lh_' + parcellation_name + '.annot')
        annotfile_rh = os.path.join(root_pth, 'annot', surface_name + '_rh_' + parcellation_name + '.annot')

        lh_centroid = centroid_extraction_sphere(sphere_lh.Points, annotfile_lh)
        rh_centroid = centroid_extraction_sphere(sphere_rh.Points, annotfile_rh)

    # generate permutation maps
    perm_id = rotate_parcellation(lh_centroid, rh_centroid, n_rot)

    # generate spin permuted p-value
    if isinstance(map1, pd.DataFrame) or isinstance(map1, pd.Series):
        map1 = map1.to_numpy()

    if isinstance(map2, pd.DataFrame) or isinstance(map2, pd.Series):
        map2 = map2.to_numpy()

    p_spin, r_dist = perm_sphere_p(map1, map2, perm_id, type, null_dist=True)

    if null_dist is True:
        return p_spin, r_dist
    elif null_dist is not True:
        return p_spin


def shuf_test(map1, map2, n_rot=100, type='pearson', null_dist=False):
    """
    Shuf permuation (author: @saratheriver)

    Parameters
    ----------
    map1 : narray, ndarray, or pandas.Series
        One of two map to be correlated
    map2 : narray, ndarray, or pandas.Series
        The other map to be correlated
    n_rot : int, optional
        Number of spin rotations. Default is 100.
    type : string, optional
        Correlation type {'pearson', 'spearman'}. Default is 'pearson'.
    null_dist : bool, optional
        Output null correlations. Default is False.

    Returns
    -------
    p_shuf : float
        Permutation p-value
    r_dist : 1D ndarray
        Null correlations, shape = (n_rot*2,). Only if ``null_dist is True``.
    """

    r = 0  # count successful (r) iterations unsuccessful (c) iterations
    c = 0  # count unsuccessful (c) iterations
    nroi = map1.shape[0]  # number of regions

    # generate random permutations
    perm_id = np.zeros((nroi, n_rot))
    while (r < n_rot):
        rot_lr_sort = np.random.permutation(nroi)

        # verify that permutation does not map to itself
        if np.all(rot_lr_sort == range(nroi)) is not True:
            perm_id[:, r] = rot_lr_sort
            r = r + 1
        elif np.all(rot_lr_sort == range(nroi)) is True:
            c = c + 1
            print('map to itself n.' + str(c))

        # track progress
        if np.mod(r, 100) == 0:
            print('permutation ' + str(r) + ' of ' + str(n_rot))

    # empirical correlation
    rho_emp = pd.Series(map1).corr(pd.Series(map2), method=type)

    # permutation of measures
    x_perm = np.empty((0, nroi))
    y_perm = np.empty((0, nroi))
    for rr in range(n_rot):
        x_perm2 = []
        y_perm2 = []
        for ii in range(nroi):
            x_perm2 = np.append(x_perm2, map1[int(perm_id[ii, rr])])
            y_perm2 = np.append(y_perm2, map2[int(perm_id[ii, rr])])
        x_perm = np.vstack((x_perm, x_perm2))
        y_perm = np.vstack((y_perm, y_perm2))

    x_perm = np.transpose(x_perm)
    y_perm = np.transpose(y_perm)

    # correlation to unpermuted measures
    rho_null_xy = []
    rho_null_yx = []
    for rr in range(n_rot):
        rho_null_xy = np.append(rho_null_xy, pd.Series(x_perm[:, rr]).corr(pd.Series(map2), method=type))
        rho_null_yx = np.append(rho_null_yx, pd.Series(map1).corr(pd.Series(y_perm[:, rr]), method=type))

    # p-value definition depends on the sign of the empirical correlation
    if rho_emp >= 0:
        p_perm_xy = np.sum((rho_null_xy > rho_emp).astype(int)) / n_rot
        p_perm_yx = np.sum((rho_null_yx > rho_emp).astype(int)) / n_rot
    else:
        p_perm_xy = np.sum((rho_null_xy < rho_emp).astype(int)) / n_rot
        p_perm_yx = np.sum((rho_null_yx < rho_emp).astype(int)) / n_rot

    # average p-values
    p_shuf = (p_perm_xy + p_perm_yx) / 2

    # null distribution
    r_dist = np.append(rho_null_xy, rho_null_yx)

    if null_dist is True:
        return p_shuf, r_dist
    elif null_dist is not True:
        return p_shuf
