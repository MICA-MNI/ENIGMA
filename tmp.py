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
from nilearn import plotting

# Load cortico-cortical functional connectivity data
fc_ctx, fc_ctx_labels, _, _ = load_fc()

# Load cortico-cortical structural connectivity data
sc_ctx, sc_ctx_labels, _, _ = load_sc()

from enigmatoolbox.datasets import load_sc, load_fc
from nilearn import plotting

# Load subcortico-cortical functional connectivity data
_, _, fc_sctx, fc_sctx_labels = load_fc()

# Load subcortico-cortical structural connectivity data
_, _, sc_sctx, sc_sctx_labels = load_sc()

import numpy as np
from enigmatoolbox.plotting import plot_cortical
from enigmatoolbox.utils.parcellation import parcel_to_surface

# Compute weighted degree centrality measures from the connectivity data
fc_ctx_dc = np.sum(fc_ctx, axis=0)
sc_ctx_dc = np.sum(sc_ctx, axis=0)

import numpy as np
from enigmatoolbox.plotting import plot_subcortical

# Compute weighted degree centrality measures from the connectivity data
fc_sctx_dc = np.sum(fc_sctx, axis=1)
sc_sctx_dc = np.sum(sc_sctx, axis=1)

import numpy as np

# Remove subcortical values corresponding to the ventricles
# (as we don't have connectivity values for them!)
SV_d_noVent = SV_d.drop([np.where(SV['Structure'] == 'LLatVent')[0][0],
                        np.where(SV['Structure'] == 'RLatVent')[0][0]]).reset_index(drop=True)

# Perform spatial correlations between functional hubs and Cohen's d
fc_ctx_r = np.corrcoef(fc_ctx_dc, CT_d)[0, 1]
fc_sctx_r = np.corrcoef(fc_sctx_dc, SV_d_noVent)[0, 1]

# Perform spatial correlations between structural hubs and Cohen's d
sc_ctx_r = np.corrcoef(sc_ctx_dc, CT_d)[0, 1]
sc_sctx_r = np.corrcoef(sc_sctx_dc, SV_d_noVent)[0, 1]

# Store correlation coefficients
rvals = {'functional cortical hubs': fc_ctx_r, 'functional subcortical hubs': fc_sctx_r,
         'structural cortical hubs': sc_ctx_r, 'structural subcortical hubs': sc_sctx_r}


from enigmatoolbox.permutation_testing import spin_test, shuf_test

# Remove subcortical values corresponding to the ventricles
# (as we don't have connectivity values for them!)
SV_d_noVent = SV_d.drop([np.where(SV['Structure'] == 'LLatVent')[0][0],
                        np.where(SV['Structure'] == 'RLatVent')[0][0]]).reset_index(drop=True)

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
                   label='$r$={:.2f}'.format(rvals[fn]) + '\n$p$={:.3f}'.format(dd[0]))
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

    # Plot relationships between hubs and atrophy
    axs[k].scatter(meas[fn][0], meas[fn][1], color=col,
                   label='$r$={:.2f}'.format(rvals[fn[0]]) + '\n$p$={:.3f}'.format(p_and_d[fn[0]][0]))
    m, b = np.polyfit(meas[fn][0], meas[fn][1], 1)
    axs[k].plot(meas[fn][0], m * meas[fn][0] + b, color=col)
    axs[k].set_ylim((-1, 0.5))
    axs[k].set_xlabel('{}'.format(fn[0].capitalize()))
    axs[k].set_ylabel('{}'.format(fn[1].capitalize()))
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

    # Plot relationships between hubs and atrophy
    axs[k].scatter(meas[fn][0], meas[fn][1], color=col,
                   label='$r$={:.2f}'.format(rvals[fn[0]]) + '\n$p$={:.3f}'.format(p_and_d[fn[0]][0]))
    m, b = np.polyfit(meas[fn][0], meas[fn][1], 1)
    axs[k].plot(meas[fn][0], m * meas[fn][0] + b, color=col)
    axs[k].set_ylim((-1, 0.5))
    axs[k].set_xlabel('{}'.format(fn[0].capitalize()))
    axs[k].set_ylabel('{}'.format(fn[1].capitalize()))
    axs[k].spines['top'].set_visible(False)
    axs[k].spines['right'].set_visible(False)
    axs[k].legend(loc=1, frameon=False)

fig.tight_layout()
plt.show()