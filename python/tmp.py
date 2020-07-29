import os
import numpy as np
import enigmatoolbox.datasets
from enigmatoolbox.datasets import load_subcortical
from enigmatoolbox.plotting import plot_hemispheres
from enigmatoolbox.datasets import load_sc, load_fc
from enigmatoolbox.utils.parcellation import subcorticalvertices

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