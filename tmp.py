from enigmatoolbox.datasets import load_example_data

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