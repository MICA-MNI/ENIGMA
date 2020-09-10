"""
Figure 1. Load example data
"""
from enigmatoolbox.datasets import load_example_data
from enigmatoolbox.utils.useful import zscore_matrix

# Load example data
cov, metr1_SubVol, metr2_CortThick, metr3_CortSurf = load_example_data()

# Z-score data in patients relative to controls
groups = cov['Dx'].to_list()
controlGroup = 0
CortThick_Z = zscore_matrix(metr2_CortThick.iloc[:, 1:-5], groups, controlGroup)
SubVol_Z = zscore_matrix(metr1_SubVol.iloc[:, 1:-1], groups, controlGroup)

# Extract data for a specific group (e.g., individuals with left TLE)
CortThick_Z_LTLE = CortThick_Z.iloc[cov[cov['SDx'] == 3].index, :]
SubVol_Z_LTLE = SubVol_Z.iloc[cov[cov['SDx'] == 3].index, :]


"""
Figure 2. Surface data visualization
"""
from enigmatoolbox.utils.useful import reorder_sctx
import numpy as np
from enigmatoolbox.utils.parcellation import parcel_to_surface
from enigmatoolbox.plotting import plot_cortical, plot_subcortical

# Re-order subcortical data (alphabetically and by hemisphere)
SubVol_Z_LTLE_r = reorder_sctx(SubVol_Z_LTLE)

# Mean data across all individuals with left TLE
CortThick_Z_LTLE_mean = np.mean(CortThick_Z_LTLE, axis=0)
SubVol_Z_LTLE_r_mean = np.mean(SubVol_Z_LTLE_r, axis=0)

# Map parcellated data to the surface (cortical values only)
CortThick_Z_LTLE_mean_fsa5 = parcel_to_surface(CortThick_Z_LTLE_mean, 'aparc_fsa5')

# Project data to the surface templates
plot_cortical(array_name=CortThick_Z_LTLE_mean_fsa5, surface_name="fsa5",
              size=(800, 400), cmap='Blues_r', color_bar=True, color_range=(-2, 0))

plot_subcortical(array_name=SubVol_Z_LTLE_r_mean, size=(800, 400),
                 cmap='Blues_r', color_bar=True, color_range=(-3, 0))