function [components, variance, correlation_matrix, names] = cross_disorder_effect(varargin)
%
% Usage:
%   [components, variance, ~, names] = cross_disorder_effect(varargin)
%   [~, ~, correlation_matrix, names] = cross_disorder_effect(varargin)
%
% Description:
%   Cross-disorder effect (authors: @boyongpark, @saratheriver)   
%
% Name/value pairs:
%   disorder (cell array, optional) - Any combination of disorder name. 
%       Default is all available disorders, except 'adhd' due to NaNs.
%       Options are any combination of {'22q', 'adhd', 'asd', 'bipolar', 
%       'depression', 'epilepsy', 'ocd', 'schizophrenia'}.
%   measure (cell array, optional) - Any combination of measure names 
%       Default is {'CortThick', 'CortSurf', 'SubVol'}.
%   additional_data_cortex (double array, optional) - Name for additional *cortical* ENIGMA-type data.
%       Must also provide 'additional_name_cortex'.
%   additional_name_cortex (cell array, optional) - Additional *cortical* ENIGMA-type data (n,
%       68). Must also provide 'additional_data_cortex'. Default is empty.
%   additional_data_subcortex (double array, optional) - Name for additional *subcortical* ENIGMA-type data.
%       Must also provide 'additional_name_subcortex'.
%   additional_name_subcortex (cell array, optional) - Additional *subcortical* ENIGMA-type data (n,
%       16). Must also provide 'additional_data_subcortex'. Default is empty.
%   ignore (cell array, optional) - Ignore summary statistics with these expressions. 
%       Default is ('mega') as it contains NaNs.
%   include (cell array, optional) - Include only summary statistics with these expressions. 
%       Default is empty.
%   method (string, optional) - Analysis method {'pca', 'correlation'}.
%       Default is 'pca'.
%
% Outputs:
%   components (structure) - Principal components of shared effects in 
%       descending order in terms of component variance. Only is method is 'pca'.
%   variance (structure) - Variance of components. Only is method is 'pca'.
%   correlation_matrix (structure) - Correlation matrices of for every
%       pair of shared effect maps. Only is method is 'correlation'.
%   names (structure) - Names of disorder and case-control effect maps
%       included in analysis.
%
% Sara Lariviere  |  saratheriver@gmail.com

% default options
all_disorders = {'22q', 'asd', 'bipolar', 'depression', 'epilepsy', 'ocd', 'schizophrenia'};
all_measures = {'CortThick', 'CortSurf', 'SubVol'}; 

p = inputParser;
addParameter(p, 'disorder', all_disorders, @iscell);
addParameter(p, 'measure', all_measures, @iscell); 
addParameter(p, 'additional_data_cortex', [], @isnumeric);
addParameter(p, 'additional_name_cortex', {}, @iscell);
addParameter(p, 'additional_data_subcortex', [], @isnumeric);
addParameter(p, 'additional_name_subcortex', {}, @iscell);
addParameter(p, 'ignore', {'mega'}, @iscell);
addParameter(p, 'include', {}, @iscell);
addParameter(p, 'method', 'pca', @ischar);

% Parse the input
parse(p, varargin{:});
in = p.Results;

mat_d.cortex = []; mat_d.subcortex = [];
names.cortex = {}; names.subcortex = {};
for ii = 1:length(in.disorder)
    % Load summary statistics
    sum_stats = load_summary_stats(in.disorder{ii});
    fieldos = fieldnames(sum_stats);
    
    % Loop through structure fields (case-control options)
    for jj = 1:length(fieldnames(sum_stats))
        if contains(fieldos{jj}, 'Cort')
            if isempty(in.include)
                if ~contains(fieldos{jj}, in.ignore) && ...
                    any(contains(fieldos{jj}, in.measure))
                        ssc = struct2cell(sum_stats);
                        mat_d.cortex = [mat_d.cortex; table2array(ssc{jj}(:, 3)).'];
                        names.cortex = [names.cortex; [in.disorder{ii}, ': ', fieldos{jj}]];
                end
            elseif ~isempty(in.include)
                if ~contains(fieldos{jj}, in.ignore) && ...
                    contains(fieldos{jj}, in.include) && ...
                    any(contains(fieldos{jj}, in.measure))
                        ssc = struct2cell(sum_stats);
                        mat_d.cortex = [mat_d.cortex; table2array(ssc{jj}(:, 3)).'];
                        names.cortex = [names.cortex; [in.disorder{ii}, ': ', fieldos{jj}]];
                end
            end
        elseif contains(fieldos{jj}, 'Sub')
            if isempty(in.include)
                if ~contains(fieldos{jj}, in.ignore) && ...
                    any(contains(fieldos{jj}, in.measure))
                        ssc = struct2cell(sum_stats);
                        mat_d.subcortex = [mat_d.subcortex; table2array(ssc{jj}(:, 3)).'];
                        names.subcortex = [names.subcortex; [in.disorder{ii}, ': ', fieldos{jj}]];
                end
            elseif ~isempty(in.include)
                if ~contains(fieldos{jj}, in.ignore) && ...
                    contains(fieldos{jj}, in.include) && ...
                    any(contains(fieldos{jj}, in.measure))
                        ssc = struct2cell(sum_stats);
                        mat_d.subcortex = [mat_d.subcortex; table2array(ssc{jj}(:, 3)).'];
                        names.subcortex = [names.subcortex; [in.disorder{ii}, ': ', fieldos{jj}]];
                end
            end
        end
    end
end

% If additional data and name
if ~isempty(in.additional_data_cortex) && ~isempty(in.additional_name_cortex)
    mat_d.cortex = [mat_d.cortex; in.additional_data];
    names.cortex = [names.cortex; in.additional_name];
end

if ~isempty(in.additional_data_subcortex) && ~isempty(in.additional_name_subcortex)
    mat_d.subcortex = [mat_d.subcortex; in.additional_data];
    names.subcortex = [names.subcortex; in.additional_name];
end

switch in.method
    case 'pca' 
        % Peform PCA on data matrix
        [~, components.cortex, ~, ~, variance.cortex] = pca(mat_d.cortex.', 'Rows','complete');
        variance.cortex = variance.cortex ./ 100;
        [~, components.subcortex, ~, ~, variance.subcortex] = pca(mat_d.subcortex.', 'Rows','complete');
        variance.subcortex = variance.subcortex ./ 100;
        correlation_matrix = [];
        
    case 'correlation'
        % Perform cross-correlation
        components.cortex = []; components.subcortex = [];
        variance.cortex = []; variance.subcortex = [];
        correlation_matrix.cortex = corrcoef(mat_d.cortex.');
        correlation_matrix.subcortex = corrcoef(mat_d.subcortex.');
        
end
return