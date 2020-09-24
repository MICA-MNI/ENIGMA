%% Add the path to the ENIGMA TOOLBOX matlab folder
addpath(genpath('/path/to/ENIGMA/matlab/'));

%% Figure 1c. Load summary statistics
% Load summary statistics for a given disease (e.g., epilepsy)
sum_stats = load_summary_stats('epilepsy');

% Get cortical thickness and subcortical volume tables
CT = sum_stats.CortThick_case_vs_controls_ltle;
SV = sum_stats.SubVol_case_vs_controls_ltle;

% Extract Cohen's d values
CT_d = CT.d_icv;
SV_d = SV.d_icv;


%% Figure 2b. Surface data visualization
% Map parcellated data to the surface (cortical values only)
CT_d_fsa5 = parcel_to_surface(CT_d, 'aparc_fsa5');

% Project Cohen's d values to the surface templates
f = figure,
    plot_cortical(CT_d_fsa5, 'fsa5')
    colormap(TealRd); colorbar_range([-0.5, 0.5]) 
    
f = figure,
    plot_subcortical(SV_d)
    colormap(TealRd); colorbar_range([-0.5, 0.5]) 
                 
                 
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
[fc_ctx, fc_ctx_labels, fc_sctx, fc_sctx_labels] = load_fc();

% Load structural connectivity data
[sc_ctx, sc_ctx_labels, sc_sctx, sc_sctx_labels] = load_sc();


%% Figure 5b. Hub susceptibility model
% Remove subcortical values corresponding to the ventricles
SV_d_noVent = SV_d;
SV_d_noVent([find(strcmp(SV.Structure, 'LLatVent')); ...
            find(strcmp(SV.Structure, 'RLatVent'))], :) = [];

% Compute weighted degree centrality measures
fc_ctx_dc  = sum(fc_ctx, 1);
fc_sctx_dc = sum(fc_sctx, 2);

% Perform spatial correlations between hubs and Cohen's d
fc_ctx_r = corrcoef(fc_ctx_dc, CT_d);
fc_sctx_r = corrcoef(fc_sctx_dc, SV_d_noVent);


%% Figure 5e. Permutation testing
% Spin permutation testing for two cortical maps
fc_ctx_p  = spin_test(fc_ctx_dc, CT_d, 'fsa5', 'aparc', 1000);

% Shuf permutation testing for two subcortical maps 
fc_sctx_p = shuf_test(fc_sctx_dc, SV_d_noVent, 1000);

                  
%% Figure 6b. Disease epicenter mapping
% Identify cortical epicenters
fc_ctx_epi              = zeros(size(fc_ctx, 1), 1);
fc_ctx_epi_p            = zeros(size(fc_ctx, 1), 1);
for seed = 1:size(fc_ctx, 1)
    seed_conn           = fc_ctx(:, seed);
    r_tmp               = corrcoef(seed_conn, CT_d);
    fc_ctx_epi(seed)    = r_tmp(1, 2);
    fc_ctx_epi_p(seed)  = spin_test(seed_conn, CT_d, ...
                                    'fsa5', 1000);
end

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
