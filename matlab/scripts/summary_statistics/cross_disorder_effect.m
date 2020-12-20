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
%   disorder (cell array, optional) - Any combination of disorder name. Default is all available disorders
%       {'22q', 'adhd', 'asd', 'bipolar', 'depression', 'epilepsy', 'ocd', 'schizophrenia'}.
%   measure (cell array, optional) - Any combination of measure names 
%       Default is {'CortThick', 'CortSurf'}.
%   additional_data (double array, optional) - Name for additional ENIGMA-type data.
%       Must also provide 'additional_name'.
%   additional_name (cell array, optional) - Additional ENIGMA-type data (n,
%       68). Must also provide 'additional_data'.
%   ignore (cell array, optional) - Ignore summary statistics with these expressions. 
%       Default is ('mega') as it contains NaNs.
%   method (string, optional) - Analysis method {'pca', 'correlation'}.
%       Default is 'pca'.
%   figure (string, optional) - Whether to output figures {'True', 'False'}. 
%       Default is 'True'.
%
% Outputs:
%   components (double array) - Principal components of shared effects in 
%       descending order in terms of component variance. Only is method is 'pca'.
%   variance (double array) - Variance of components. Only is method is 'pca'.
%   correlation_matrix (double array) - Correlation matrix of for every
%       pair of shared effect maps. Only is method is 'correlation'.
%   names (cell array) - Name of disorder and case-control effect maps
%       included in analysis.
%
% Sara Lariviere  |  saratheriver@gmail.com

% default options
all_disorders = {'22q', 'adhd', 'asd', 'bipolar', 'depression', 'epilepsy', 'ocd', 'schizophrenia'};
all_measures = {'CortThick', 'CortSurf'}; % only cortical measures for now since only epilepsy has subcortical volumes

p = inputParser;
addParameter(p, 'disorder', all_disorders, @iscell);
addParameter(p, 'measure', all_measures, @iscell); 
addParameter(p, 'additional_data', [], @isnumeric);
addParameter(p, 'additional_name', {}, @iscell);
addParameter(p, 'ignore', {'mega'}, @iscell); % because of nans in data
addParameter(p, 'method', 'pca', @ischar); % correlation
addParameter(p, 'figure', 'True', @ischar);

% Parse the input
parse(p, varargin{:});
in = p.Results;

mat_d = [];
names = {};
for ii = 1:length(in.disorder)
    % Load summary statistics
    sum_stats = load_summary_stats(in.disorder{ii});
    fieldos = fieldnames(sum_stats);
    
    % Loop through structure fields (case-control options)
    for jj = 1:length(fieldnames(sum_stats))
        if ~contains(fieldos{jj}, in.ignore) && ...
            any(contains(fieldos{jj}, in.measure))
                ssc = struct2cell(sum_stats);
                mat_d = [mat_d; table2array(ssc{jj}(:, 3)).'];
                names = [names; [in.disorder{ii}, ': ', fieldos{jj}]];
        end
    end
end

% If additional data and name
if ~isempty(in.additional_data) && ~isempty(in.additional_name)
    mat_d = [mat_d; in.additional_data];
    names = [names; in.additional_name];
end

switch in.method
    case 'pca' 
        % Peform PCA on data matrix
        [~, components, ~, ~, variance] = pca(mat_d.', 'Rows','pairwise');
        variance = variance ./ 100;
        correlation_matrix = [];
        
        % plot principal component on brain surface
        if strcmp(in.figure, 'True')
           f = figure,
               plot_cortical(parcel_to_surface(components(:, 1)), 'color_range', [-0.5 0.5], 'cmap', 'RdBu_r')
        end
        
    case 'correlation'
        % Perform cross-correlation
        components = [];
        variance = [];
        correlation_matrix = corrcoef(mat_d.');
        
        % plot correlation matrix
        if strcmp(in.figure, 'True')
            f = figure('units','normalized','outerposition',[0 0 .65 1]),
                imagesc(correlation_matrix, [-1 1])
                axis square;
                colormap(RdBu_r);
                colorbar;
                set(gca, 'YTick', 1:1:size(correlation_matrix, 1), ...
                    'YTickLabel', strrep(names, '_', ' '), 'XTick', 1:1:size(correlation_matrix, 1), ...
                    'XTickLabel', strrep(names, '_', ' '), 'XTickLabelRotation', 45)
        end
end
return