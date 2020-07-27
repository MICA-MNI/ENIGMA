from enigmatoolbox.datasets import load_sc, load_fc
from nilearn import plotting

# Let's use load_sc() and load_fc() functions to return:
# 14 x 68 ndarray (fc/sc: subcortico-cortical connectivity matrix)
# 14 x 1 ndarray (fcl/scl: name of subcortical areas)

# Load and plot functional connectivity data
_, _, fc, fcl = load_fc()
fc_plot = plotting.plot_matrix(fc, figure=(9, 9), labels=fcl, vmax=0.5, vmin=0, cmap='Reds')

# Load and plot structural connectivity data
_, _, sc, scl = load_sc()
sc_plot = plotting.plot_matrix(sc, figure=(9, 9), labels=scl, vmax=10, vmin=0, cmap='Blues')

# As above, we can also extract seed-based connectivity! Here, we chose the left hippocampus as example seed:
seed = "Lhippo"
seed_conn_fc = fc[[i for i, item in enumerate(fcl) if seed in item],]   # extract FC row corresponding to the seed
seed_conn_sc = sc[[i for i, item in enumerate(scl) if seed in item],]   # extract SC row corresponding to the seed