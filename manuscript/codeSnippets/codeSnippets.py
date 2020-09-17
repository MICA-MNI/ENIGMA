"""
Figure 1a. Load example data
"""
from enigmatoolbox.datasets import load_example_data
from enigmatoolbox.utils.useful import zscore_matrix

# Load example data
cov, metr1_SubVol, metr2_CortThick, metr3_CortSurf = load_example_data()

# Z-score data in patients relative to controls
groups = cov['Dx'].to_list()
controlGroup = 0
CortThick_Z = zscore_matrix(metr2_CortThick.iloc[:, 1:-5], groups, controlGroup)
SubVol_Z = zscore_matrix(metr1_SubVol.iloc[:, 1:-1], groups, controlGroup)

# Extract data for a specific group (e.g., individuals with left TLE)
CortThick_Z_LTLE = CortThick_Z.iloc[cov[cov['SDx'] == 3].index, :]
SubVol_Z_LTLE = SubVol_Z.iloc[cov[cov['SDx'] == 3].index, :]


"""
Figure 2a. Surface data visualization
"""
from enigmatoolbox.utils.useful import reorder_sctx
import numpy as np
from enigmatoolbox.utils.parcellation import parcel_to_surface
from enigmatoolbox.plotting import plot_cortical, plot_subcortical

# Re-order subcortical data (alphabetically and by hemisphere)
SubVol_Z_LTLE_r = reorder_sctx(SubVol_Z_LTLE)

# Mean data across all individuals with left TLE
CortThick_Z_LTLE_mean = np.mean(CortThick_Z_LTLE, axis=0)
SubVol_Z_LTLE_r_mean = np.mean(SubVol_Z_LTLE_r, axis=0)

# Map parcellated data to the surface (cortical values only)
CortThick_Z_LTLE_mean_fsa5 = parcel_to_surface(CortThick_Z_LTLE_mean, 'aparc_fsa5')

# Project data to the surface templates
plot_cortical(array_name=CortThick_Z_LTLE_mean_fsa5, surface_name="fsa5",
              size=(800, 400), cmap='Blues_r', color_bar=True, color_range=(-2, 0))

plot_subcortical(array_name=SubVol_Z_LTLE_r_mean, size=(800, 400),
                 cmap='Blues_r', color_bar=True, color_range=(-3, 0))


"""
Figure 3a. Fetch disease-related gene expression data
"""
from enigmatoolbox.datasets import fetch_ahba, risk_genes

# Fetch gene expression data
genes = fetch_ahba()

# Get the names of epilepsy-related genes (Focal HS phenotype)
epilepsy_genes = risk_genes('epilepsy')['focalhs']

# Extract gene expression data for epilepsy (Focal HS)
epilepsy_gene_data = genes[genes.columns.intersection(epilepsy_genes)]


"""
Figure 4a. Load connectivity data
"""
from enigmatoolbox.datasets import load_fc, load_sc

# Load functional connectivity data
fc_ctx, fc_ctx_labels, fc_sctx, fc_sctx_labels = load_fc()

# Load structural connectivity data
sc_ctx, sc_ctx_labels, sc_sctx, sc_sctx_labels = load_sc()


"""
Figure 5a. Hub susceptibility model
"""
import numpy as np
from enigmatoolbox.permutation_testing import spin_test, shuf_test

# Remove subcortical values corresponding to the ventricles
SubVol_Z_LTLE_r_mean_noVent = SubVol_Z_LTLE_r_mean.drop(['LLatVent', 'RLatVent'])

# Compute weighted degree centrality measures
fc_ctx_dc = np.sum(fc_ctx, axis=0)
fc_sctx_dc = np.sum(fc_sctx, axis=1)

# Perform spatial correlations between hubs and mean atrophy
fc_ctx_r = np.corrcoef(fc_ctx_dc, CortThick_Z_LTLE_mean)[0, 1]
fc_sctx_r = np.corrcoef(fc_sctx_dc, SubVol_Z_LTLE_r_mean_noVent)[0, 1]

# Spin permutation testing for two cortical maps
fc_ctx_p = spin_test(fc_ctx_dc, CortThick_Z_LTLE_mean, surface_name='fsa5',
                     n_rot=1000, type='pearson')

# Shuf permutation testing for two subcortical maps
fc_sctx_p = shuf_test(fc_sctx_dc, SubVol_Z_LTLE_r_mean_noVent,
                      n_rot=1000, type='pearson')


"""
Figure 6a. Disease epicenter mapping
"""
import numpy as np
from enigmatoolbox.permutation_testing import spin_test

# Identify functional epicenters
fc_ctx_epi = []
fc_ctx_epi_p = []
for seed in range(fc_ctx.shape[0]):
    seed_con = fc_ctx[:, seed]
    fc_ctx_epi = np.append(fc_ctx_epi, np.corrcoef(seed_con, CortThick_Z_LTLE_mean)[0, 1])
    fc_ctx_epi_p = spin_test(seed_con, CortThick_Z_LTLE_mean, surface_name='fsa5',
                         n_rot=1000, type='pearson')

fc_sctx_epi = []
fc_sctx_epi_p = []
for seed in range(fc_sctx.shape[0]):
    seed_con = fc_sctx[seed, :]
    fc_sctx_epi = np.append(fc_sctx_epi, np.corrcoef(seed_con, CortThick_Z_LTLE_mean)[0, 1])
    fc_sctx_epi_p = spin_test(seed_con, CortThick_Z_LTLE_mean, surface_name='fsa5',
                             n_rot=1000, type='pearson')
