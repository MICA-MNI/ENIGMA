from enigmatoolbox.datasets import load_summary_stats

# Load summary statistics for ENIGMA-Epilepsy
sum_stats = load_summary_stats('epilepsy')

# Get case-control subcortical volume and cortical thickness tables
SV = sum_stats['SubVol_case_vs_controls_ltle']
CT = sum_stats['CortThick_case_vs_controls_ltle']

# Extract Cohen's d values
SV_d = SV['d_icv']
CT_d = CT['d_icv']


from enigmatoolbox.datasets import load_sc, load_fc
# Load and plot cortical functional connectivity data
fc_ctx, fc_ctx_labels, _, _ = load_fc()

# Load and plot cortical structural connectivity data
sc_ctx, sc_ctx_labels, _, _ = load_sc()


from enigmatoolbox.datasets import load_sc, load_fc
# Load and plot subcortical functional connectivity data
_, _, fc_sctx, fc_sctx_labels = load_fc()

# Load and plot subcortical structural connectivity data
_, _, sc_sctx, sc_sctx_labels = load_sc()


import numpy as np
# Compute weighted degree centrality measures from the connectivity data
fc_ctx_dc = np.sum(fc_ctx, axis=0)
sc_ctx_dc = np.sum(sc_ctx, axis=0)


import numpy as np
# Compute weighted degree centrality measures from the connectivity data
fc_sctx_dc = np.sum(fc_sctx, axis=1)
sc_sctx_dc = np.sum(sc_sctx, axis=1)


import numpy as np
# Remove subcortical values corresponding the ventricles
# (as we don't have connectivity values for them!)
SV_d_noVent = SV_d.drop([np.where(SV['Structure'] == 'LLatVent')[0][0],
                        np.where(SV['Structure'] == 'RLatVent')[0][0]])
SV_d_noVent = SV_d_noVent.reset_index(drop=True)

# Perform spatial correlations between cortical hubs and Cohen's d
fc_ctx_r = np.corrcoef(fc_ctx_dc, CT_d)[0, 1]
sc_ctx_r = np.corrcoef(sc_ctx_dc, CT_d)[0, 1]

# Perform spatial correlations between subcortical hubs and Cohen's d
fc_sctx_r = np.corrcoef(fc_sctx_dc, SV_d_noVent)[0, 1]
sc_sctx_r = np.corrcoef(sc_sctx_dc, SV_d_noVent)[0, 1]

# Store correlation coefficients
rvals = {'functional cortical hubs': fc_ctx_r, 'functional subcortical hubs': fc_sctx_r,
         'structural cortical hubs': sc_ctx_r, 'structural subcortical hubs': sc_sctx_r}


from enigmatoolbox.permutation_testing import spin_test, shuf_test

# Remove subcortical values corresponding the ventricles
# (as we don't have connectivity values for them!)
SV_d_noVent = SV_d.drop([np.where(SV['Structure'] == 'LLatVent')[0][0],
                        np.where(SV['Structure'] == 'RLatVent')[0][0]])
SV_d_noVent = SV_d_noVent.reset_index(drop=True)

# Spin permutation testing for two cortical maps
fc_ctx_p, fc_ctx_d = spin_test(fc_ctx_dc, CT_d, surface_name='fsa5', parcellation_name='aparc',
                               type='pearson', n_rot=1000, spin_dist=True)
sc_ctx_p, sc_ctx_d = spin_test(sc_ctx_dc, CT_d, surface_name='fsa5', parcellation_name='aparc',
                               type='pearson', n_rot=1000, spin_dist=True)

# Shuf permutation testing for two subcortical maps
fc_sctx_p, fc_sctx_d = shuf_test(fc_sctx_dc, SV_d_noVent, n_rot=1000,
                                 type='pearson', spin_dist=True)
sc_sctx_p, sc_sctx_d = shuf_test(sc_sctx_dc, SV_d_noVent, n_rot=1000,
                                 type='pearson', spin_dist=True)

# Store p-values and null distributions
p_and_d = {'functional cortical hubs': [fc_ctx_p, fc_ctx_d], 'functional subcortical hubs': [fc_sctx_p, fc_sctx_d],
          'structural cortical hubs': [sc_ctx_p, sc_ctx_d], 'structural subcortical hubs': [sc_sctx_p, sc_sctx_d]}


import matplotlib.pyplot as plt

fig, axs = plt.subplots(1, 4, figsize=(15, 3))

for k, (fn, dd) in enumerate(p_and_d.items()):
    # Define plot colors
    if k <= 1:
        col = '#A8221C'     # red for functional hubs
    else:
        col = '#324F7D'     # blue for structural hubs

    # Plot null distributions
    axs[k].hist(dd[1], bins=50, density=True, color=col, edgecolor='white', lw=0.5)
    axs[k].axvline(rvals[fn], lw=1.5, ls='--', color='k', dashes=(2, 3),
                   label='$r$={:.2f}'.format(rvals[fn]) + '\n$p$={:.2f}'.format(dd[0]))
    axs[k].set_xlabel('Null correlations \n ({})'.format(fn))
    axs[k].set_ylabel('Density')
    axs[k].spines['top'].set_visible(False)
    axs[k].spines['right'].set_visible(False)
    axs[k].legend(loc=1, frameon=False)

fig.tight_layout()
plt.show()


import matplotlib.pyplot as plt
import numpy as np

# Store degree centrality and atrophy measures
meas = {('functional cortical hubs', 'cortical thickness'): [fc_ctx_dc, CT_d],
        ('functional subcortical hubs', 'subcortical volume'): [fc_sctx_dc, SV_d_noVent],
        ('structural cortical hubs', 'cortical thickness'): [sc_ctx_dc, CT_d],
        ('structural subcortical hubs', 'subcortical volume'): [sc_sctx_dc, SV_d_noVent]}

fig, axs = plt.subplots(1, 4, figsize=(15, 3))

for k, (fn, dd) in enumerate(meas.items()):
    # Define scatter colors
    if k <= 1:
        col = '#A8221C'
    else:
        col = '#324F7D'

    # Plot relationship between hubs and atrophy
    axs[k].scatter(dd[0], dd[1], color=col,
                   label='$r$={:.2f}'.format(rvals[fn[0]]) + '\n$p$={:.2f}'.format(p_and_d[fn[0]][0]))
    m, b = np.polyfit(dd[0], dd[1], 1)
    axs[k].plot(dd[0], m * dd[0] + b, color=col)
    axs[k].set_ylim((-1, 0.5))
    axs[k].set_xlabel('{}'.format(fn[0].capitalize()))
    axs[k].set_ylabel('{}'.format(fn[1].capitalize()))
    axs[k].spines['top'].set_visible(False)
    axs[k].spines['right'].set_visible(False)
    axs[k].legend(loc=1, frameon=False)

fig.tight_layout()
plt.show()



import numpy as np
from enigmatoolbox.permutation_testing import spin_test
from enigmatoolbox.utils.parcellation import parcel_to_surface
from enigmatoolbox.plotting import plot_cortical

# Identify cortical epicenters (from functional connectivity)
fc_ctx_epi = []
fc_ctx_epi_p = []
for seed in range(fc_ctx.shape[0]):
    seed_con = fc_ctx[:, seed]
    fc_ctx_epi = np.append(fc_ctx_epi, np.corrcoef(seed_con, CT_d)[0, 1])
    fc_ctx_epi_p = np.append(fc_ctx_epi_p,
                             spin_test(seed_con, CT_d, surface_name='fsa5', parcellation_name='aparc',
                                       type='pearson', n_rot=1000))

# Identify cortical epicenters (from structural connectivity)
sc_ctx_epi = []
sc_ctx_epi_p = []
for seed in range(sc_ctx.shape[0]):
    seed_con = sc_ctx[:, seed]
    sc_ctx_epi = np.append(sc_ctx_epi, np.corrcoef(seed_con, CT_d)[0, 1])
    sc_ctx_epi_p = np.append(sc_ctx_epi_p,
                             spin_test(seed_con, CT_d, surface_name='fsa5', parcellation_name='aparc',
                                       type='pearson', n_rot=1000))

# And project the results on the surface brain
fc_ctx_epi_p_sig = np.zeros_like(fc_ctx_epi_p)
fc_ctx_epi_p_sig[np.argwhere(fc_ctx_epi_p < 0.1)] = fc_ctx_epi[np.argwhere(fc_ctx_epi_p < 0.1)]

plot_cortical(array_name=parcel_to_surface(fc_ctx_epi_p_sig, 'aparc_fsa5'), surface_name="fsa5", size=(800, 400),
              cmap='GyRd_r', color_bar=True, color_range=(-0.5, 0.5))

plot_cortical(array_name=parcel_to_surface(sc_ctx_epi, 'aparc_fsa5'), surface_name="fsa5", size=(800, 400),
              cmap='GyBu_r', color_bar=True, color_range=(-0.5, 0.5))

plot_cortical(array_name=parcel_to_surface(fc_ctx_epi_p_sig, 'aparc_fsa5'), surface_name="fsa5", size=(200, 200),
              cmap='GyRd_r', color_bar=True, color_range=(-0.5, 0.5), screenshot=True, filename='/Users/saratheriver/Desktop/epi_fc_ctx2.png')

import numpy as np
from enigmatoolbox.permutation_testing import spin_test
from enigmatoolbox.plotting import plot_subcortical

# Identify subcortical epicenters (from functional connectivity)
fc_sctx_epi = []
fc_sctx_epi_p = []
for seed in range(fc_sctx.shape[0]):
    seed_con = fc_sctx[seed, :]
    fc_sctx_epi = np.append(fc_sctx_epi, np.corrcoef(seed_con, CT_d)[0, 1])
    fc_sctx_epi_p = np.append(fc_sctx_epi_p,
                              spin_test(seed_con, CT_d, surface_name='fsa5', n_rot=100))

# Identify subcortical epicenters (from structural connectivity)
sc_sctx_epi = []
sc_sctx_epi_p = []
for seed in range(sc_sctx.shape[0]):
    seed_con = sc_sctx[seed, :]
    sc_sctx_epi = np.append(sc_sctx_epi, np.corrcoef(seed_con, CT_d)[0, 1])
    sc_sctx_epi_p = np.append(sc_sctx_epi_p,
                              spin_test(seed_con, CT_d, surface_name='fsa5', n_rot=100))

# And project the results on the surface brain
plot_subcortical(fc_sctx_epi, ventricles=False, size=(800, 400),
                 cmap='Reds_r', color_bar=True, color_range=(-0.5, -0.2))

plot_subcortical(sc_sctx_epi, ventricles=False, size=(800, 400),
                 cmap='Blues_r', color_bar=True, color_range=(-0.5, 0))


from enigmatoolbox.datasets import fetch_ahba

# Fetch gene expression data (output of fetch_ahba() is a dataframe)
genes = fetch_ahba()

# Obtain region labels
reglabels = genes['label']

# Obtain gene labels
genelabels = list(genes.columns)[1]


from enigmatoolbox.datasets import risk_genes

# Get the names of genes associated with a specific epilepsy subtype (e.g., Focal HS)
epilepsy_genes = risk_genes('epilepsy')['focalhs']

# Extract gene expression data for these Focal HS genes
epilepsy_gene_data = genes[genes.columns.intersection(epilepsy_genes)]


import numpy as np
from enigmatoolbox.utils.parcellation import parcel_to_surface
from enigmatoolbox.plotting import plot_cortical, plot_subcortical

# Compute the mean co-expression across all Focal HS genes
mean_epilepsy_genes = np.mean(epilepsy_gene_data, axis=1)

# Separate cortical (ctx) from subcortical (sctx) regions
mean_epilepsy_genes_ctx = mean_epilepsy_genes[:68]
mean_epilepsy_genes_sctx = mean_epilepsy_genes[68:]

# Map the parcellated gene expression data to our surface template (ctx only)
mean_epilepsy_genes_ctx_fsa5 = parcel_to_surface(mean_epilepsy_genes_ctx, 'aparc_fsa5')

# Project the results on the surface brain
plot_cortical(array_name=mean_epilepsy_genes_ctx_fsa5, surface_name="fsa5", size=(800, 400), nan_color=(1, 1, 1, 1),
              cmap='Greys', color_bar=True, color_range=(0.4, 0.55))

plot_subcortical(array_name=mean_epilepsy_genes_sctx, ventricles=False, size=(800, 400),
                cmap='Greys', color_bar=True, color_range=(0.4, 0.65))


from enigmatoolbox.utils.parcellation import parcel_to_surface
from enigmatoolbox.plotting import plot_cortical

# Map parcellated data to the surface (cortical values only)
CT_d_fsa5 = parcel_to_surface(CT_d, 'aparc_fsa5')

# Project Cohen's d values to the surface template
plot_cortical(array_name=CT_d_fsa5, surface_name="fsa5", size=(800, 400),
              cmap='RdBu_r', color_bar=True, color_range=(-0.5, 0.5))



from enigmatoolbox.plotting import plot_subcortical

# Project Cohen's d values to the surface template
plot_subcortical(array_name=SV_d, size=(800, 400),
                 cmap='RdBu_r', color_bar=True, color_range=(-0.5, 0.5))