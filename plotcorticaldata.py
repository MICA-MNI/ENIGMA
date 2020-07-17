import os
import numpy as np
import brainspace.datasets
from brainspace.datasets import load_fsa5
from brainspace.plotting import plot_hemispheres
from brainspace.utils.parcellation import map_to_labels

# Original data parcellated using Desikan-Killiany
# Because ENIGMA does not provide values for the brain mask and the corpus callosum
# we will give them a value of zeros
a_idx = list(range(1, 4)) + list(range(5, 39)) + list(range(40, 71))     # indices of parcels included in ENIGMA
data_DK = np.zeros(71)
data_DK[a_idx] = list(range(1, 69))

# Load cortical surface
surf_lh, surf_rh = load_fsa5()

# Load mapping between parcellation (Desikan-Killiany) and surface (fsa5)
fname = 'aparc_fsa5.csv'
labeling = np.loadtxt(os.path.join(os.path.dirname(brainspace.datasets.__file__),
                                   'parcellations', fname), dtype=np.int)

# Map parcellation values to surface (vertices)
data_fsa5 = map_to_labels(data_DK, labeling)

plot_hemispheres(surf_lh, surf_rh, array_name=data_fsa5, size=(800, 400),
                         cmap='viridis', color_bar=True, color_range=(0, 68))