function enigma_scatter(ax, x, y, varargin)

% Usage: enigma_scatter(ax, x, y, varargin)
% 
% REQUIRED INPUTS
% ax             = figure axis
% x, y           = two maps (ndarray)
%
% OPTIONAL INPUTS
% scatter_color  = color of data in scatter plot, default is black 
% linear_fit     = add linear fit on top of scatter, default is 0 (1 for true)
% fit_color      = color of line fit if linear_fit is 1 (default is black)
% xlim           = x-axis limit (tuple), default is xmin-xmax
% ylim           = y-axis limit (tuple), default is ymin-ymax
% xlabel         = label of x axis (string), default is None
% ylabel         = label of y axis (string), default is None
% corr_value     = add r=correlation value if provided (number), default is None
% p_value        = add p_spin=p-value if provided (number), default is None
% p_type         = spin (default), shuf
% 
% Sara Lariviere | Sunny (but cold) September day 2020

p = inputParser;
addParameter(p, 'scatter_color', [0 0 0], @isnumeric);
addParameter(p, 'linear_fit', 0, @isnumeric);
addParameter(p, 'fit_color', [0 0 0], @isnumeric);
addParameter(p, 'xlim', [min(x) max(x)], @isnumeric);
addParameter(p, 'ylim', [min(y) max(y)], @isnumeric);
addParameter(p, 'xlabel', "", @ischar);
addParameter(p, 'ylabel', "", @ischar);
addParameter(p, 'corr_value', [], @isnumeric);
addParameter(p, 'p_value', [], @isnumeric);
addParameter(p, 'p_type', 'spin', @ischar);

% Parse the input
parse(p, varargin{:});
in = p.Results;

% check dimensions
if size(y, 2) ~= size(x, 2)
    x = x.';
end

% scatter plot
s1      = scatter(x, y, 88, in.scatter_color, 'filled');  
xlim(in.xlim);
ylim(in.ylim);

% linear fit
if in.linear_fit == 1
    P1      = polyfit(x, y, 1);                               
    yfit_1  = P1(1) * x + P1(2);
    plot(x, yfit_1, 'color', in.fit_color, 'LineWidth', 3) 
end

% axis labels
set(get(ax, 'XLabel'), 'String', in.xlabel);   
set(get(ax, 'YLabel'), 'String', in.ylabel);   

% correlation and p- values
if ~isempty(in.corr_value) && ~isempty(in.p_value)
    text(in.xlim(1) + (((in.xlim(2) - in.xlim(1)) / 100) * 5), ...
         in.ylim(1) + (((in.ylim(2) - in.ylim(1)) / 100) * 5), ... 
         ['{\it r}=' num2str(round(in.corr_value,2)) ...
         ', {\it p}' '_{' in.p_type '}' '=' num2str(round(in.p_value,2))]); 

% correlation value only
elseif ~isempty(in.corr_value) && isempty(in.p_value)
text(in.xlim(1) + (((in.xlim(2) - in.xlim(1)) / 100) * 5), ...
     in.ylim(1) + (((in.ylim(2) - in.ylim(1)) / 100) * 5), ... 
     ['{\it r}=' num2str(round(in.corr_value,2))])

% p-value only
elseif isempty(in.corr_value) && ~isempty(in.p_value)
text(in.xlim(1) + (((in.xlim(2) - in.xlim(1)) / 100) * 5), ...
     in.ylim(1) + (((in.ylim(2) - in.ylim(1)) / 100) * 5), ... 
     ['{\it p}' '_{' in.p_type '}' '=' num2str(round(in.p_value,2))]);
end

return