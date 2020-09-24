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

# Project data to the surface templates
plot_cortical(array_name=CT_d_fsa5, surface_name="fsa5",
              size=(800, 400), cmap='RdBu_r', color_bar=True, color_range=(-0.5, 0.5))

plot_subcortical(array_name=SV_d, size=(800, 400),
                 cmap='RdBu_r', color_bar=True, color_range=(-0.5, 0.5))


"""
Figure 3a. Fetch disease-related gene expression data
"""
from enigmatoolbox.datasets import fetch_ahba, risk_genes
import numpy as np

# Fetch gene expression data
genes = fetch_ahba()

# Get the names of epilepsy-related genes (Focal HS phenotype)
epilepsy_genes = risk_genes('epilepsy')['focalhs']

# Extract gene expression data for epilepsy (Focal HS)
epilepsy_gene_data = genes[genes.columns.intersection(epilepsy_genes)]

# Project data to the surface templates
plot_cortical(array_name=parcel_to_surface(np.mean(epilepsy_gene_data, axis=1)[:68], 'aparc_fsa5'), nan_color=(1, 1, 1, 1),
              surface_name="fsa5", size=(800, 400), cmap='Greys', color_bar=True, color_range=(0.4, 0.6))

plot_subcortical(array_name=np.mean(epilepsy_gene_data, axis=1)[68:], ventricles=False, size=(800, 400),
                 cmap='Greys', color_bar=True, color_range=(0.4, 0.6))


"""
Figure 4a. Load connectivity data
"""
from enigmatoolbox.datasets import load_fc, load_sc
from nilearn import plotting
import numpy as np

# Load and plot functional connectivity data
fc_ctx, fc_ctx_labels, fc_sctx, fc_sctx_labels = load_fc()

fc_plot_ctx = plotting.plot_matrix(np.tril(fc_ctx), figure=(11,11), labels=fc_ctx_labels, vmax=0.8, vmin=0, cmap='Reds')
fc_plot_ctx.axes.spines['right'].set_visible(False)
fc_plot_ctx.axes.spines['top'].set_visible(False)
fc_plot_ctx.axes.set_xticklabels('')
fc_plot_ctx.axes.set_xticks([-1])

fc_plot_sctx = plotting.plot_matrix(fc_sctx, figure=(11,11), labels=fc_sctx_labels, vmax=0.8, vmin=0, cmap='Reds')
fc_plot_sctx.axes.spines['right'].set_visible(False)
fc_plot_sctx.axes.spines['top'].set_visible(False)
fc_plot_sctx.axes.set_xticks(range(fc_ctx.shape[1]))
fc_plot_sctx.axes.set_xticklabels(fc_ctx_labels)

# Load and plot structural connectivity data
sc_ctx, sc_ctx_labels, sc_sctx, sc_sctx_labels = load_sc()

sc_plot_ctx = plotting.plot_matrix(np.triu(sc_ctx), figure=(11, 11), labels=sc_ctx_labels, vmax=10, vmin=0, cmap='Blues')
sc_plot_ctx.axes.set_xticklabels('')
sc_plot_ctx.axes.set_xticks([-1])
sc_plot_ctx.axes.set_yticklabels('')
sc_plot_ctx.axes.set_yticks([-1])
sc_plot_ctx.axes.spines['left'].set_visible(False)
sc_plot_ctx.axes.spines['bottom'].set_visible(False)

sc_plot_sctx = plotting.plot_matrix(sc_sctx, figure=(11,11), labels=sc_sctx_labels, vmax=10, vmin=0, cmap='Blues')
sc_plot_sctx.axes.spines['left'].set_visible(False)
sc_plot_sctx.axes.spines['top'].set_visible(False)
sc_plot_sctx.axes.set_xticklabels('')
sc_plot_sctx.axes.set_xticks([-1])
sc_plot_sctx.axes.set_yticklabels('')
sc_plot_sctx.axes.set_yticks([-1])

"""
Figure 5a. Hub susceptibility model
"""
import numpy as np
from enigmatoolbox.utils.parcellation import parcel_to_surface
from enigmatoolbox.plotting import plot_cortical, plot_subcortical
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from enigmatoolbox.plotting import enigma_scatter

# Remove subcortical values corresponding to the ventricles
SV_d_noVent = SV_d.drop([np.where(SV['Structure'] == 'LLatVent')[0][0],
                        np.where(SV['Structure'] == 'RLatVent')[0][0]])
SV_d_noVent = SV_d_noVent.reset_index(drop=True)

# Compute and plot weighted degree centrality measures
fc_ctx_dc = np.sum(fc_ctx, axis=0)
fc_sctx_dc = np.sum(fc_sctx, axis=1)

plot_cortical(array_name=parcel_to_surface(fc_ctx_dc, 'aparc_fsa5'), nan_color=(1, 1, 1, 1),
              surface_name="fsa5", size=(800, 400), cmap='Reds', color_bar=True, color_range=(20, 30))

plot_subcortical(array_name=fc_sctx_dc, ventricles=False, size=(800, 400),
                 cmap='Reds', color_bar=True, color_range=(5, 10))

# Perform and plot spatial correlations between hubs and Cohen's d
fc_ctx_r = np.corrcoef(fc_ctx_dc, CT_d)[0, 1]
fc_sctx_r = np.corrcoef(fc_sctx_dc, SV_d_noVent)[0, 1]

fig = plt.figure(constrained_layout=True, figsize=(8, 3))
gs = gridspec.GridSpec(1, 2, figure=fig)

ax1 = fig.add_subplot(gs[0, 0])
enigma_scatter(ax1, fc_ctx_dc, CT_d, scatter_color='#A8221C', linear_fit=True, fit_color='#A8221C',
               xlabel='Cortico-cortical degree centrality', ylabel='Cortical thickness (z-score)',
               xlim=(5, 30), ylim=(-1, 0.5), corr_value=fc_ctx_r)

ax2 = fig.add_subplot(gs[0, 1])
enigma_scatter(ax2, fc_sctx_dc, SV_d_noVent, scatter_color='#A8221C', linear_fit=True, fit_color='#A8221C',
               xlabel='Subcortico-cortical degree centrality', ylabel='Subcortical volume (z-score)',
               xlim=(1, 13), ylim=(-1, 0.5), corr_value=fc_sctx_r)


"""
Figure 5d. Permutation testing
"""
from enigmatoolbox.permutation_testing import spin_test, shuf_test

# Spin permutation testing for two cortical maps
fc_ctx_p = spin_test(fc_ctx_dc, CT_d, surface_name='fsa5', n_rot=1000)

# Shuf permutation testing for two subcortical maps
fc_sctx_p = shuf_test(fc_sctx_dc, SV_d_noVent, n_rot=1000)


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
    fc_ctx_epi = np.append(fc_ctx_epi, np.corrcoef(seed_con, CT_d)[0, 1])
    fc_ctx_epi_p = np.append(fc_ctx_epi_p,
                             spin_test(seed_con, CT_d, surface_name='fsa5', n_rot=100))

fc_sctx_epi = []
fc_sctx_epi_p = []
for seed in range(fc_sctx.shape[0]):
    seed_con = fc_sctx[seed, :]
    fc_sctx_epi = np.append(fc_sctx_epi, np.corrcoef(seed_con, CT_d)[0, 1])
    fc_sctx_epi_p = np.append(fc_sctx_epi_p,
                              spin_test(seed_con, CT_d, surface_name='fsa5', n_rot=100))
