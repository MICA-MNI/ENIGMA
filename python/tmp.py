import os
import numpy as np
import enigmatoolbox.datasets
from enigmatoolbox.datasets import load_fsa5
from enigmatoolbox.plotting import plot_hemispheres
from enigmatoolbox.datasets import load_sc, load_fc


# Load functional and structural cortico-cortical connectivity data
fc, _, _, _ = load_fc()
sc, _, _, _ = load_sc()

# Compute weighted degree centrality measures from the connectivity data
dc_f = np.sum(fc, axis=0)
dc_s = np.sum(sc, axis=0)

# Map parcellated data to the surface
fname = 'aparc_fsa5.csv'
labeling = np.loadtxt(os.path.join(os.path.dirname(enigmatoolbox.datasets.__file__),
          'parcellations', fname), dtype=np.int)
dc_f_fsa5 = map_to_labels(dc_f, labeling)
dc_s_fsa5 = map_to_labels(dc_s, labeling)

# And project the results on the surface brain
surf_lh, surf_rh = load_fsa5()
plot_hemispheres(surf_lh, surf_rh, array_name=dc_f_fsa5, size=(800, 400),
                 cmap='Reds', color_bar=True, color_range=(20, 30))

plot_hemispheres(surf_lh, surf_rh, array_name=dc_s_fsa5, size=(800, 400),
                 cmap='Blues', color_bar=True, color_range=(100, 300))