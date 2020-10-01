"""
Permutation functions
"""

import os
import nibabel as nb
import numpy as np
import pandas as pd
import warnings

from ..datasets import load_fsa5, load_conte69

def centroid_extraction_sphere(sphere_coords, annotfile):
    """
    Function to extract centroids of a cortical parcellation on the
    Freesurfer sphere, for subsequent input to code for the performance of a
    spherical permutation. Runs on individual hemispheres.

    Inputs:
    sphere_coords   sphere coordinates (n x 3)
    annot_file      'fsa5_lh_aparc.annot' (string)

    Output:
    centroid      coordinates of the centroid of each region on the sphere

    Rafael Romero-Garcia, 2017
    Ported to Python by Sara Larivière, rainy September 2020 evening
    """

    labels, ctab, names = nb.freesurfer.io.read_annot(annotfile, orig_ids=True)

    ind = 0
    centroid = np.empty((0, 3))
    for ic in range(ctab.shape[0]):
        if not names[ic].decode("utf-8") == 'unknown' and not names[ic].decode("utf-8") == 'corpuscallosum':
            ind = ind + 1
            label = ctab[ic, -1]
            centroid = np.vstack((centroid, np.array(np.mean(sphere_coords[labels == label, :], axis=0))))

    return centroid


def rotate_parcellation(coord_l, coord_r, nrot=100):
    """
    Function to generate a permutation map from a set of cortical regions of interest to itself,
    while (approximately) preserving contiguity and hemispheric symmetry.
    The function is based on a rotation of the FreeSurfer projection of coordinates
    of a set of regions of interest on the sphere.

    Inputs:
    coord_l       coordinates of left hemisphere regions on the sphere        array of size [n(LH regions) x 3]
    coord_r       coordinates of right hemisphere regions on the sphere       array of size [n(RH regions) x 3]
    nrot          number of rotations (default = 10'000)                      scalar

    Output:
    perm_id      array of permutations, from set of regions to itself        array of size [n(total regions) x nrot]

    FrantiÅ¡ek VÃ¡Å¡a, fv247@cam.ac.uk, June 2017 - June 2018
          Updated on 5/9/2019 with permutation scheme that uniformly samples the space of permutations on the sphere
          See github repo (@frantisekvasa) and references within for details

    Ported to Python by Sara Larivière, rainy September 2020 evening
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
        dist_l = np.empty((0, nroi_l))
        for ii in range(nroi_l):
            dist_l2 = []
            for jj in range(nroi_l):
                dist_l2 = np.append(dist_l2, np.sqrt(np.sum((coord_l[ii, :]-coord_l_rot[jj, :])**2)))
            dist_l = np.vstack((dist_l, dist_l2))

        # right hemisphere
        dist_r = np.empty((0, nroi_r))
        for ii in range(nroi_r):
            dist_r2 = []
            for jj in range(nroi_r):
                dist_r2 = np.append(dist_r2, np.sqrt(np.sum((coord_r[ii, :] - coord_r_rot[jj, :]) ** 2)))
            dist_r = np.vstack((dist_r, dist_r2))

        # LEFT
        # calculate distances, proceed in order of "most distant minimum"
        # -> for each unrotated region find closest rotated region (minimum), then assign the most distant pair (maximum of the minima),
        # as this region is the hardest to match and would only become harder as other regions are assigned
        temp_dist_l = dist_l
        rot_l = []
        ref_l = []
        for ii in range(nroi_l):
            # max(min) (described above)
            ref_ix = [i for i, e in enumerate(np.nanmin(temp_dist_l, axis=1)) if e == np.nanmax(np.nanmin(temp_dist_l, axis=1))]  # "furthest" row
            rot_ix = [i for i, e in enumerate(temp_dist_l[ref_ix, :][0]) if e == np.nanmin(temp_dist_l[ref_ix, :], axis=1)]    # closest region
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
            ref_ix = [i for i, e in enumerate(np.nanmin(temp_dist_r, axis=1)) if e == np.nanmax(np.nanmin(temp_dist_r, axis=1))]  # "furthest" row
            rot_ix = [i for i, e in enumerate(temp_dist_r[ref_ix, :][0]) if e == np.nanmin(temp_dist_r[ref_ix, :], axis=1)]    # closest region
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


def perm_sphere_p(x, y, perm_id, corr_type='pearson', spin_dist=False):
    """
    Function to generate a p-value for the spatial correlation between two parcellated cortical surface maps,
    using a set of spherical permutations of regions of interest (which can be generated using the function "rotate_parcellation").
    The function performs the permutation in both directions; i.e.: by permute both measures,
    before correlating each permuted measure to the unpermuted version of the other measure

    Inputs:
    x                 one of two maps to be correlated                                                                    vector
    y                 second of two maps to be correlated                                                                 vector
    perm_id           array of permutations, from set of regions to itself (as generated by "rotate_parcellation")        array of size [n(total regions) x nrot]
    corr_type         type of correlation                                                                                 "spearman" or "pearson" (default)

    Output:
    p_perm            permutation p-value

    FrantiÅ¡ek VÃ¡Å¡a, fv247@cam.ac.uk, June 2017 - June 2018

    Ported to Python by Sara Larivière, rainy September 2020 evening
    """

    nroi = perm_id.shape[0]   # number of regions
    nperm = perm_id.shape[1]  # number of permutatons

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
    if rho_emp > 0:
        p_perm_xy = np.sum((rho_null_xy > rho_emp).astype(int)) / nperm
        p_perm_yx = np.sum((rho_null_yx > rho_emp).astype(int)) / nperm
    elif rho_emp < 0:
        p_perm_xy = np.sum((rho_null_xy < rho_emp).astype(int)) / nperm
        p_perm_yx = np.sum((rho_null_yx < rho_emp).astype(int)) / nperm

    # average p-values
    p_perm = (p_perm_xy + p_perm_yx) / 2

    if spin_dist is True:
        return p_perm, np.append(rho_null_xy, rho_null_yx)
    elif spin_dist is not True:
        return p_perm


def spin_test(map1, map2, surface_name='fsa5', parcellation_name='aparc', n_rot=100, type='pearson', spin_dist=False):
    """
    INPUTS
       map1               = one of two cortical map to be correlated
       map2               = the other cortical map to be correlated
       surface_name       = 'fsa5' (default) or 'conte69'
       parcellation_name  = 'aparc' (default)
       n_rot              = number of spin rotations (default 100)
       type               = correlation type, 'pearson' (default), 'spearman'
       spin_dist          = save distribution of spinned correlations (null model)

    OUTPUT
       p_spin          = permutation p-value
       r_dist          = distribution of spinned correlations (number of spins * 2)


    Functions above from here
           https://github.com/frantisekvasa/rotate_parcellation

     Last modifications:
     SL | a rainy September day 2020
    """

    if surface_name is "fsa5":
        sphere_lh, sphere_rh = load_fsa5(as_sphere=True)
    elif surface_name is "conte69":
        raise ValueError('Not yet implemented :/')
        sphere_lh, sphere_rh = load_conte69(as_sphere=True)

    root_pth = os.path.dirname(__file__)
    annotfile_lh = os.path.join(root_pth, 'annot', surface_name+'_lh_'+parcellation_name+'.annot')
    annotfile_rh = os.path.join(root_pth, 'annot', surface_name+'_rh_'+parcellation_name+'.annot')

    # get sphere coordinates of parcels
    lh_centroid = centroid_extraction_sphere(sphere_lh.Points, annotfile_lh)
    rh_centroid = centroid_extraction_sphere(sphere_rh.Points, annotfile_rh)

    # generate permutation maps
    perm_id = rotate_parcellation(lh_centroid, rh_centroid, n_rot)

    # generate spin permuted p-value
    p_spin, r_dist = perm_sphere_p(map1, map2, perm_id, type, spin_dist=True)

    if spin_dist is True:
        return p_spin, r_dist
    elif spin_dist is not True:
        return p_spin


def shuf_test(map1, map2, n_rot=100, type='pearson', spin_dist=False):
    """
    INPUTS
       map1            = one of two subcortical map to be correlated
       map2            = the other subcortical map to be correlated
       n_rot           = number of shuffles (default 100)
       type            = correlation type, 'pearson' (default), 'spearman'
       spin_dist       = save distribution of spinned correlations (null model)

    OUTPUT
       p_shuf          = permutation p-value
       r_dist          = distribution of shuffled correlations (number of shuffles * 2)

     Sara Lariviere | a sunny September day 2020
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
    if rho_emp > 0:
        p_perm_xy = np.sum((rho_null_xy > rho_emp).astype(int)) / n_rot
        p_perm_yx = np.sum((rho_null_yx > rho_emp).astype(int)) / n_rot
    elif rho_emp < 0:
        p_perm_xy = np.sum((rho_null_xy < rho_emp).astype(int)) / n_rot
        p_perm_yx = np.sum((rho_null_yx < rho_emp).astype(int)) / n_rot

    # average p-values
    p_shuf = (p_perm_xy + p_perm_yx) / 2

    # null distribution
    r_dist = np.append(rho_null_xy, rho_null_yx)

    if spin_dist is True:
        return p_shuf, r_dist
    elif spin_dist is not True:
        return p_shuf
