from enigmatoolbox.datasets import fetch_ahba
from enigmatoolbox.datasets import epilepsy_genes

# Let's start by loading the microarray expression data
gx = fetch_ahba()

# Get the names of genes associated with specific epilepsy subtypes (using Focal HS as example here)
# Other subtypes include: 'allepilepsy', 'focalepilepsy', 'generalizedepilepsy', 'jme', 'cae'
epigx = epilepsy_genes()
fh_genes = epigx['focalhs']

# We can now extract the gene expression data for these specifc genes
fh_gx = gx[fh_genes]

# Alternatively, we can also combine all dem epilepsy genes together (and removing duplicates)
allg = epigx['allepilepsy'] + epigx['focalepilepsy'] + epigx['generalizedepilepsy'] + epigx['jme'] + epigx['cae'] + epigx['focalhs']
allg = list(dict.fromkeys(allg))
allgx = gx[allg]




import os
import numpy as np
import enigmatoolbox.datasets
from enigmatoolbox.utils.parcellation import map_to_labels
from enigmatoolbox.plotting import plot_cortical, plot_subcortical

# Following the above code, we can then map epilepsy-related gene expression to the surface!
labeling = np.loadtxt(os.path.join(os.path.dirname(enigmatoolbox.datasets.__file__),
          'parcellations', 'aparc_fsa5.csv'), dtype=np.int)
fh_gx_fsa5 = map_to_labels(np.mean(fh_gx, axis=1)[:68], labeling)
plot_cortical(array_name=fh_gx_fsa5, surface_name="fsa5", size=(800, 400), nan_color=(1, 1, 1, 1),
              cmap='Greys', color_bar=True, color_range=(0.4, 0.55))

plot_subcortical(array_name=np.mean(fh_gx, axis=1)[68:], ventricles=False, size=(800, 400),
                 cmap='Greys', color_bar=True, color_range=(0.4, 0.65))