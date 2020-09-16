%% Add the path to the ENIGMA TOOLBOX matlab folder
addpath(genpath('/path/to/ENIGMA/matlab/'));

%% Figure 1b. Load example data
% Load example data
[cov, metr1_SubVol, metr2_CortThick, metr3_CortSurf] = load_example_data();

% Z-score data in patients relative to controls
groups       = cov.Dx;
controlGroup = 0;
CortThick_Z  = zscore_matrix(metr2_CortThick(:, 2:end-5), groups, controlGroup);
SubVol_Z     = zscore_matrix(metr1_SubVol(:, 2:end-1), groups, controlGroup);

% Extract data for a specific group (e.g., individuals with left TLE)
CortThick_Z_LTLE = CortThick_Z(cov.SDx == 3, :);
SubVol_Z_LTLE    = SubVol_Z(cov.SDx == 3, :);


%% Figure 1d. Load summary statistics
% Load summary statistics for a given disease (e.g., epilepsy)
sum_stats = load_summary_stats('epilepsy');

% List available summary statistic tables
sum_stats


%% Figure 2b. Surface data visualization
% Re-order subcortical data (alphabetically and by hemisphere)
SubVol_Z_LTLE_r = reorder_sctx(SubVol_Z_LTLE);

% Mean data across all individuals with left TLE
CortThick_Z_LTLE_mean = varfun(@mean, CortThick_Z_LTLE)
SubVol_Z_LTLE_r_mean  = varfun(@mean, SubVol_Z_LTLE_r);

% Map parcellated data to the surface (cortical values only)
CortThick_Z_LTLE_mean_fsa5 = parcel_to_surface(CortThick_Z_LTLE_mean{:, :}, ...
                                               'aparc_fsa5');

% Project data to the surface templates
f = figure,
    plot_cortical(CortThick_Z_LTLE_mean_fsa5, 'fsa5')
    colormap(flipud(Blues)); colorbar_range([-2, 0]) 
    
f = figure,
    plot_subcortical(SubVol_Z_LTLE_r_mean{:, :})
    colormap(flipud(Blues)); colorbar_range([-3, 0]) 
                 
                 
%% Figure 3b. Fetch disease-related gene expression data
% Fetch gene expression data
[genes, ~, genelabels] = fetch_ahba();

% Get the names of epilepsy-related genes (Focal HS phenotype)
epilepsy_genes = risk_genes('epilepsy');
epilepsy_genes = find(ismember(genelabels, epilepsy_genes.focalhs));

% Extract gene expression data for epilepsy (Focal HS)
epilepsy_gene_data = genes(:, epilepsy_genes);


%% Figure 4b. Load connectivity data
% Load functional connectivity data
[ctx, ctx_labels, sctx, sctx_labels] = load_fc();


%% Figure 5b. Hub susceptibility model
% Remove subcortical values corresponding to the ventricles
SubVol_Z_LTLE_r_mean_noVent               = SubVol_Z_LTLE_r_mean;
SubVol_Z_LTLE_r_mean_noVent.mean_LLatVent = [];
SubVol_Z_LTLE_r_mean_noVent.mean_RLatVent = [];

% Compute weighted degree centrality measures
ctx_dc  = sum(ctx, 1);
sctx_dc = sum(sctx, 2);

% Perform spatial correlations between hubs and mean atrophy
ctx_r  = corrcoef(ctx_dc, CortThick_Z_LTLE_mean{:, :});
sctx_r = corrcoef(sctx_dc, SubVol_Z_LTLE_r_mean_noVent{:, :});

% Spin permutation testing for two cortical maps
ctx_p  = spin_test(ctx_dc, CortThick_Z_LTLE_mean{:, :}, ...
                   'fsa5', 1000, 'pearson');

% Shuf permutation testing for two subcortical maps 
sctx_p = shuf_test(sctx_dc, SubVol_Z_LTLE_r_mean_noVent{:, :}, ...
                   1000, 'pearson');


%% Figure 6b. Disease epicenter mapping
% Identify cortical epicenters
ctx_epi              = zeros(size(ctx, 1), 1);
ctx_epi_p = zeros(size(ctx, 1), 1);
for seed = 1:size(ctx, 1)
    seed_conn        = ctx(:, seed);
    r_tmp            = corrcoef(seed_conn, CortThick_Z_LTLE_mean{:, :});
    ctx_epi(seed)    = r_tmp(1, 2);
    ctx_epi_p(seed)  = spin_test(seed_conn, CortThick_Z_LTLE_mean{:, :}, ...
                                 'fsa5', 1000, 'pearson');
end

% Identify subcortical epicenters
sctx_epi             = zeros(size(sctx, 1), 1);
sctx_epi_p           = zeros(size(sctx, 1), 1);
for seed = 1:size(sctx, 1)
    seed_conn        = sctx(seed, :);
    r_tmp            = corrcoef(seed_conn, CortThick_Z_LTLE_mean{:, :});
    sctx_epi(seed)   = r_tmp(1, 2);
    sctx_epi_p(seed) = spin_test(seed_conn, CortThick_Z_LTLE_mean{:, :}, ...
                                 'fsa5', 1000, 'pearson');
end
