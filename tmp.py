from enigmatoolbox.datasets import load_example_data

# Load all example data from an individual site
cov, metr1_SubVol, metr2_CortThick, metr3_CortSurf = load_example_data()


from enigmatoolbox.utils.useful import reorder_sctx

# Re-order the subcortical data alphabetically and by hemisphere
metr1_SubVol_r = reorder_sctx(metr1_SubVol)

from enigmatoolbox.utils.useful import zscore_matrix

# Z-score patients' data relative to controls (lower z-score = more atrophy)
group = cov['Dx'].to_list()
controlCode = 0
sv = zscore_matrix(metr1_SubVol_r.iloc[:, 1:-1], group, controlCode)
ct = zscore_matrix(metr2_CortThick.iloc[:, 1:-5], group, controlCode)
sa = zscore_matrix(metr3_CortSurf.iloc[:, 1:-5], group, controlCode)

# Mean z-score values across individuals with from a specific group (e.g., left TLE, that is SDx == 3)
sv_tle = sv.iloc[cov[cov['SDx'] == 3].index, :].mean(axis=0)
ct_tle = ct.iloc[cov[cov['SDx'] == 3].index, :].mean(axis=0)
sa_tle = sa.iloc[cov[cov['SDx'] == 3].index, :].mean(axis=0)

from enigmatoolbox.datasets import load_sc, load_fc
from nilearn import plotting

# Load and plot functional connectivity data
fc, fcl, _, _ = load_fc()

# Load and plot structural connectivity data
sc, scl, _, _ = load_sc()

import numpy as np
from enigmatoolbox.plotting import plot_cortical
from enigmatoolbox.utils.parcellation import parcel_to_surface

# Compute weighted degree centrality measures from the connectivity data
dc_f = np.sum(fc, axis=0)
dc_s = np.sum(sc, axis=0)

# Map parcellated data to the surface
dc_f_fsa5 = parcel_to_surface(dc_f, 'aparc_fsa5')
dc_s_fsa5 = parcel_to_surface(dc_s, 'aparc_fsa5')

from enigmatoolbox.permutation_testing import spin_test, shuf_test

# Spin permutation testing for two cortical maps
fc_ctx_p, fc_ctx_d = spin_test(dc_f, ct_tle.to_numpy(), surface_name='fsa5', parcellation_name='aparc',
                               n_rot=1000, type='pearson', spin_dist=True)
sc_ctx_p, sc_ctx_d = spin_test(dc_s, ct_tle.to_numpy(), surface_name='fsa5', parcellation_name='aparc',
                               n_rot=100, type='pearson', spin_dist=True)
