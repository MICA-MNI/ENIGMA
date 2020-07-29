import os
import numpy as np
import enigmatoolbox.datasets
from enigmatoolbox.plotting import plot_co
from enigmatoolbox.utils.parcellation import map_to_labels

# Load functional and structural subcortico-cortical connectivity data
_, _, fc, _ = load_fc()
_, _, sc, _ = load_sc()

# Compute weighted degree centrality measures from the connectivity data
dc_f = np.sum(fc, axis=1)
dc_s = np.sum(sc, axis=0)

#
dc_f_sctx = subcorticalvertices(subcortical_values=np.array(range(16)))

# And project the results on the subcortical surfaces
surf_lh, surf_rh = load_subcortical()
plot_hemispheres(surf_lh, surf_rh, array_name=dc_f_sctx, size=(800, 400),
                 cmap='Reds', color_bar=True, color_range=(1, 10))

plot_hemispheres(surf_lh, surf_rh, array_name=dc_s, size=(800, 400),
                 cmap='Blues', color_bar=True, color_range=(100, 300))








fname = 'aparc_fsa5.csv'
labeling = np.loadtxt(os.path.join(os.path.dirname(enigmatoolbox.datasets.__file__),
          'parcellations', fname), dtype=np.int)

# Map parcellation values to surface (vertices)
# In addition to several parcellations (Schaefer, Glasser, aparc, etc.), the function below also works with
# ENIGMA-parcellated data (e.g., Desikan-Killiany atlas without values for the brain mask and the corpus
# callosum [68 x 1 ndarray])
data_fsa5 = map_to_labels(np.arange(68), labeling)

plot_cortical(array_name=data_fsa5, size=(800, 400),
                 cmap='Blues', color_bar=True, color_range=(100, 300))