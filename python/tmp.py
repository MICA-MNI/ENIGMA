import numpy as np
from enigmatoolbox.plotting import plot_subcortical
from enigmatoolbox.datasets import load_sc, load_fc

# Load functional and structural subcortico-cortical connectivity data
_, _, fc, _ = load_fc()
_, _, sc, _ = load_sc()

# Compute weighted degree centrality measures from the connectivity data
dc_f = np.sum(fc, axis=1)
dc_s = np.sum(sc, axis=1)

# And project the results on the subcortical surfaces (don't forget to set the ventricles flag to False!)
plot_subcortical(array_name=dc_f, ventricles=False, size=(800, 400),
                 cmap='Reds', color_bar=True, color_range=(5, 10))

plot_subcortical(array_name=dc_s, ventricles=False, size=(800, 400),
                 cmap='Blues', color_bar=True, color_range=(100, 300))