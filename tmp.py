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
SV_z = zscore_matrix(metr1_SubVol_r.iloc[:, 1:-1], group, controlCode)
CT_z = zscore_matrix(metr2_CortThick.iloc[:, 1:-5], group, controlCode)
SA_z = zscore_matrix(metr3_CortSurf.iloc[:, 1:-5], group, controlCode)

# Mean z-score values across individuals with from a specific group (e.g., left TLE, that is SDx == 3)
SV_z_mean = SV_z.iloc[cov[cov['SDx'] == 3].index, :].mean(axis=0)
CT_z_mean = CT_z.iloc[cov[cov['SDx'] == 3].index, :].mean(axis=0)
SA_z_mean = SA_z.iloc[cov[cov['SDx'] == 3].index, :].mean(axis=0)