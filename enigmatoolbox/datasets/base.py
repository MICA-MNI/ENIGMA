import os
import numpy as np
import pandas as pd

from vtk import vtkPolyDataNormals

from ..mesh.mesh_io import read_surface
from ..mesh.mesh_operations import combine_surfaces
from ..utils.parcellation import surface_to_parcel
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


def risk_genes(disorder=None):
    """ Outputs names of GWAS-derived risk genes for specific diseases/disorders

        Parameters (pick one)
        ---------------------
        'adhd'               : Demontis et al., 2018, Nat Genet
        'asd'                : Grove et al., 2019, Nat Genet
        'bipolar'            : Stahl et al., 2019, Nat Genet
        'depression'         : Howard et al., 2019, Nat Genet
        'epilepsy'           : ILAE on Complex Epilepsies, 2018, Nat Commun
        'hippocampal_volume' : Horgusluoglu-Moloch, 2019, Sci Rep
        'ocd'                : n/a
        'schizophrenia'      : Pardiñas et al., 2018, Nat Genet
        'tourette'           : Yu et al., 2019 Am J Psychiatry

        Returns
        -------
        dx_gx : names of genes for specified disorder
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
    """ Loads ENIGMA example dataset (from one site - MICA-MNI Montreal)
            Processed according to ENIGMA protocols

        Returns
        -------
        cov   : contains information on covariates (panda dataframe)
        metr1 : contains information on subcortical volume
        metr2 : contains information on cortical thickness
        metr3 : contains information on surface area
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