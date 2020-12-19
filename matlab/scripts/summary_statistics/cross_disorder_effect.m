function [components, variance] = cross_disorder_effect(varargin)

sum_stats = load_summary_stats('epilepsy')

% Get case-control subcortical volume and cortical thickness tables
SV = sum_stats.SubVol_case_vs_controls_ltle;
CT = sum_stats.CortThick_case_vs_controls_ltle;

% Extract Cohen's d values
SV_d = SV.d_icv;
CT_d = CT.d_icv;

% default options
all_disorders = {'22q', 'adhd', 'asd', 'bipolar', 'depression', 'epilepsy', 'ocd', 'schizophrenia'};
all_measures = {'SubVol', 'CortThick', 'CortSurf'}

p = inputParser;
addParameter(p, 'disorder', all_disorders, @iscell);
addParameter(p, 'measure', all_measures, @iscell); 
addParameter(p, 'stats', 'cohensd', @ischar);
addParameter(p, 'additional_data', [], @isnumeric);
addParameter(p, 'ignore', {''}, @iscell);

% Parse the input
parse(p, varargin{:});
in = p.Results;

mat = [];
for ii = 1:length(in.disorder)
    A_cell = struct2cell(sum_stats);
    length(fieldnames(sum_stats))
    fieldnames(sum_stats)
end

% Peform PCA on data matrix
[~, components, ~, ~, variance] = pca(mat);

return