import numpy as np
from enigmatoolbox.datasets import load_example_data
from enigmatoolbox.utils.useful import zscore_matrix, reorder_sctx
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
# Load functional and structural cortico-cortical connectivity data (for simplicity, we won't load the regions' labels)
fc_ctx, _, fc_sctx, _ = load_fc()
sc_ctx, _, sc_sctx, _ = load_sc()


"""
4 - Functional/structural cortical disease epicenters
"""
# Correlations between seed-based connectivity (looping over all cortical regions) and
# cortical thickness decreases in left TLE