from enigmatoolbox.datasets import load_summary_stats

# Load summary statistics for ENIGMA-Epilepsy
sum_stats = load_summary_stats('epilepsy')

# Get case-control subcortical volume and cortical thickness tables
SV = sum_stats['SubVol_case_vs_controls_ltle']
CT = sum_stats['CortThick_case_vs_controls_ltle']

# Extract Cohen's d values
SV_d = SV['d_icv']
CT_d = CT['d_icv']


from enigmatoolbox.datasets import load_sc, load_fc
# Load and plot cortical functional connectivity data
fc_ctx, fc_ctx_labels, _, _ = load_fc()

# Load and plot cortical structural connectivity data
sc_ctx, sc_ctx_labels, _, _ = load_sc()


from enigmatoolbox.datasets import load_sc, load_fc
# Load and plot subcortical functional connectivity data
_, _, fc_sctx, fc_sctx_labels = load_fc()

# Load and plot subcortical structural connectivity data
_, _, sc_sctx, sc_sctx_labels = load_sc()


import numpy as np
# Compute weighted degree centrality measures from the connectivity data
fc_ctx_dc = np.sum(fc_ctx, axis=0)
sc_ctx_dc = np.sum(sc_ctx, axis=0)


import numpy as np
# Compute weighted degree centrality measures from the connectivity data
fc_sctx_dc = np.sum(fc_sctx, axis=1)
sc_sctx_dc = np.sum(sc_sctx, axis=1)


import numpy as np
# Remove subcortical values corresponding the ventricles
# (as we don't have connectivity values for them!)
SV_d_noVent = SV_d.drop([np.where(SV['Structure'] == 'LLatVent')[0][0],
                        np.where(SV['Structure'] == 'RLatVent')[0][0]])
SV_d_noVent = SV_d_noVent.reset_index(drop=True)

# Perform spatial correlations between cortical hubs and Cohen's d
fc_ctx_r = np.corrcoef(fc_ctx_dc, CT_d)[0, 1]
sc_ctx_r = np.corrcoef(sc_ctx_dc, CT_d)[0, 1]

# Perform spatial correlations between subcortical hubs and Cohen's d
fc_sctx_r = np.corrcoef(fc_sctx_dc, SV_d_noVent)[0, 1]
sc_sctx_r = np.corrcoef(sc_sctx_dc, SV_d_noVent)[0, 1]


from enigmatoolbox.permutation_testing import spin_test, shuf_test

# Spin permutation testing for two cortical maps
fc_ctx_p, fc_ctx_d = spin_test(fc_ctx_dc, CT_d, surface_name='fsa5', parcellation_name='aparc',
                               type='pearson', n_rot=1000, spin_dist=True)
sc_ctx_p, sc_ctx_d = spin_test(sc_ctx_dc, CT_d, surface_name='fsa5', parcellation_name='aparc',
                               type='pearson', n_rot=1000, spin_dist=True)

# Shuf permutation testing for two subcortical maps
fc_sctx_p, fc_sctx_d = shuf_test(fc_sctx_dc, SV_d_noVent, n_rot=1000,
                                 type='pearson', spin_dist=True)
sc_sctx_p, sc_sctx_d = shuf_test(sc_sctx_dc, SV_d_noVent, n_rot=1000,
                                 type='pearson', spin_dist=True)


import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from enigmatoolbox.plotting import enigma_scatter

fig = plt.figure(constrained_layout=True, figsize=(15, 3))
gs = gridspec.GridSpec(1, 4, figure=fig)

# Functional cortical hubs and cortical thickness
ax1 = fig.add_subplot(gs[0, 0])
enigma_scatter(ax1, fc_ctx_dc, CT_d, scatter_color='#A8221C', linear_fit=True, fit_color='#A8221C',
               xlabel='Cortico-cortical degree centrality', ylabel='Cortical thickness (z-score)',
               xlim=(5, 30), ylim=(-1, 0.5), corr_value=fc_ctx_r, p_value=fc_ctx_p)

# Functional subcortical hubs and subcortical volume
ax2 = fig.add_subplot(gs[0, 1])
enigma_scatter(ax2, fc_sctx_dc, SV_d_noVent, scatter_color='#A8221C', linear_fit=True, fit_color='#A8221C',
               xlabel='Subcortico-cortical degree centrality', ylabel='Subcortical volume (z-score)',
               xlim=(1, 13), ylim=(-1, 0.5), corr_value=fc_sctx_r, p_value=fc_sctx_p, p_type='shuf')

# Structural cortical hubs and cortical thickness
ax3 = fig.add_subplot(gs[0, 2])
enigma_scatter(ax3, sc_ctx_dc, CT_d, scatter_color='#324F7D', linear_fit=True, fit_color='#324F7D',
               xlabel='Cortico-cortical degree centrality', ylabel='Cortical thickness (z-score)',
               xlim=(0, 350), ylim=(-1, 0.5), corr_value=sc_ctx_r, p_value=sc_ctx_p)

# Functional subcortical hubs and subcortical volume
ax4 = fig.add_subplot(gs[0, 3])
enigma_scatter(ax4, sc_sctx_dc, SV_d_noVent, scatter_color='#324F7D', linear_fit=True, fit_color='#324F7D',
               xlabel='Subcortico-cortical degree centrality', ylabel='Subcortical volume (z-score)',
               xlim=(90, 375), ylim=(-1, 0.5), corr_value=sc_sctx_r, p_value=sc_sctx_p, p_type='shuf')