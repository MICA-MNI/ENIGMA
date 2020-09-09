import numpy as np

# Remove subcortical values corresponding to the ventricles
SubVol_Z_LTLE_r = SubVol_Z_LTLE_r.drop(columns=['LLatVent', 'RLatVent'])

# Compute weighted degree centrality measures
fc_ctx_dc = np.sum(fc_ctx, axis=0)
fc_sctx_dc = np.sum(fc_sctx, axis=1)

sc_ctx_dc = np.sum(sc_ctx, axis=0)
sc_sctx_dc = np.sum(sc_sctx, axis=1)

# Perform spatial correlations between hubs and mean atrophy
fc_ctx_r = np.corrcoef(fc_ctx_dc, np.mean(CortThick_Z_LTLE, axis=0))[0, 1]
fc_sctx_r = np.corrcoef(fc_sctx_dc, np.mean(SubVol_Z_LTLE_r, axis=0))[0, 1]

sc_ctx_r = np.corrcoef(sc_ctx_dc, np.mean(CortThick_Z_LTLE, axis=0))[0, 1]
sc_sctx_r = np.corrcoef(sc_sctx_dc, np.mean(SubVol_Z_LTLE_r, axis=0))[0, 1]