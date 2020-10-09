import os
import numpy as np
import pandas as pd

from vtk import vtkPolyDataNormals

from ..mesh.mesh_io import read_surface
from ..mesh.mesh_operations import combine_surfaces
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


def load_mask(name='midline', surface_name="fsa5", join=False):
    """ Load mask for conte69, fsa5 (default), and fsa5_with_sctx.

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
    if surface_name is "conte69":
        ipth = os.path.join(root_pth, 'surfaces', 'conte69_32k_{0}{1}_mask.csv')
        if name == 'midline':
            name = ''
        else:
            name = '_' + name
        mask_lh = np.loadtxt(ipth.format('lh', name), dtype=np.bool)
        mask_rh = np.loadtxt(ipth.format('rh', name), dtype=np.bool)
        if join:
            return np.concatenate([mask_lh, mask_rh])

    else:
        ipth = os.path.join(root_pth, 'surfaces', surface_name + '_{0}{1}_mask.csv')
        if name == 'midline':
            name = ''
        else:
            print('sorry there\'s no other option for now')
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


def load_fsa5(as_sphere=False, with_normals=True, join=False, with_sctx=False):
    """ Load fsaverage5 surfaces.

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
    with_sctx : bool, optional
        If False, returns cortical spheres, if True, returns combined
        cortical+subcortical surface (spheres only at this moment)

    Returns
    -------
    surf : tuple of BSPolyData or BSPolyData
        Surfaces for left and right hemispheres. If ``join == True``, one
        surface with both hemispheres.
    """

    root_pth = os.path.dirname(__file__)
    if as_sphere is True and with_sctx is not True:
        fname = 'fsa5_sphere_{}.gii'
    elif as_sphere is True and with_sctx is True:
        fname = 'fsa5_with_sctx_sphere_{}.gii'
    elif as_sphere is not True and with_sctx is not True:
        fname = 'fsa5_{}.gii'
    elif as_sphere is not True and with_sctx is True:
        fname = 'fsa5_with_sctx_{}.gii'

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
    """ Load structural connectivity data parcellated using Desikan Killiany (author: @saratheriver)

        Returns
        -------
        strucMatrix_ctx : 2D ndarray
            Cortico-cortical connectivity, shape = (68, 68)
        strucLabels_ctx : 1D ndarray
            Cortical labels, shape (68,)
        strucMatrix_sctx : 2D ndarray
            Subcortico-cortical connectivity, shape = (14, 68)
        strucLabels_sctx : 1D ndarray
            Subcortical labels, shape = (14,)
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
    """ Load functional connectivity data parcellated using Desikan Killiany (author: @saratheriver)

        Returns
        -------
        funcMatrix_ctx : 2D ndarray
            Cortico-cortical connectivity, shape = (68, 68)
        funcLabels_ctx : 1D ndarray
            Cortical labels, shape (68,)
        funcMatrix_sctx : 2D ndarray
            Subcortico-cortical connectivity, shape = (14, 68)
        funcLabels_sctx : 1D ndarray
            Subcortical labels, shape = (14,)
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


def structural_covariance(zdata):
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
    """ Fetch Allen Human Brain Atlas microarray expression data from all donors and all genes (author: @saratheriver)

            Parameters
            ----------
            csvfile : None or string
                Path to downloaded csvfile
                If None (default), fetches microarray expression data from the internet

            Returns
            -------
            genes : pandas.DataFrame
                Table of gene co-expression data, shape = (82, 15633)
        """
    if csvfile is None:
        url = 'https://raw.githubusercontent.com/saratheriver/enigma-extra/master/ahba/allgenes.csv'
        return pd.read_csv(url, error_bad_lines=False)
    else:
        return pd.read_csv(csvfile, error_bad_lines=False)


def risk_genes(disorder=None):
    """ Outputs names of GWAS-derived risk genes for a given disorder

        Parameters
        ----------
        disorder : {'adhd', 'asd', 'bipolar', 'depression', 'epilepsy', 'hippocampal_volume', 'ocd', 'schizophrenia',
        'tourette'}
            Name of disorder, default is None

        Returns
        -------
        risk_genes : set
            Names of genes for a given disorder
    """
    if disorder is "adhd":
        return {'ST3GAL3', 'KDM4A', 'KDM4A-AS1', 'PTPRF', 'SLC6A9', 'ARTN', 'DPH2',
                 'ATP6V0B', 'B4GALT2', 'CCDC24', 'IPO13', 'SPAG16', 'PCDH7', 'LINC02497',
                 'LINC00461', 'MIR9-2', 'LINC02060', 'TMEM161B-AS1', 'FOXP2', 'MIR3666',
                 'LINC01288', 'SORCS3', 'DUSP6', 'POC1B', 'SEMA6D', 'LINC01572'};

    elif disorder is "asd":
        return {'NEGR1', 'PTBP2', 'CADPS', 'FEZF2', 'TMEM33', 'DCAF4L1',
                'SLC30A9', 'BEND4', 'NUDT12', 'KCNN2', 'MMS22L', 'POU3F2',
                'KMT2E', 'SRPK2', 'C8orf74', 'SOX7', 'PINX1', 'MROH5',
                'MARK3', 'CKB', 'TRMT61A', 'BAG5', 'APOPT1', 'KLC1',
                'XRCC3', 'MACROD2', 'XRN2', 'KIZ', 'NKX2-4', 'NKX2-2'}

    elif disorder is "bipolar":
        return {'PLEKHO1', 'LMAN2L', 'SCN2A', 'PCGEM1', 'TRANK1', 'ITIH1',
                'CD47', 'FSTL5', 'ADCY2', 'SSBP2', 'RIMS1', 'POU3F2',
                'RPS6KA2', 'THSD7A', 'SRPK2', 'MRPS33', 'ANK3', 'ADD3',
                'FADS2', 'PACS1', 'PC', 'SHANK2', 'CACNA1C', 'STARD9',
                'ZNF592', 'GRIN2A', 'HDAC5', 'ZCCHC2', 'NCAN', 'STK4'}

    elif disorder is "depression":
        return {'SORCS3', 'RBFOX1', 'GRM5', 'HIST1H2BN', 'SHISA9', 'TCF4', 'NEGR1', 'HIST1H3J', 'DENND1A',
                'DCC', 'RSRC1', 'TENM2', 'TMEM161B', 'DRD2', 'PGBD1', 'ZKSCAN4', 'HIST1H1B', 'ERBB4', 'ZKSCAN8',
                'BTN3A2', 'PCLO', 'ZSCAN16', 'ZSCAN9', 'TMEM106B', 'MEF2C', 'OLFM4', 'GRM8', 'ZNF165', 'LRFN5',
                'OR2B2', 'HIST1H2BL', 'ZCCHC7', 'B3GALTL', 'BTN2A1', 'ZSCAN26', 'RERE', 'CDH13', 'ASTN2', 'CACNA1E',
                'HIST1H2AL', 'HLA-B', 'HIST1H4L', 'ZSCAN12', 'CHD6', 'CTNNA3', 'METTL9', 'MEGF11', 'ZSCAN31', 'ZNF197',
                'KLC1', 'ZNF660', 'SPPL3', 'YLPM1', 'PCDH9', 'ZNF445', 'ZKSCAN7', 'HIST1H3I', 'LIN28B', 'PAX5', 'PROX2',
                'FAM172A', 'CELF4', 'DLST', 'NRG1', 'SGCZ', 'OR12D3', 'RAB27B', 'IGSF6', 'GPC6', 'PAX6', 'SGIP1', 'KDM3A',
                'C16orf45', 'DCDC5', 'ESR2', 'LRP1B', 'EMILIN3', 'TRMT61A', 'XRCC3', 'SOX5', 'CNTNAP5', 'SEMA6D', 'ANKK1',
                'ZFHX4', 'LST1', 'PRSS16', 'TYR', 'RFWD2', 'PQLC2L', 'BTN1A1', 'DCDC1', 'ZDHHC21', 'TTC12', 'SDK1', 'APOPT1',
                'VRK2', 'CABP1', 'ZKSCAN3', 'SAMD5', 'ADCK3', 'DENND1B', 'TAOK3', 'HS6ST3', 'MYRF', 'RTN1', 'PSORS1C1', 'CKB',
                'SF3B1', 'FADS2', 'GTF2IRD1', 'NRD1', 'ZC3H7B', 'AREL1', 'RANGAP1', 'ZNF184', 'ZDHHC5', 'HIST1H2BF', 'FAM120A',
                'KIF15', 'NKAPL', 'FCF1', 'SORBS3', 'PCDHA2', 'PCDHA1', 'PRR34', 'SCYL1', 'MR1', 'BTN3A3', 'TCTEX1D1', 'CELF2', 'CTNND1',
                'HSPA1A', 'ASCC3', 'ELAVL2', 'HIST1H2BO', 'RPS6KL1', 'PCDHA3', 'TRMT10C', 'ABT1', 'SCAI', 'FADS1', 'CTTNBP2', 'KMT2A',
                'BEND4', 'ESRRG', 'BAZ2B', 'GPC5', 'IQCJ-SCHIP1', 'TCAIM', 'TMX2', 'SLC17A3', 'MED19', 'ZNF638', 'CDH22', 'GRIK5', 'HARS',
                'HSPE1-MOB4', 'EP300', 'HLA-DQB1', 'PCNP', 'ZHX3', 'BCHE', 'CRB1', 'C3orf84', 'MICB', 'SLC30A9', 'MARK3', 'FHIT', 'MARCH10',
                'CDK14', 'PLCG1', 'PSORS1C2', 'AP3B1', 'POGZ', 'TRAF3', 'CSMD1', 'TMEM67', 'PCDHA4', 'TOPAZ1', 'PMFBP1', 'CNTN5', 'INPP4B',
                'ZNF322', 'ASIC2', 'PLA2R1', 'CHMP3', 'SOX6', 'PCDHA5', 'FANCL', 'ZNF35', 'TMEM42', 'KIAA1143', 'C11orf31',
                'ACVR1B', 'ZNF501', 'RFTN2', 'TMEM258', 'TAL1', 'NICN1', 'HLA-DQA1', 'ACTL8', 'MOB4', 'CCDC36', 'PCDHA6', 'STK19',
                'RHOA', 'MAP9', 'FNIP2', 'RBMS3', 'PLCL1', 'SLC44A4', 'LTBP3', 'SPRY2', 'C7orf72', 'HTT', 'UBE2M', 'OTX2', 'BAG5', 'CDH9',
                'LPIN3', 'EPHB2', 'HMGN4', 'PPP6C', 'NOX4', 'PRR16', 'EXT1', 'MGAT4C', 'EYS', 'STAU1', 'HARS2', 'BAD', 'MYBPC3', 'ETFDH', 'SIM1',
                'FH', 'ANKS1B', 'ITPR3', 'RABEPK', 'RHOBTB1', 'BSN', 'RAB3B', 'ZNF536', 'TOP1', 'CAMKK2', 'MANEA', 'ARHGEF25', 'VPS41',
                'ATP1A3', 'ITGB6', 'ASXL3', 'ANKHD1', 'PCDHA7', 'PTPRS', 'CCS', 'PHF2', 'IK', 'KYNU', 'PPID', 'FAM120AOS', 'ZMAT2', 'SERPING1',
                'USP3', 'CACNA2D1', 'ANKHD1-EIF4EBP3', 'GINM1', 'C1QTNF7', 'MIER1', 'SLC4A9', 'PSEN2'}

    elif disorder is "epilepsy":
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

    elif disorder is "hippocampal_volume":
        return {'TESC','ACVR1','MSRB3','DPP4'}

    elif disorder is "ocd":
        return print("aye aye aye I've got nothin'")

    elif disorder is "schizophrenia":
        return {'xMHC','DPYD','MIR137','ARL3','AS3MT','C10orf32','CNNM2','CYP17A1','INA','NT5C2','PCGF6','PDCD11','SFXN2','TAF5','TRIM8',
                'USMG5','WBP1L','CACNA1C','TSNARE1','SLC39A8','MAD1L1','ZSWIM6','ABCB9','ARL6IP4','C12orf65','CDK2AP1','MPHOSPH9','OGFOD2',
                'PITPNM2','RILPL2','SBNO1','SETD8','AC073043.2','C2orf47','C2orf69','TYW5','FES','FURIN','MAN2A2','TRANK1','AL049840.1','APOPT1',
                'BAG5','CKB','KLC1','PPP1R13B','TRMT61A','XRCC3','ZFYVE21','AC027228.1','AGPHD1','CHRNA3','CHRNA5','CHRNB4','IREB2','PSMA4','IMMP2L',
                'SNX19','ZNF804A','CNKSR2','CACNB2','LRP1','MYO1A','NAB2','NDUFA4L2','NXPH4','R3HDM2','SHMT2','STAC3','STAT6','TAC3','TMEM194A','LRRIQ3',
                'C2orf82','EFHD1','GIGYF2','KCNJ13','NGEF','ESAM','MSANTD2','NRGN','VSIG2','TCF4','AMBRA1','ARHGAP1','ATG13','CHRM4','CKAP5','CREB3L1',
                'DGKZ','F2','HARBI1','MDK','ZNF408','CCDC39','DNAJC19','FXR1','ACTR5','PPP1R16B','SLC32A1','FANCL','VRK2','ADAMTSL3','GOLGA6L4','ZSCAN2',
                'TCF4','ANKRD44','BOLL','COQ10B','HSPD1','HSPE1','MARS2','PLCL1','RFTN2','SF3B1','CHADL','EP300','L3MBTL2','RANGAP1','KCNV1','CNTN4','DRD2',
                'IGSF9B','GLT8D1','GNL3','ITIH1','ITIH3','ITIH4','MUSTN1','NEK4','NISCH','NT5DC2','PBRM1','SMIM4','SPCS1','STAB1','TMEM110','TMEM110-MUSTN1',
                'ALDOA','ASPHD1','C16orf92','DOC2A','FAM57B','GDPD3','HIRIP3','INO80E','KCTD13','MAPK3','PPP4C','SEZ6L2','TAOK2','TBX6','TMEM219','YPEL3',
                'CACNA1I','MSL2','NCK1','PCCB','PPP2R3A','SLC35G2','STAG1','GRIA1 ','PJA1','SGSM2','SMG6','SRR','TSR1','GRM3','VPS14C','KDM4A','PTPRF','CILP2',
                'GATAD2A','HAPLN4','MAU2','NCAN','NDUFA13','PBX4','SUGP1','TM6SF2','TSSK6','ANP32E','APH1A','C1orf51','C1orf54','CA14','OTUD7B','PLEKHO1','VPS45',
                'SNAP91','PLCH2','ERCC4','MLL5','PUS7','SRPK2','RERE','SLC45A1','ATP2A2','C4orf27','CLCN3','NEK1','FUT9','CENPM','CYP2D6','FAM109B','NAGA','NDUFA6',
                'SEPT3','SHISA8','SMDT1','SREBF2','TCF20','TNFRSF13C','WBP2NL'}

    elif disorder is "tourette":
        return {'FLT3', 'OTUD1', 'LINC01122', 'MIR2113', 'CSMD3', 'MIR2053', 'EPB41', 'MECR', 'OPRD1',
                'PTPRU', 'SRSF4', 'TMEM200B', 'CDKN1A', 'KCTD20', 'MIR3925', 'PANDAR', 'PXT1', 'RAB44',
                'SRSF3', 'STK38', 'LOC402160', 'RNF4', 'ZFYVE28', 'AHCTF1P1', 'BAZ2B', 'CD302', 'DPP4',
                'ITGB6', 'LOC643072', 'LOC100505984', 'LOC100996579', 'LOC101929512', 'LY75', 'LY75-CD302',
                'MARCH7', 'MIR4785', 'PLA2R1', 'PSMD14', 'RBMS1', 'SLC4A10', 'TANC1', 'TANK', 'TBR1', 'WDSUB1',
                'FPR1', 'FPR2', 'FPR3', 'HCCAT3', 'LOC101928571', 'ZNF350', 'ZNF432', 'ZNF577', 'ZNF613',
                'ZNF614', 'ZNF615', 'ZNF616', 'ZNF649', 'ZNF841'}

    else:
        raise ValueError("must specify a valid disorder... but just one!")


def load_example_data():
    """ Loads the ENIGMA example dataset (from one site - MICA-MNI Montreal; author: @saratheriver)

    Returns
    -------
    cov : pandas.DataFrame
        Contains information on covariates
    metr1 : pandas.DataFrame
        Contains information on subcortical volume
    metr2 : pandas.DataFrame
        Contains information on cortical thickness
    metr3 : pandas.DataFrame
        Contains information on surface area
    """
    root_pth = os.path.dirname(__file__)

    cov = os.path.join(root_pth, 'xdata', 'cov.csv')
    metr1 = os.path.join(root_pth, 'xdata', 'metr1_SubVol.csv')
    metr2 = os.path.join(root_pth, 'xdata', 'metr2_CortThick.csv')
    metr3 = os.path.join(root_pth, 'xdata', 'metr3_CortSurf.csv')

    return pd.read_csv(cov, error_bad_lines=False), \
           pd.read_csv(metr1, error_bad_lines=False), \
           pd.read_csv(metr2, error_bad_lines=False), \
           pd.read_csv(metr3, error_bad_lines=False)


def load_summary_stats(disorder=None):
    """ Outputs summary statistics for a given disorder (author: @saratheriver)

        Parameters
        ----------
        disorder : {'22q', 'adhd', 'asd', 'bipolar', 'depression', 'epilepsy', 'ocd', 'schizophrenia'}
            Disorder name, default is None

        Returns
        -------
        summary_stats : pandas.DataFrame
            Available summary statistics
    """
    root_pth = os.path.dirname(__file__)

    if disorder is "22q":
        CortThick_case_controls = pd.read_csv(os.path.join(root_pth, 'summary_statistics',
                                             '22q_case-controls_CortThick.csv'), error_bad_lines=False)
        CortSurf_case_controls = pd.read_csv(os.path.join(root_pth, 'summary_statistics',
                                                         '22q_case-controls_CortSurf.csv'), error_bad_lines=False)
        CortThick_psychP_psychN = pd.read_csv(os.path.join(root_pth, 'summary_statistics',
                                                           '22q_psych+-psych-_CortThick.csv'), error_bad_lines=False)
        CortSurf_psychP_psychN = pd.read_csv(os.path.join(root_pth, 'summary_statistics',
                                                          '22q_psych+-psych-_CortSurf.csv'), error_bad_lines=False)
        return {'CortThick_case_vs_controls': CortThick_case_controls,
                'CortSurf_case_vs_controls': CortSurf_case_controls,
                'CortThick_psychP_vs_psychN': CortThick_psychP_psychN,
                'CortSurf_psychP_vs_psychN': CortSurf_psychP_psychN}

    elif disorder is "adhd":
        CortThick_case_controls_allages = pd.read_csv(os.path.join(root_pth, 'summary_statistics',
                                                                   'adhdallages_case-controls_CortThick.csv'),
                                                      error_bad_lines=False)
        CortSurf_case_controls_allages = pd.read_csv(os.path.join(root_pth, 'summary_statistics',
                                                                  'adhdallages_case-controls_CortSurf.csv'),
                                                     error_bad_lines=False)
        CortThick_case_controls_adult = pd.read_csv(os.path.join(root_pth, 'summary_statistics',
                                                                 'adhdadult_case-controls_CortThick.csv'),
                                                    error_bad_lines=False)
        CortSurf_case_controls_adult = pd.read_csv(os.path.join(root_pth, 'summary_statistics',
                                                                'adhdadult_case-controls_CortSurf.csv'),
                                                   error_bad_lines=False)
        CortThick_case_controls_adolescent = pd.read_csv(os.path.join(root_pth, 'summary_statistics',
                                                                      'adhdadolescent_case-controls_CortThick.csv'),
                                                         error_bad_lines=False)
        CortSurf_case_controls_adolescent = pd.read_csv(os.path.join(root_pth, 'summary_statistics',
                                                                     'adhdadolescent_case-controls_CortSurf.csv'),
                                                        error_bad_lines=False)
        CortThick_case_controls_pediatric = pd.read_csv(os.path.join(root_pth, 'summary_statistics',
                                                                     'adhdpediatric_case-controls_CortThick.csv'),
                                                        error_bad_lines=False)
        CortSurf_case_controls_pediatric = pd.read_csv(os.path.join(root_pth, 'summary_statistics',
                                                                    'adhdpediatric_case-controls_CortSurf.csv'),
                                                       error_bad_lines=False)

        return {'CortThick_case_vs_controls_allages': CortThick_case_controls_allages,
                'CortSurf_case_vs_controls_allages': CortSurf_case_controls_allages,
                'CortThick_case_vs_controls_adult': CortThick_case_controls_adult,
                'CortSurf_case_vs_controls_adult': CortSurf_case_controls_adult,
                'CortThick_case_vs_controls_adolescent': CortThick_case_controls_adolescent,
                'CortSurf_case_vs_controls_adolescent': CortSurf_case_controls_adolescent,
                'CortThick_case_vs_controls_pediatric': CortThick_case_controls_pediatric,
                'CortSurf_case_vs_controls_pediatric': CortSurf_case_controls_pediatric}

    elif disorder is "asd":
        CortThick_case_controls_meta_analysis = pd.read_csv(os.path.join(root_pth, 'summary_statistics',
                                                                         'asd_meta-analysis_case-controls_CortThick.csv'),
                                                            error_bad_lines=False)
        CortThick_case_controls_mega_analysis = pd.read_csv(os.path.join(root_pth, 'summary_statistics',
                                                                         'asd_mega-analysis_case-controls_CortThick.csv'),
                                                            error_bad_lines=False)

        return {'CortThick_case_vs_controls_meta_analysis': CortThick_case_controls_meta_analysis,
                'CortThick_case_vs_controls_mega_analysis': CortThick_case_controls_mega_analysis}

    elif disorder is "bipolar":
        CortSurf_case_controls = pd.read_csv(os.path.join(root_pth, 'summary_statistics',
                                                          'bd_case-controls_CortSurf.csv'), error_bad_lines=False)

        return {'CortSurf_case_vs_controls': CortSurf_case_controls}

    elif disorder is "depression":
        CortThick_case_controls_adult = pd.read_csv(os.path.join(root_pth, 'summary_statistics',
                                                                 'mddadult_case-controls_CortThick.csv'),
                                                    error_bad_lines=False)
        CortSurf_case_controls_adult = pd.read_csv(os.path.join(root_pth, 'summary_statistics',
                                                                 'mddadult_case-controls_CortSurf.csv'),
                                                    error_bad_lines=False)
        CortThick_case_controls_adolescent = pd.read_csv(os.path.join(root_pth, 'summary_statistics',
                                                                      'mddadolescent_case-controls_CortThick.csv'),
                                                         error_bad_lines=False)
        CortSurf_case_controls_adolescent = pd.read_csv(os.path.join(root_pth, 'summary_statistics',
                                                                     'mddadolescent_case-controls_CortSurf.csv'),
                                                        error_bad_lines=False)

        return {'CortThick_case_vs_controls_adult': CortThick_case_controls_adult,
                'CortSurf_case_vs_controls_adult': CortSurf_case_controls_adult,
                'CortThick_case_vs_controls_adolescent': CortThick_case_controls_adolescent,
                'CortSurf_case_vs_controls_adolescent': CortSurf_case_controls_adolescent}

    elif disorder is "epilepsy":
        CortThick_case_controls_allepilepsy = pd.read_csv(os.path.join(root_pth, 'summary_statistics',
                                                                       'allepi_case-controls_CortThick.csv'),
                                                          error_bad_lines=False)
        SubVol_case_controls_allepilepsy = pd.read_csv(os.path.join(root_pth, 'summary_statistics',
                                                                    'allepi_case-controls_SubVol.csv'),
                                                       error_bad_lines=False)
        CortThick_case_controls_gge = pd.read_csv(os.path.join(root_pth, 'summary_statistics',
                                                               'gge_case-controls_CortThick.csv'),
                                                  error_bad_lines=False)
        SubVol_case_controls_gge = pd.read_csv(os.path.join(root_pth, 'summary_statistics',
                                                            'gge_case-controls_SubVol.csv'),
                                               error_bad_lines=False)
        CortThick_case_controls_ltle = pd.read_csv(os.path.join(root_pth, 'summary_statistics',
                                                                'tlemtsl_case-controls_CortThick.csv'),
                                                   error_bad_lines=False)
        SubVol_case_controls_ltle = pd.read_csv(os.path.join(root_pth, 'summary_statistics',
                                                             'tlemtsl_case-controls_SubVol.csv'),
                                                error_bad_lines=False)
        CortThick_case_controls_rtle = pd.read_csv(os.path.join(root_pth, 'summary_statistics',
                                                                'tlemtsr_case-controls_CortThick.csv'),
                                                   error_bad_lines=False)
        SubVol_case_controls_rtle = pd.read_csv(os.path.join(root_pth, 'summary_statistics',
                                                             'tlemtsr_case-controls_SubVol.csv'),
                                                error_bad_lines=False)

        return {'CortThick_case_vs_controls_allepilepsy': CortThick_case_controls_allepilepsy,
                'SubVol_case_vs_controls_allepilepsy': SubVol_case_controls_allepilepsy,
                'CortThick_case_vs_controls_gge': CortThick_case_controls_gge,
                'SubVol_case_vs_controls_gge': SubVol_case_controls_gge,
                'CortThick_case_vs_controls_ltle': CortThick_case_controls_ltle,
                'SubVol_case_vs_controls_ltle': SubVol_case_controls_ltle,
                'CortThick_case_vs_controls_rtle': CortThick_case_controls_rtle,
                'SubVol_case_vs_controls_rtle': SubVol_case_controls_rtle}

    elif disorder is "ocd":
        CortThick_case_controls_adult = pd.read_csv(os.path.join(root_pth, 'summary_statistics',
                                                                 'ocdadults_case-controls_CortThick.csv'),
                                                    error_bad_lines=False)
        CortSurf_case_controls_adult = pd.read_csv(os.path.join(root_pth, 'summary_statistics',
                                                                 'ocdadults_case-controls_CortSurf.csv'),
                                                    error_bad_lines=False)
        CortThick_medicatedcase_controls_adult = pd.read_csv(os.path.join(root_pth, 'summary_statistics',
                                                                          'ocdadults_medicatedcase-controls_CortThick.csv'),
                                                             error_bad_lines=False)
        CortSurf_medicatedcase_controls_adult = pd.read_csv(os.path.join(root_pth, 'summary_statistics',
                                                                         'ocdadults_medicatedcase-controls_CortSurf.csv'),
                                                            error_bad_lines=False)
        CortThick_case_controls_pediatric = pd.read_csv(os.path.join(root_pth, 'summary_statistics',
                                                                     'ocdpediatric_case-controls_CortThick.csv'),
                                                        error_bad_lines=False)
        CortSurf_case_controls_pediatric = pd.read_csv(os.path.join(root_pth, 'summary_statistics',
                                                                    'ocdpediatric_case-controls_CortSurf.csv'),
                                                       error_bad_lines=False)
        CortThick_medicatedcase_controls_pediatric = pd.read_csv(os.path.join(root_pth, 'summary_statistics',
                                                                              'ocdpediatric_medicatedcase-controls_CortThick.csv'),
                                                                 error_bad_lines=False)
        CortSurf_medicatedcase_controls_pediatric = pd.read_csv(os.path.join(root_pth, 'summary_statistics',
                                                                             'ocdpediatric_medicatedcase-controls_CortSurf.csv'),
                                                                error_bad_lines=False)

        return {'CortThick_case_vs_controls_adult': CortThick_case_controls_adult,
                'CortSurf_case_vs_controls_adult': CortSurf_case_controls_adult,
                'CortThick_medicatedcase_vs_controls_adult': CortThick_medicatedcase_controls_adult,
                'CortSurf_medicatedcase_vs_controls_adult': CortSurf_medicatedcase_controls_adult,
                'CortThick_case_vs_controls_pediatric': CortThick_case_controls_pediatric,
                'CortSurf_case_vs_controls_pediatric': CortSurf_case_controls_pediatric,
                'CortThick_medicatedcase_vs_controls_pediatric': CortThick_medicatedcase_controls_pediatric,
                'CortSurf_medicatedcase_vs_controls_pediatric': CortSurf_medicatedcase_controls_pediatric}

    elif disorder is "schizophrenia":
        CortThick_case_controls = pd.read_csv(os.path.join(root_pth, 'summary_statistics',
                                                          'scz_case-controls_CortThick.csv'), error_bad_lines=False)
        CortSurf_case_controls = pd.read_csv(os.path.join(root_pth, 'summary_statistics',
                                                          'scz_case-controls_CortSurf.csv'), error_bad_lines=False)

        return {'CortThick_case_vs_controls': CortThick_case_controls,
                'CortSurf_case_vs_controls': CortSurf_case_controls}

    else:
        raise ValueError("must specify a valid disorder...!")


def reorder_sum_stats(in_file, out_file):
    """
    Re-order cortical structures in summary statistics files

    in_file = pd dataframe (sum_stats)
    """
    # Load in_fil
    in_file = pd.read_csv(in_file, error_bad_lines=False)

    # Get original order properly
    _, _, d_orig, _ = load_example_data()
    d_orig.columns = d_orig.columns.str.rstrip('_thickavg')
    d_orig = list(d_orig.columns)[1:-5]
    d_orig[len(d_orig)//2-1] = 'L_insula'
    d_orig[-1] = 'R_insula'

    # Reorder summary stats
    newidx = []
    for j in range(len(d_orig)):
        newidx = np.append(newidx, [i for i, e in enumerate(in_file['Structure'].to_list()) if e == d_orig[j]])

    out = in_file.iloc[newidx]

    return out.to_csv(out_file, index=False)

"""
    For every new summary statistic file, run the following command to reorder
    cortical structures according to ENIGMA mega-analysis protocols!
    
    * only run for CortThick and CortSurf
    ------------------------------------------------------------------------------------

    in_file = '/Users/saratheriver/Desktop/McGill_PhD/ENIGMA/enigmatoolbox/datasets/summary_statistics/tlemtsl_case-controls_CortThick.csv'
    reorder_sum_stats(in_file, in_file)
"""