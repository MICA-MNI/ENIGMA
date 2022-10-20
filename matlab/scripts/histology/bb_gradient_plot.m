function bb_gradient_plot(data, varargin)
%
% Usage:
%   bb_gradient_plot(data, varargin)
%
% Description:
%   Stratify parcellated data according to the BigBrain gradient 
%       (authors: @caseypaquola, @saratheriver)
%
% Inputs:
%   data (double array) - vector of data
%       Parcellated data.
%
% Name/value pairs:
%   parcellation (string, optional) - Name of parcellation.
%       Options are: 'aparc', 'schaefer_100', 'schaefer_200', 'schaefer_300',
%       'schaefer_400', 'glasser_360'. Default is 'aparc'.
%   title (string, optional) - Title of spider plot. Default is empty.
%   axis_range (double array, optional) - Range of spider plot axes. 
%       Default is (min, max).
%   yaxis_label (string, optional) - Label for y-axis. Default is empty.
%   xaxis_label (string, optional) - Label for x-axis. Default is empty.
%
% Outputs:
%   figure
%       Gradient plot.
%
% Sara Lariviere  |  saratheriver@gmail.com

% data check
if nargin < 1; error('Need data to plot'); end

% Parse the input
p = inputParser;
addParameter(p, 'parcellation', 'aparc', @ischar);
addParameter(p, 'title', '', @ischar);
addParameter(p, 'axis_range', [min(data) max(data)], @isnumeric);
addParameter(p, 'yaxis_label', '', @ischar);
addParameter(p, 'xaxis_label', '', @ischar);
parse(p, varargin{:});
in = p.Results;

% Load gradient
g = dlmread(['bb_gradient_' in.parcellation '.csv']);

% Define number of bins
numbin = 5;
p = 100/numbin:100/numbin:100;
newg = nan(numbin, round(length(g)/numbin));

% Store means
means = [];

% Bin colors
spec = flipud([213, 62, 79
               253, 174, 97
               235, 235, 181
               171, 221, 164
               50, 136, 189]/255);

% Initiate figure
set(gcf, 'color', 'white', 'renderer', 'painters', ...
    'units','normalized','position',[0 0 .7 .4]);
hold on

% Loop over bins
for ii = 1:numbin
    % Split gradients into bins
    if ii == 1
        tmp = find(g <= prctile(g, p(ii)));
        newg(ii, 1:length(tmp)) = tmp;
    else
        tmp = find(g <= prctile(g, p(ii)) & ...
                           g > prctile(g, p(ii-1)));
        newg(ii, 1:length(tmp)) = tmp;
    end
    
    % Scatter bins
    scatter(rand([length(tmp), 1])*.3 + (ii - 0.15), ...
            data(newg(ii, 1:length(tmp))), 222, spec(ii,:), 'filled', ...
            'MarkerEdgeColor', [1 1 1], 'LineWidth', 0.88, ...
            'MarkerFaceAlpha', 0.88)

    % Plot mean line
    plot([ii - 0.17 ii + 0.17], [nanmean(data(newg(ii, 1:length(tmp)))) ...
        nanmean(data(newg(ii, 1:length(tmp))))], ...
        'linewidth', 10, 'color', [0 0 0])
    plot([ii - 0.16 ii + 0.16], [nanmean(data(newg(ii, 1:length(tmp)))) ...
        nanmean(data(newg(ii, 1:length(tmp))))], ...
        'linewidth', 6, 'color', spec(ii,:))

    % Store mean
    means = [means nanmean(data(newg(ii, 1:length(tmp))))];
end

% Connect means with lines (only if data in each bin)
if ~any(isnan(means))
    jj = [1:numbin-1; 2:numbin].';
    for ii = 1: size(jj, 1)
        l = patch([jj(ii, 1)+0.23 jj(ii, 2)-0.23], ...
             [means(jj(ii, 1)) means(jj(ii, 2))], [0 0 0]);
        l.FaceAlpha = 0.88;
        l.LineWidth = 2.5;
    end
else
    warning('Some empty bins, not plotting connecting lines')
end

% Figure axes and other things to prettify
box off
yticks([in.axis_range(1) in.axis_range(2)]);
xticks(1:numbin);
set(gca, 'TickLength', [0, 0], 'XTickLabel', ...
    {'Bin1', 'Bin2', 'Bin3', 'Bin4', 'Bin5'}, 'FontSize', 16);
xlim([0.5 5.5]);
ylim([in.axis_range(1) in.axis_range(2)]);
text(3, in.axis_range(2), in.title, 'horizontalalignment', 'center', 'fontweight', ...
    'bold', 'fontsize', 16);
xlabel(in.xaxis_label, 'fontsize', 20) 
ylabel(in.yaxis_label, 'fontsize', 20) 
return

