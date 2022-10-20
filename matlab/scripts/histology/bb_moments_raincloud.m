function bb_moments_raincloud(region_idx, parcellation, title)
%
% Usage:
%   bb_moments_raincloud(region_idx, title)
%
% Description:
%   Stratify regional data according to BigBrain statistical moments 
%       (authors: @caseypaquola, @saratheriver)
%
% Inputs:
%   region_idx (double array) - vector of data.
%       Indices of regions to be included in analysis.
%       parcellation (string, optional) - Name of parcellation.
%       Options are: 'aparc', 'schaefer_100', 'schaefer_200', 'schaefer_300',
%       'schaefer_400', 'glasser_360'. Default is 'aparc'.
%   title (string, optional) - Title of raincloud plot. Default is empty.
%
% Outputs:
%   figure
%       Raincloud plot.
%
% Sara Lariviere  |  saratheriver@gmail.com

% data check
if nargin < 1; error('Need data to plot'); end
if nargin < 2; parcellation = 'aparc'; end
if nargin < 3; title = ''; end

% Load BigBrain statistical moments (mean, skewness) 
bb_moments = dlmread(['bb_moments_' parcellation '.csv']);
bb_moments = bb_moments([2 4], :);
bb_moments(1,:) = rescale(bb_moments(1,:), -1, 1);
bb_moments(2,:) = rescale(bb_moments(2,:), -1, 1);

% Moments colors
spec = [158,1,66; 102,194,165]/255;

% Plot first moment at the top
inv = 2 * (size(bb_moments, 1):-1:1);

% Initiate figure
set(gcf, 'color', 'white', 'renderer', 'painters', ...
    'units','normalized','position',[0 0 .7 .4]);
hold on

% Loop over BigBrain moments
for ii = 1:size(bb_moments, 1)
    jj = inv(ii);
     
    % Scatter plot
    scatter(bb_moments(ii, region_idx), ...
            rand([length(region_idx), 1])*.3 + (jj - 0.15), ...
            122, spec(ii,:), 'filled', 'MarkerEdgeColor', [1 1 1], ...
            'LineWidth', 0.88, 'MarkerFaceAlpha', 0.88)

    % Density distribution
    [fi,xi] = ksdensity(bb_moments(ii, region_idx), 'Function', 'pdf');
    p = patch(xi, fi + jj + 0.3, spec(ii,:));
    p.EdgeColor = [1 1 1];
    p.LineWidth = 0.75;
    p.EdgeAlpha = 0;
    p.FaceAlpha = .88;

    % In-house box plot
    qr = [prctile(bb_moments(ii, region_idx), 25) prctile(bb_moments(ii, region_idx), 75)];
    rectangle('position',[qr(1) jj-0.15 qr(2)-qr(1) .3], 'FaceColor', [spec(ii, :) 0.41], ...
                  'EdgeColor', [0 0 0 .88], 'LineWidth', 1.5, 'Curvature', [.1 .1]);
    
    % Median line
    line([median(bb_moments(ii, region_idx)) median(bb_moments(ii, region_idx))], ...
          [(jj-0.15) (jj+0.15)], 'color', [0 0 0], 'linewidth', 4)  

    % Detect outliers, and if any, excluse them from the whiskers
    if sum(isoutlier(bb_moments(ii, region_idx))) == 0
        mini = nanmin(bb_moments(ii, region_idx));
        maxi = nanmax(bb_moments(ii, region_idx));
    else
        outid = find(isoutlier(bb_moments(ii, region_idx)));
        dat = bb_moments(ii, region_idx);
        dat(outid) = [];
        mini = nanmin(dat);
        maxi = nanmax(dat);
    end
    line([mini qr(1)], ...
          [jj jj], 'color', [0 0 0], 'linewidth', 1.5)  
    line([qr(2) maxi], ...
          [jj jj], 'color', [0 0 0], 'linewidth', 1.5)  

    % Figure axes and other things to prettify
    box off
    yticks([2.4 4.4])
    xticks([-1.5 -1 -0.5 0 0.5 1 1.5])
    set(gca, 'TickLength', [0, 0], 'YTickLabel', ...
        {'Skewness', 'Mean'}, 'FontSize', 18);
    ytickangle(90);
    xlim([-1.6 1.6]);
    ylim([1.5 5.5]);
    text(0, 5.5, title, 'horizontalalignment', 'center', 'fontweight', ...
        'bold', 'fontsize', 18);
end
return
