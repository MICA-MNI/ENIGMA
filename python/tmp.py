from enigmatoolbox.datasets import load_sc, load_fc
from nilearn import plotting
import numpy as np
import os
import enigmatoolbox.datasets
from enigmatoolbox.datasets import load_fsa5
from enigmatoolbox.plotting import plot_hemispheres
from enigmatoolbox.utils.parcellation import map_to_labels

c, cl, s, sl = load_fc()
c_plot = plotting.plot_matrix(c, figure=(8,8), labels=cl, vmax=0.8, vmin=-0.8)

seed = "L_middletemporal"
seed_conn = c[[i for i, item in enumerate(cl) if seed in item]]

# Load cortical surface
surf_lh, surf_rh = load_fsa5()

# Load mapping between parcellation (Desikan-Killiany) and surface (fsa5)
labeling = np.loadtxt(os.path.join(os.path.dirname(enigmatoolbox.datasets.__file__),
                      'parcellations', 'aparc_fsa5.csv'), dtype=np.int)

# Map parcellation values to surface (vertices)
a_idx = list(range(1, 4)) + list(range(5, 39)) + list(range(40, 71)) # indices of parcels included in ENIGMA
seed_conn_DK = np.zeros(71)                                               # vector of zeros to be filled with cortical values
seed_conn_DK[a_idx] = seed_conn

data_fsa5 = map_to_labels(seed_conn_DK, labeling)

plot_hemispheres(surf_lh, surf_rh, array_name=data_fsa5, size=(800, 400),
                 cmap='viridis', color_bar=True, color_range=(0.2, .6))

# _, _, x = f() to ignore multiple returns

plotting.plot_matrix


sc, scl, _, _ = load_fc()
sc_plot = plotting.plot_matrix(sc, figure=(9, 9), labels=scl, vmax=0.8, vmin=0, cmap='Reds')