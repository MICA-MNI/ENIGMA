import os
import numpy as np
import pandas as pd

from vtk import vtkPolyDataNormals

from ..mesh.mesh_io import read_surface
from ..mesh.mesh_operations import combine_surfaces
from ..utils.parcellation import reduce_by_labels
from ..vtk_interface import wrap_vtk, serial_connect


def load_parcellation(name, scale=400, join=False):
    """ Load parcellation for conte69.

    Parameters
    ----------
    name : {'schaefer', 'vosdewael'}
        Parcellation name, either 'schaefer' for Schaefer (functional)
        parcellations or 'vosdewael' for a subparcellation of aparc.
    scale : {100, 200, 300, 400}, optional
        Number of parcels. Default is 400.
    join : bool, optional
        If False, return one array for each hemisphere. Otherwise,
        return a single array for both left and right hemisphere.
        Default is False.

    Returns
    -------
    parcellation : tuple of ndarrays or ndarray
        Parcellations for left and right hemispheres. If ``join == True``, one
        parcellation with both hemispheres.
    """

    root_pth = os.path.dirname(__file__)
    fname = '{name}_{np}_conte69.csv'.format(name=name, np=scale)
    ipth = os.path.join(root_pth, 'parcellations', fname)
    x = np.loadtxt(ipth, dtype=np.int)
    if join:
        return x
    return x[:x.size//2], x[x.size//2:]


def load_mask(name='midline', join=False):
    """ Load mask for conte69.

    Parameters
    ----------
    name : {'midline', 'temporal'} or None, optional
        Region name. If 'midline', load mask for all cortex.
        Default is 'midline'.
    join : bool, optional
        If False, return one array for each hemisphere. Otherwise,
        return a single array for both left and right hemispheres.
        Default is False.

    Returns
    -------
    mask : tuple of ndarrays or ndarray
        Boolean masks for left and right hemispheres. If ``join == True``, one
        mask with both hemispheres.
    """

    root_pth = os.path.dirname(__file__)
    ipth = os.path.join(root_pth, 'surfaces', 'conte69_32k_{0}{1}_mask.csv')
    if name == 'midline':
        name = ''
    else:
        name = '_' + name
    mask_lh = np.loadtxt(ipth.format('lh', name), dtype=np.bool)
    mask_rh = np.loadtxt(ipth.format('rh', name), dtype=np.bool)
    if join:
        return np.concatenate([mask_lh, mask_rh])
    return mask_lh, mask_rh


def load_conte69(as_sphere=False, with_normals=True, join=False):
    """ Load conte69 surfaces.

    Parameters
    ----------
    as_sphere : bool, optional
        Return spheres instead of cortical surfaces. Default is False.
    with_normals : bool, optional
        Whether to compute surface normals. Default is True.
    join : bool, optional
        If False, return one surface for left and right hemispheres. Otherwise,
        return a single surface as a combination of both left and right
        surfaces. Default is False.

    Returns
    -------
    surf : tuple of BSPolyData or BSPolyData
        Surfaces for left and right hemispheres. If ``join == True``, one
        surface with both hemispheres.
    """

    root_pth = os.path.dirname(__file__)
    if as_sphere:
        fname = 'conte69_32k_{}_sphere.gii'
    else:
        fname = 'conte69_32k_{}.gii'

    ipth = os.path.join(root_pth, 'surfaces', fname)
    surfs = [None] * 2
    for i, side in enumerate(['lh', 'rh']):
        surfs[i] = read_surface(ipth.format(side))
        if with_normals:
            nf = wrap_vtk(vtkPolyDataNormals, splitting=False,
                          featureAngle=0.1)
            surfs[i] = serial_connect(surfs[i], nf)

    if join:
        return combine_surfaces(*surfs)
    return surfs[0], surfs[1]


def load_fsa5(with_normals=True, join=False):
    """ Load fsaverage5 surfaces.

    Parameters
    ----------
    with_normals : bool, optional
        Whether to compute surface normals. Default is True.
    join : bool, optional
        If False, return one surface for left and right hemispheres. Otherwise,
        return a single surface as a combination of both left and right
        surfaces. Default is False.

    Returns
    -------
    surf : tuple of BSPolyData or BSPolyData
        Surfaces for left and right hemispheres. If ``join == True``, one
        surface with both hemispheres.
    """

    root_pth = os.path.dirname(__file__)
    fname = 'fsa5_{}.gii'

    ipth = os.path.join(root_pth, 'surfaces', fname)
    surfs = [None] * 2
    for i, side in enumerate(['lh', 'rh']):
        surfs[i] = read_surface(ipth.format(side))
        if with_normals:
            nf = wrap_vtk(vtkPolyDataNormals, splitting=False,
                          featureAngle=0.1)
            surfs[i] = serial_connect(surfs[i], nf)

    if join:
        return combine_surfaces(*surfs)
    return surfs[0], surfs[1]


def load_subcortical(with_normals=False, join=False):
    """ Load subcortical surfaces.

    Parameters
    ----------
    with_normals : bool, optional
        Whether to compute surface normals. Default is False.
    join : bool, optional
        If False, return one surface for left and right hemispheres. Otherwise,
        return a single surface as a combination of both left and right
        surfaces. Default is False.

    Returns
    -------
    surf : tuple of BSPolyData or BSPolyData
        Surfaces for left and right hemispheres. If ``join == True``, one
        surface with both hemispheres.
    """

    root_pth = os.path.dirname(__file__)
    fname = 'sctx_{}.gii'

    ipth = os.path.join(root_pth, 'surfaces', fname)
    surfs = [None] * 2
    for i, side in enumerate(['lh', 'rh']):
        surfs[i] = read_surface(ipth.format(side))
        if with_normals:
            nf = wrap_vtk(vtkPolyDataNormals, splitting=False,
                          featureAngle=0.1)
            surfs[i] = serial_connect(surfs[i], nf)

    if join:
        return combine_surfaces(*surfs)
    return surfs[0], surfs[1]


def _load_feat(feat_name, parcellation=None, mask=None):
    root_pth = os.path.dirname(__file__)
    ipth = os.path.join(root_pth, 'matrices', 'main_group',
                        '{0}.csv'.format(feat_name))
    x = np.loadtxt(ipth, dtype=np.float)
    if mask is not None:
        x = x[mask]

    if parcellation is not None:
        if mask is not None:
            parcellation = parcellation[mask]
        x = reduce_by_labels(x, parcellation, red_op='mean')
    return x


def load_marker(name, join=False):
    """ Load cortical data for conte69.

    Parameters
    ----------
    name : {'curvature', 'thickness', 't1wt2w'}
        Marker name.
    join : bool, optional
        If False, return one array for each hemisphere. Otherwise,
        return a single array for both left and right hemispheres.
        Default is False.

    Returns
    -------
    marker : tuple of ndarrays or ndarray
        Marker data for left and right hemispheres. If ``join == True``, one
        array with both hemispheres.
    """

    feat_name = 'conte69_32k_{0}'.format(name)
    x = _load_feat(feat_name)
    if join:
        return x
    return x[:x.size//2], x[x.size//2:]


def load_sc():
    """ Load structural connectivity data from 207 HCP subjects
        Parcellated using Desikan Killiany (68 cortical regions and 16 subcortical structures)

        Returns
        -------
        strucMatrix_ctx : 68 x 68 ndarray representing cortico-cortical connectivity
        strucLabels_ctx : 68 x 1 ndarray representing cortical labels
        strucMatrix_sctx : 14 x 68 ndarray representing subcortico-cortical connectivity
        strucLabels_sctx : 14 x 1 ndarray representing subcortical labels *

        * ventricles are excluded
    """
    root_pth = os.path.dirname(__file__)

    ctx = 'strucMatrix_ctx.csv'
    ctx_ipth = os.path.join(root_pth, 'matrices', 'hcp_connectivity', ctx)

    ctxL = 'strucLabels_ctx.csv'
    ctxL_ipth = os.path.join(root_pth, 'matrices', 'hcp_connectivity', ctxL)

    sctx = 'strucMatrix_sctx.csv'
    sctx_ipth = os.path.join(root_pth, 'matrices', 'hcp_connectivity', sctx)

    sctxL = 'strucLabels_sctx.csv'
    sctxL_ipth = os.path.join(root_pth, 'matrices', 'hcp_connectivity', sctxL)

    return np.loadtxt(ctx_ipth, dtype=np.float, delimiter=','), \
           np.loadtxt(ctxL_ipth, dtype='str', delimiter=','), \
           np.loadtxt(sctx_ipth, dtype=np.float, delimiter=','), \
           np.loadtxt(sctxL_ipth, dtype='str', delimiter=',')


def load_fc():
    """ Load functional connectivity data from 207 HCP subjects
        Parcellated using Desikan Killiany (68 cortical regions and 16 subcortical structures)

        Returns
        -------
        strucMatrix_ctx : 68 x 68 ndarray representing cortico-cortical connectivity
        strucLabels_ctx : 68 x 1 ndarray representing cortical labels
        strucMatrix_sctx : 14 x 68 ndarray representing subcortico-cortical connectivity
        strucLabels_sctx : 14 x 1 ndarray representing subcortical labels *

        * ventricles are excluded
    """
    root_pth = os.path.dirname(__file__)

    ctx = 'funcMatrix_ctx.csv'
    ctx_ipth = os.path.join(root_pth, 'matrices', 'hcp_connectivity', ctx)

    ctxL = 'funcLabels_ctx.csv'
    ctxL_ipth = os.path.join(root_pth, 'matrices', 'hcp_connectivity', ctxL)

    sctx = 'funcMatrix_sctx.csv'
    sctx_ipth = os.path.join(root_pth, 'matrices', 'hcp_connectivity', sctx)

    sctxL = 'funcLabels_sctx.csv'
    sctxL_ipth = os.path.join(root_pth, 'matrices', 'hcp_connectivity', sctxL)

    return np.loadtxt(ctx_ipth, dtype=np.float, delimiter=','), \
           np.loadtxt(ctxL_ipth, dtype='str', delimiter=','), \
           np.loadtxt(sctx_ipth, dtype=np.float, delimiter=','), \
           np.loadtxt(sctxL_ipth, dtype='str', delimiter=',')


def enigma_covariance(zdata):
    """ Construction of intra-individual brain structural covariance networks

        Parameters
        ----------
        zdata : z-scored matrix (#subjects x #features) of morphological features
                (e.g., cortical thickness + subcortical volume)

        Returns
        -------
        joint_var_matrix : ndarray #features x #features x #subjects
    """
    joint_var_matrix = np.zeros((zdata.shape[1], zdata.shape[1], zdata.shape[0]))
    for kk in range(zdata.shape[0]):
        for ii in range(zdata.shape[1]):
            for jj in range(zdata.shape[1]):
                joint_var_matrix[ii, jj, kk] = 1 / np.exp(np.square(zdata[kk, ii] - zdata[kk, jj]))
    return joint_var_matrix


def fetch_ahba(csvfile=None):
    """ Fetch Allen Human Brain Atlas microarray expression data from all donors and all genes
            Parcellated using Desikan Killiany
                68 cortical regions and 14 subcortical structures (ventricles are excluded)

            Returns
            -------
            g : gene expression matrix, 82 x 15633 panda dataframe
        """
    if csvfile is None:
        url = 'https://raw.githubusercontent.com/saratheriver/enigma-extra/master/ahba/allgenes.csv'
        return pd.read_csv(url, error_bad_lines=False)
    else:
        return pd.read_csv(csvfile, error_bad_lines=False)

def epilepsy_genes():
    """ Outputs names of epilepsy-related risk genes based on previous GWAS
        (ILAE on Complex Epilepsies, 2018, Nat Comms)

        Returns
        -------
        epigx : names of genes for epilepsy subtypes (dict)
    """
    allepilepsy = ['FANCL', 'BCL11A', 'SCN3A', 'SCN2A', 'TTC21B', 'SCN1A', 'HEATR3', 'BRD7']
    focalepilepsy = ['SCN3A', 'SCN2A', 'TTC21B', 'SCN1A']
    generalizedepilepsy = ['FANCL', 'BCL11A', 'SCN3A', 'SCN2A', 'TTC21B', 'SCN1A', 'STAT4', 'PCDH7', 'GABRA2', 'KCNN2',
                           'ATXN1', 'PNPO', 'GRIK1']
    jme = ['STX1B']
    cae = ['FANCL', 'BCL11A', 'ZEB2']
    focalhs = ['C3orf33', 'SLC33A1', 'KCNAB1', 'GJA1']

    return {'allepilepsy': allepilepsy, 'focalepilepsy': focalepilepsy,
             'generalizedepilepsy': generalizedepilepsy, 'jme': jme,
             'cae': cae, 'focalhs': focalhs}