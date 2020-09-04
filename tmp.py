import numpy as np
from enigmatoolbox.datasets import load_example_data
from enigmatoolbox.utils.useful import zscore_matrix
from enigmatoolbox.plotting import plot_subcortical
from enigmatoolbox.datasets import load_sc, load_fc

"""
1 - Let's start by loading our example data
"""
# Here we need the covariates and cortical thickness data
cov, _, metr2_CortThick, _ = load_example_data()


"""
2 - We can then and z-score data in patients relative to controls, so that lower values
    correspond to greater atrophy
"""
# Z-score patients' data relative to controls (lower z-score = more atrophy)
group = cov['Dx'].to_list()
controlCode = 0
ct = zscore_matrix(metr2_CortThick.iloc[:, 1:-5], group, controlCode)

# Mean z-score values across individuals with left TLE (SDx == 3)
ct_tle = np.mean(ct.to_numpy()[cov[cov['SDx'] == 3].index, :], axis=0)


"""
3 - Let's then load our functional and structural connectivity matrices
"""
# Load functional and structural subcortico-cortical connectivity data (for simplicity, we won't load the regions' labels)
_, _, fc_sctx, _ = load_fc()
_, _, sc_sctx, _ = load_sc()


"""
4 - Functional/structural cortical disease epicenters
    Correlations between seed-based connectivity (looping over all subcortical regions) and
    cortical thickness decreases in left TLE
"""
# Functional subcortical epicenters
fc_sctx_epi = []
for seed in range(fc_sctx.shape[0]):
    seed_con = fc_sctx[seed, :]
    fc_sctx_epi = np.append(fc_sctx_epi, np.corrcoef(seed_con, ct_tle)[0, 1])

# Structural subcortical epicenters
sc_sctx_epi = []
for seed in range(sc_sctx.shape[0]):
    seed_con = sc_sctx[seed, :]
    sc_sctx_epi = np.append(sc_sctx_epi, np.corrcoef(seed_con, ct_tle)[0, 1])


"""
5 - Project our findings onto cortical surfaces
"""
# Functional cortical epicenters
plot_subcortical(fc_sctx_epi, ventricles=False, size=(800, 400),
                 cmap='Reds_r', color_bar=True, color_range=(-0.5, 0))

# Structural cortical epicenters
plot_subcortical(sc_sctx_epi, ventricles=False, size=(800, 400),
                 cmap='Blues_r', color_bar=True, color_range=(-0.5, 0))