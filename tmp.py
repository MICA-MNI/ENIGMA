from enigmatoolbox.datasets import load_sc, load_fc
from nilearn import plotting

# Load cortico-cortical functional connectivity data
fc_ctx, fc_ctx_labels, _, _ = load_fc()

# Load cortico-cortical structural connectivity data
sc_ctx, sc_ctx_labels, _, _ = load_sc()

# Plot cortico-cortical connectivity matrices
fc_plot = plotting.plot_matrix(fc_ctx, figure=(11, 10.5), labels=fc_ctx_labels, vmax=0.8, vmin=0, cmap='Reds')

sc_plot = plotting.plot_matrix(sc_ctx, figure=(11, 10.5), labels=sc_ctx_labels, vmax=10, vmin=0, cmap='Blues')


from enigmatoolbox.utils.parcellation import parcel_to_surface
from enigmatoolbox.plotting import plot_cortical

# Extract seed-based connectivity
seed = "L_middletemporal"
seed_conn_fc = fc_ctx[[i for i, item in enumerate(fc_ctx_labels) if seed in item], ]
seed_conn_sc = sc_ctx[[i for i, item in enumerate(sc_ctx_labels) if seed in item], ]

# Map parcellated data to the surface
seed_conn_fc_fsa5 = parcel_to_surface(seed_conn_fc, 'aparc_fsa5')
seed_conn_sc_fsa5 = parcel_to_surface(seed_conn_sc, 'aparc_fsa5')

# Project the results on the surface brain
plot_cortical(array_name=seed_conn_fc_fsa5, surface_name="fsa5", size=(800, 400),
              cmap='Reds', color_bar=True, color_range=(0.2, 0.7))

plot_cortical(array_name=seed_conn_sc_fsa5, surface_name="fsa5", size=(800, 400),
              cmap='Blues', color_bar=True, color_range=(2, 10))



from enigmatoolbox.datasets import load_sc, load_fc

# Load subcortico-cortical functional connectivity data
_, _, fc_sctx, fc_sctx_labels = load_fc()

# Load subcortico-cortical structural connectivity data
_, _, sc_sctx, sc_sctx_labels = load_sc()


from enigmatoolbox.plotting import plot_cortical

# Extract seed-based connectivity
seed = "Lhippo"
seed_conn_fc = fc_sctx[[i for i, item in enumerate(fc_sctx_labels) if seed in item],]
seed_conn_sc = sc_sctx[[i for i, item in enumerate(sc_sctx_labels) if seed in item],]

# Map parcellated data to the surface
seed_conn_fc_fsa5 = parcel_to_surface(seed_conn_fc, 'aparc_fsa5')
seed_conn_sc_fsa5 = parcel_to_surface(seed_conn_sc, 'aparc_fsa5')

# Project the results on the surface brain
plot_cortical(array_name=seed_conn_fc_fsa5, surface_name="fsa5", size=(800, 400),
              cmap='Reds', color_bar=True, color_range=(0.1, 0.3))

plot_cortical(array_name=seed_conn_sc_fsa5, surface_name="fsa5", size=(800, 400),
              cmap='Blues', color_bar=True, color_range=(1, 10))