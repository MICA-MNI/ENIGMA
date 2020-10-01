"""
Figure 1a. Load summary statistics
"""
from enigmatoolbox.datasets import load_summary_stats

# Load summary statistics for a given disease (e.g., epilepsy)
sum_stats = load_summary_stats('epilepsy')

# Get cortical thickness and subcortical volume tables
CT = sum_stats['CortThick_case_vs_controls_ltle']
SV = sum_stats['SubVol_case_vs_controls_ltle']

# Extract Cohen's d values
CT_d = CT['d_icv']
SV_d = SV['d_icv']


"""
Figure 2a. Surface data visualization
"""
from enigmatoolbox.utils.parcellation import parcel_to_surface
from enigmatoolbox.plotting import plot_cortical, plot_subcortical

# Map parcellated data to the surface (cortical values only)
CT_d_fsa5 = parcel_to_surface(CT_d, 'aparc_fsa5')

# Project Cohen's d values to the surface templates
plot_cortical(array_name=CT_d_fsa5, surface_name="fsa5",
              size=(800, 400), cmap='TealRd', color_bar=True, color_range=(-0.5, 0.5))

plot_subcortical(array_name=SV_d, size=(800, 400),
                 cmap='TealRd', color_bar=True, color_range=(-0.5, 0.5))


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

# Remove subcortical values corresponding to the ventricles
SV_d_noVent = SV_d.drop([np.where(SV['Structure'] == 'LLatVent')[0][0],
                        np.where(SV['Structure'] == 'RLatVent')[0][0]])
SV_d_noVent = SV_d_noVent.reset_index(drop=True)

# Compute weighted degree centrality measures
fc_ctx_dc = np.sum(fc_ctx, axis=0)
fc_sctx_dc = np.sum(fc_sctx, axis=1)

# Perform spatial correlations between hubs and Cohen's d
fc_ctx_r = np.corrcoef(fc_ctx_dc, CT_d)[0, 1]
fc_sctx_r = np.corrcoef(fc_sctx_dc, SV_d_noVent)[0, 1]


"""
Figure 5d. Permutation testing
"""
from enigmatoolbox.permutation_testing import spin_test, shuf_test

# Spin permutation testing for two cortical maps
fc_ctx_p = spin_test(fc_ctx_dc, CT_d, surface_name='fsa5', parcellation_name='aparc', n_rot=100)

# Shuf permutation testing for two subcortical maps
fc_sctx_p = shuf_test(fc_sctx_dc, SV_d_noVent, n_rot=1000)

map1 = np.append(fc_ctx_dc, fc_sctx_dc)
map2 = np.append(CT_d, SV_d_noVent)
p, d = shuf_test(map1, map2, n_rot=1000, spin_dist=True)

"""
Figure 6a. Disease epicenter mapping
"""
import numpy as np
from enigmatoolbox.permutation_testing import spin_test

# Identify cortical epicenters
fc_ctx_epi = []
fc_ctx_epi_p = []
for seed in range(fc_ctx.shape[0]):
    seed_con = fc_ctx[:, seed]
    fc_ctx_epi = np.append(fc_ctx_epi, np.corrcoef(seed_con, CT_d)[0, 1])
    fc_ctx_epi_p = np.append(fc_ctx_epi_p,
                             spin_test(seed_con, CT_d, surface_name='fsa5', n_rot=100))

# Identify subcortical epicenters
fc_sctx_epi = []
fc_sctx_epi_p = []
for seed in range(fc_sctx.shape[0]):
    seed_con = fc_sctx[seed, :]
    fc_sctx_epi = np.append(fc_sctx_epi, np.corrcoef(seed_con, CT_d)[0, 1])
    fc_sctx_epi_p = np.append(fc_sctx_epi_p,
                              spin_test(seed_con, CT_d, surface_name='fsa5', n_rot=100))
