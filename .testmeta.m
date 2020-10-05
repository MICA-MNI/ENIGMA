% Load summary statistics for ENIGMA-Epilepsy
sum_stats = load_summary_stats('epilepsy');

% Get case-control subcortical volume and cortical thickness tables
SV = sum_stats.SubVol_case_vs_controls_ltle;
CT = sum_stats.CortThick_case_vs_controls_ltle;

% Extract Cohen's d values
SV_d = SV.d_icv;
CT_d = CT.d_icv;

% Load and plot functional connectivity data
[fc_ctx, fc_ctx_labels, ~, ~] = load_fc();

% Load and plot structural connectivity data
[sc_ctx, sc_ctx_labels, ~, ~] = load_sc();

% Load and plot functional connectivity data
[~, ~, fc_sctx, fc_sctx_labels] = load_fc();

% Load and plot structural connectivity data
[~, ~, sc_sctx, sc_sctx_labels] = load_sc();

% Compute weighted degree centrality measures from the connectivity data
fc_ctx_dc           = sum(fc_ctx);
sc_ctx_dc           = sum(sc_ctx);

% Map parcellated data to the surface
fc_ctx_dc_fsa5      = parcel_to_surface(fc_ctx_dc, 'aparc_fsa5');
sc_ctx_dc_fsa5      = parcel_to_surface(sc_ctx_dc, 'aparc_fsa5');

%% Compute weighted degree centrality measures from the connectivity data
fc_sctx_dc          = sum(fc_sctx, 2);
sc_sctx_dc          = sum(sc_sctx, 2);


% Remove subcortical values corresponding the ventricles
% (as we don't have connectivity values for them!)
SV_d_noVent = SV_d;
SV_d_noVent([find(strcmp(SV.Structure, 'LLatVent')); ...
            find(strcmp(SV.Structure, 'RLatVent'))], :) = [];

% Perform spatial correlations between cortical hubs and Cohen's d
fc_ctx_r = corrcoef(fc_ctx_dc, CT_d);
sc_ctx_r = corrcoef(sc_ctx_dc, CT_d);

% Perform spatial correlations between structural hubs and Cohen's d
fc_sctx_r = corrcoef(fc_sctx_dc, SV_d_noVent);
sc_sctx_r = corrcoef(sc_sctx_dc, SV_d_noVent);


% Remove subcortical values corresponding the ventricles
% (as we don't have connectivity values for them!)
SV_d_noVent = SV_d;
SV_d_noVent([find(strcmp(SV.Structure, 'LLatVent')); ...
            find(strcmp(SV.Structure, 'RLatVent'))], :) = [];
        
% Spin permutation testing for two cortical maps
[fc_ctx_p, fc_ctx_d]   = spin_test(fc_ctx_dc, CT_d, 'fsa5', ...
                                   'aparc', 1000, 'pearson');
[sc_ctx_p, sc_ctx_d]   = spin_test(sc_ctx_dc, CT_d, 'fsa5', ...
                                   'aparc', 1000, 'pearson');
                               
% Shuf permutation testing for two subcortical maps 
[fc_sctx_p, fc_sctx_d] = shuf_test(fc_sctx_dc, SV_d_noVent, ...
                                   1000, 'pearson');
[sc_sctx_p, sc_sctx_d] = shuf_test(sc_sctx_dc, SV_d_noVent, ...
                                   1000, 'pearson');
                               

% Create figure
f = figure,
    set(gcf,'color','w');
    set(gcf,'units','normalized','position',[0 0 1 0.3])

    % Functional cortical hubs and cortical thickness
    ax1 = subplot(1, 4, 1); hold on
    enigma_scatter(ax1, fc_ctx_dc, CT_d, 'scatter_color', [0.66 0.13 0.11], 'linear_fit', 1, ...
                   'fit_color', [0.66 0.13 0.11], 'xlabel', 'Cortico-cortical degree centrality', ...
                   'ylabel', 'Cortical thickness (Cohen''s d)', 'xlim', [5 30], 'ylim', [-1 0.5], ...
                   'corr_value', fc_ctx_r(1, 2), 'p_value', fc_ctx_p, 'p_type', 'spin')

    % Functional subcortical hubs and subcortical volume
    ax2 = subplot(1, 4, 2); hold on
    enigma_scatter(ax2, fc_sctx_dc.', SV_d_noVent, 'scatter_color', [0.66 0.13 0.11], 'linear_fit', 1,...
                   'fit_color', [0.66 0.13 0.11], 'xlabel', 'Subcortico-cortical degree centrality', ...
                   'ylabel', 'Subcortical volume (Cohen''s d)', 'xlim', [1 13], 'ylim', [-1 0.5], ...
                   'corr_value', fc_sctx_r(1, 2), 'p_value', fc_sctx_p, 'p_type', 'shuf')

    % Structural cortical hubs and cortical thickness
    ax3 = subplot(1, 4, 3); hold on
    enigma_scatter(ax3, sc_ctx_dc, CT_d, 'scatter_color', [0.20 0.33 0.49],'linear_fit', 1, ...
                   'fit_color', [0.20 0.33 0.49], 'xlabel', 'Cortico-cortical degree centrality', ...
                   'ylabel', 'Cortical thickness (Cohen''s d)', 'xlim', [0 350], 'ylim', [-1 0.5], ...
                   'corr_value', sc_ctx_r(1, 2), 'p_value', sc_ctx_p, 'p_type', 'spin')

    % Structural subcortical hubs and subcortical volume
    ax4 = subplot(1, 4, 4); hold on
    enigma_scatter(ax4, sc_sctx_dc.', SV_d_noVent, 'scatter_color', [0.20 0.33 0.49], 'linear_fit', 1,...
                   'fit_color', [0.20 0.33 0.49], 'xlabel', 'Subcortico-cortical degree centrality', ...
                   'ylabel', 'Subcortical volume (Cohen''s d)', 'xlim', [90 375], 'ylim', [-1 0.5], ...
                   'corr_value', sc_sctx_r(1, 2), 'p_value', sc_sctx_p, 'p_type', 'shuf')
                               
               

% Identify cortical epicenters
fc_ctx_epi              = zeros(size(fc_ctx, 1), 1);
fc_ctx_epi_p            = zeros(size(fc_ctx, 1), 1);
for seed = 1:size(fc_ctx, 1)
    seed_conn           = fc_ctx(:, seed);
    r_tmp               = corrcoef(seed_conn, CT_d);
    fc_ctx_epi(seed)    = r_tmp(1, 2);
    fc_ctx_epi_p(seed)  = spin_test(seed_conn, CT_d, 'fsa5', ...
                                   'aparc', 1000, 'pearson');
end

sc_ctx_epi              = zeros(size(sc_ctx, 1), 1);
sc_ctx_epi_p            = zeros(size(sc_ctx, 1), 1);
for seed = 1:size(sc_ctx, 1)
    seed_conn           = sc_ctx(:, seed);
    r_tmp               = corrcoef(seed_conn, CT_d);
    sc_ctx_epi(seed)    = r_tmp(1, 2);
    sc_ctx_epi_p(seed)  = spin_test(seed_conn, CT_d, 'fsa5', ...
                                   'aparc', 1000, 'pearson');
end

% Project the results on the surface brain
f = figure,
    plot_cortical(parcel_to_surface(fc_ctx_epi, 'aparc_fsa5'), 'fsa5', 'functional cortical epicenters')
    colorbar_range([-0.5 -0.2])
    colormap(flipud(Reds))

f = figure,
    plot_cortical(parcel_to_surface(sc_ctx_epi, 'aparc_fsa5'), 'fsa5', 'structural cortical epicenters')
    colorbar_range([-0.5 0])
    colormap(flipud(Blues))

    
% Identify subcortical epicenters
fc_sctx_epi             = zeros(size(fc_sctx, 1), 1);
fc_sctx_epi_p           = zeros(size(fc_sctx, 1), 1);
for seed = 1:size(fc_sctx, 1)
    seed_conn           = fc_sctx(seed, :);
    r_tmp               = corrcoef(seed_conn, CT_d);
    fc_sctx_epi(seed)   = r_tmp(1, 2);
    fc_sctx_epi_p(seed) = spin_test(seed_conn, CT_d, ...
                                    'fsa5', 1000);
end