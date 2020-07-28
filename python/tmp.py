import os
import numpy as np
import enigmatoolbox.datasets
from enigmatoolbox.datasets import load_fsa5
from enigmatoolbox.plotting import plot_hemispheres

# Load mapping between parcellation (e.g., Desikan-Killiany) and surface (fsa5)
fname = 'aparc_fsa5.csv'
labeling = np.loadtxt(os.path.join(os.path.dirname(enigmatoolbox.datasets.__file__),
                      'parcellations', 'aparc_fsa5.csv'), dtype=np.int)

# Map parcellation values to surface (vertices)
# The function below will work with ENIGMA-parcellated data (e.g., Desikan-Killiany atlas
# without values for the brain mask and the corpus callosum [68 x 1 ndarray])
data_fsa5 = map_to_labels(np.arange(68), labeling)

# Load cortical surface and map values to the surface brain
surf_lh, surf_rh = load_fsa5()
plot_hemispheres(surf_lh, surf_rh, array_name=data_fsa5, size=(800, 400),
                 cmap='viridis', color_bar=True, color_range=(np.min(data_fsa5), np.max(data_fsa5)))