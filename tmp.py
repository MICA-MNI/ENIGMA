import numpy as np
from enigmatoolbox.datasets import load_example_data
from enigmatoolbox.utils.useful import zscore_matrix, reorder_sctx
from enigmatoolbox.datasets import load_sc, load_fc

"""
1 - Let's start by loading our example data
"""
# Here we need the covariates, cortical thickness, and subcortical volume data
cov, metr1_SubVol, metr2_CortThick, _ = load_example_data()

# After loading our subcortical data, we must re-order them (alphabetically and by hemisphere)
# so to match the order from the connectivity matrices
metr1_SubVol_r = reorder_sctx(metr1_SubVol)

# We must also remove subcortical values corresponding the ventricles (as we don't have connectivity values for them!)
metr1_SubVol_r = metr1_SubVol_r.drop(columns=['LLatVent', 'RLatVent'])


"""
2 - We can then z-score data in patients relative to controls, so that lower values
    correspond to greater atrophy
"""
# Z-score patients' data relative to controls (lower z-score = more atrophy)
group = cov['Dx'].to_list()
controlCode = 0
sv = zscore_matrix(metr1_SubVol_r.iloc[:, 1:-1], group, controlCode)
ct = zscore_matrix(metr2_CortThick.iloc[:, 1:-5], group, controlCode)

# Mean z-score values across individuals with left TLE (SDx == 3)
ct_tle = np.mean(ct.to_numpy()[cov[cov['SDx'] == 3].index, :], axis=0)
sv_tle = np.mean(sv.to_numpy()[cov[cov['SDx'] == 3].index, :], axis=0)


"""
3 - Let's then load our functional and structural connectivity matrices
    and compute degree centrality metrics to identify the spatial distribution
    of hubs
"""
# Load functional and structural cortico-cortical connectivity data (for simplicity, we won't load the regions' labels)
fc_ctx, _, fc_sctx, _ = load_fc()
sc_ctx, _, sc_sctx, _ = load_sc()

# Compute weighted degree centrality measures from the functional connectivity data
fc_ctx_dc = np.sum(fc_ctx, axis=0)
fc_sctx_dc = np.sum(fc_sctx, axis=1)

# Compute weighted degree centrality measures from the structural connectivity data
sc_ctx_dc = np.sum(sc_ctx, axis=0)
sc_sctx_dc = np.sum(sc_sctx, axis=1)


"""
4 - We can now perform spatial correlations between decreases in cortical thickness/
    subcortical volume and functional/structural degree centrality maps
"""
# Perform spatial correlations between functional hubs and atrophy
fc_ctx_r = np.corrcoef(fc_ctx_dc, ct_tle)[0, 1]
fc_sctx_r = np.corrcoef(fc_sctx_dc, sv_tle)[0, 1]

# Perform spatial correlations between structural hubs and atrophy
sc_ctx_r = np.corrcoef(sc_ctx_dc, ct_tle)[0, 1]
sc_sctx_r = np.corrcoef(sc_sctx_dc, sv_tle)[0, 1]


"""
5 - We can also perform permutation tests to check whether our correlations are significant
"""
from enigmatoolbox.permutation_testing import spin_test, shuf_test

# Spin permutation testing for two cortical maps
fc_ctx_p = spin_test(fc_ctx_dc, ct_tle, surface_name='fsa5', n_rot=1000, type='pearson')
sc_ctx_p = spin_test(sc_ctx_dc, ct_tle, surface_name='fsa5', n_rot=1000, type='pearson')

# Shuf permutation testing for two subcortical maps
fc_sctx_p = shuf_test(fc_sctx_dc, sv_tle, n_rot=1000, type='pearson')
sc_sctx_p = shuf_test(sc_sctx_dc, sv_tle, n_rot=1000, type='pearson')



import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from enigmatoolbox.plotting import scatter

fig = plt.figure(constrained_layout=True, figsize=(15, 3))
gs = gridspec.GridSpec(1, 4, figure=fig)

# Functional cortical hubs and cortical thickness
ax1 = fig.add_subplot(gs[0, 0])
scatter(ax1, fc_ctx_dc, ct_tle, scatter_color='#A8221C', linear_fit=True, fit_color='#A8221C',
        xlabel='Cortico-cortical degree centrality', ylabel='Cortical thickness (z-score)',
        xlim=(5, 30), ylim=(-2, 1), corr_value=fc_ctx_r, p_value=fc_ctx_p)

# Functional subcortical hubs and subcortical volume
ax2 = fig.add_subplot(gs[0, 1])
scatter(ax2, fc_sctx_dc, sv_tle, scatter_color='#A8221C', linear_fit=True, fit_color='#A8221C',
        xlabel='Subcortico-cortical degree centrality', ylabel='Subcortical volume (z-score)',
        xlim=(1, 13), ylim=(-3.5, 0), corr_value=fc_sctx_r, p_value=fc_sctx_p, p_type='shuf')

# Structural cortical hubs and cortical thickness
ax3 = fig.add_subplot(gs[0, 2])
scatter(ax3, sc_ctx_dc, ct_tle, scatter_color='#324F7D', linear_fit=True, fit_color='#324F7D',
        xlabel='Cortico-cortical degree centrality', ylabel='Cortical thickness (z-score)',
        xlim=(0, 350), ylim=(-2, 1), corr_value=sc_ctx_r, p_value=sc_ctx_p)

# Functional subcortical hubs and subcortical volume
ax4 = fig.add_subplot(gs[0, 3])
scatter(ax4, sc_sctx_dc, sv_tle, scatter_color='#324F7D', linear_fit=True, fit_color='#324F7D',
        xlabel='Subcortico-cortical degree centrality', ylabel='Subcortical volume (z-score)',
        xlim=(90, 375), ylim=(-3.5, 0), corr_value=sc_sctx_r, p_value=sc_sctx_p, p_type='shuf')