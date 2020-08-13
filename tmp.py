import numpy as np
from enigmatoolbox.datasets import load_example_data
from enigmatoolbox.utils.useful import zscore_matrix, reorder_sctx
from enigmatoolbox.datasets import load_sc, load_fc
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

"""
1 - Let's start by loading our example data and z-score data
    in patients relative to controls
"""
# Let's first load our example data. Here we need the covariates, cortical thickness, and subcortical volume data
cov, metr1_SubVol, metr2_CortThick, _ = load_example_data()

# After loading our subcortical data, we must re-order them (alphabetically and by hemisphere)
# so to match the order from the connectivity matrices and as a pre-requisite for plot_subcortical()
metr1_SubVol_r = reorder_sctx(metr1_SubVol)

# We must also remove subcortical values corresponding the ventricles (as we don't have connectivity values for them!)
metr1_SubVol_r = metr1_SubVol_r.drop(columns=['LLatVent', 'RLatVent'])


"""
2 - Let's then load our functional and structural connectivity matrices
    and compute degree centrality metrics to identify the spatial distribution
    of hubs
"""
# We can z-score the data in patients relative to controls (lower z-score = more atrophy)
group = cov['Dx'].to_list()
controlCode = 0
sv = zscore_matrix(metr1_SubVol_r.iloc[:, 1:-1], group, controlCode)
ct = zscore_matrix(metr2_CortThick.iloc[:, 1:-5], group, controlCode)

# And mean z-score values across individuals with left TLE
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

# Let's check our correlation values
fc_ctx_r
Out: -0.3262858710039119
fc_sctx_r
Out: -0.3694570967953776
sc_ctx_r
Out: -0.10906952508821116
sc_sctx_r
Out: -0.15460373306487168