function class_mean = economo_koskinas_spider(parcel_data, varargin)
%
% Usage:
%   class_mean = economo_koskinas_spider(parcel_data, varargin)
%
% Description:
%   Stratify parcellated data according to von Economo-Koskinas 
%       cytoarchitectonic classes (authors: @caseypaquola, @saratheriver)
%
% Inputs:
%   parcel_data (double array) - vector of data
%       Parcellated data.
%
% Name/value pairs:
%   parcellation (string, optional) - Parcellation to go from parcel_data to 
%       surface. Default is 'aparc_fsa5'.
%   fill (double, optional) - Value for mask. Default is 0.
%   title (string, optional) - Title of spider plot. Default is empty.
%   axis_range (double array, optional) - Range of spider plot axes. 
%       Default is (min, max).
%   label (cell array, optional) - List of axis labels. Length = 5.
%       Default is names of von Economo-Koskinas cytoarchitectonic classes.
%   color (double array, optional) - Color of line. Default is [0 0 0].
%
% Outputs:
%   class_mean (double array) - Mean values within each von 
%       Economo-Koskinas cytoarchitectonic class.
%   figure
%       Spider plot.
%
% Sara Lariviere  |  saratheriver@gmail.com

% data check
if nargin < 1; error('Need data to plot'); end

p = inputParser;
addParameter(p, 'parcellation', 'aparc_fsa5', @ischar);
addParameter(p, 'fill', 0, @isnumeric);
addParameter(p, 'title', '', @ischar);
addParameter(p, 'axis_range', [], @isnumeric);
addParameter(p, 'label', {}, @iscell);
addParameter(p, 'color', [0 0 0], @isnumeric);
addParameter(p, 'f', gca, @isgraphics);
addParameter(p, 'background', [1 1 1], @isnumeric);

% Parse the input
parse(p, varargin{:});
in = p.Results;


% Map parcellated data to the surface
surf_data = parcel_to_surface(parcel_data, in.parcellation, in.fill);

% average within ve classes
if contains(in.parcellation, 'fsa5')
    ve = dlmread('economo_koskinas_fsa5.csv');
elseif contains(in.parcellation, 'conte69')
    ve = dlmread('economo_koskinas_conte69.csv');
end
ve_class = zeros(5, 1);
for ii = 1:5
    id = find(ve == ii);
    ve_class(ii) = nanmean(surf_data(id));
end

class_mean = array2table(ve_class.', 'VariableNames', {'Agranular', 'Frontal', ...
                         'Parietal', 'Polar', 'Granular'});

data_orig = class_mean;
class_mean = class_mean{:, :}';

% re-defined optional inputs
if isempty(in.axis_range)
    in.axis_range = [min(class_mean) max(class_mean)];
end
if isempty(in.label)
    in.label = data_orig.Properties.VariableNames;
end

% check labels
if size(in.label, 1) ~= size(class_mean, 1)
    in.label = in.label.';
end
    
% Rep axis_range
axis_range = repmat([min(class_mean) max(class_mean)], size(class_mean, 1), 1)

% size segments and number of cases
[r c] = size(class_mean);
% exit for too few axes
if r < 3
	errordlg('Must have at least three measurement axes')
	error('Program Termination:  Must have a minimum of three axes')
end
ax = gca;
ca = ax; 
cla(ca); 

hold on

% set the axes to the current text axes
axes(ax)
% set to add plot
set(ax,'nextplot','add');

% clear figure and set limits
set(ca,'visible','off'); %set(f,'color','w')
set(ca,'xlim',[-1.25 1.25],'ylim',[-1.25 1.25]); axis(ca,'equal','manual')
% title
text(0,1.3, in.title, 'horizontalalignment','center','fontweight','bold',...
     'fontsize', 18);


% scale by range
angw = linspace(0,2*pi,r+1)';
mag = (class_mean - in.axis_range(:,1) * ones(1,c)) ./ (diff(in.axis_range,[],2) * ones(1,c));
% scale trimming
mag(mag < 0) = 0; mag(mag > 1) = 1;
% wrap data (close the last axis to the first)
ang = angw(1:end-1); angwv = angw * ones(1,c); magw = [mag; mag(1,:)];


% make the plot
% define the axis locations
start = [zeros(1,r); cos(ang')]; stop = [zeros(1,r); sin(ang')];
% plot the axes
plot(ca,start,stop,'color',[.6 .6 .6],'linestyle','-'); axis equal
% plot axes markers
inc = 0.25:.25:1; mk = .025 * ones(1,4); tx = 4 * mk; tl = 0:.25:1;
% loop each axis ang plot the line markers and labels
% add axes
for ii = 1:r
    for kk = 1:length(inc)-1
        xCenter = 0;
        yCenter = 0;
        theta = 0 : 0.01 : 2*pi;
        radius = inc(kk);
        x = radius * cos(theta) + xCenter;
        y = radius * sin(theta) + yCenter; 
        plot(x,y,'color',[ .6 .6 .6])
    end
    
	% label the tick marks
    if ii == 1
        newinc = 0:0.25:0.75;
        for jj = [1:4]
    		temp = text([cos(ang(ii)) * newinc(jj) + sin(ang(ii)) * tx(jj)], ...
    				[sin(ang(ii)) * newinc(jj) - cos(ang(ii)) * tx(jj)], ...
    				num2str(chop(in.axis_range(ii,1) + newinc(jj)*diff(in.axis_range(ii,:)),2)), ...
    				'fontsize', 10);
            temp.Color = [.6 .6 .6];     
            % flip the text alignment for lower axes
            if ang(ii) >= pi
                set(temp,'HorizontalAlignment','right')
            end
        end
	end
	% label each axis
	temp = text([cos(ang(ii)) * 1.1 + sin(ang(ii)) * 0], ...
			[sin(ang(ii)) * 1.1 - cos(ang(ii)) * 0], ...
			char(in.label(ii,:)), 'fontsize', 14);
	% flip the text alignment for right side axes
	if ang(ii) > pi/2 && ang(ii) < 3*pi/2
		set(temp,'HorizontalAlignment','right')
	end
end


% plot the data
o = polar(ca,angw*ones(1,c),magw);
% set color of the lines
for ii = 1:c; 
    set(o(ii),'color',in.color(ii,:),'linewidth',3); 
end

% set background color
set(gcf,'Color', in.background)

return

function [v] = rd(v,dec)
% quick round function (to specified decimal)
% function [v] = rd(v,dec)
%
% inputs  2 - 1 optional
% v       number to round    class real
% dec     decimal loaction   class integer
%
% outputs 1
% v       result             class real
%
% positive dec shifts rounding location to the right (larger number)
% negative dec shifts rounding location to the left (smaller number)
%
% michael arant
% Michelin Maericas Research and Development Corp
if nargin < 1; help rd; error('I/O error'); end

if nargin == 1; dec = 0; end

v = v / 10^dec;
v = round(v);
v = v * 10^dec;

function [val] = color_index(len)
% get unique colors for each item to plot
% function [val] = color_index(len)
%
% inputs  1
% len     number of objects     class integer
%
% outputs 1
% val     color vector          class real
%
% michael arant

if nargin < 1 || nargout < 1; help color_index; error('I / O error'); end

if len == 1
	val = [0 0 0];
else
	% initial color posibilities (no white)
	% default color scale
	col = [	0 0 0
			0 0 1
			0 1 1
			0 1 0
			1 1 0
			1 0 1
			1 0 0];

	% reduce if fewer than 6 items are needed (no interpolation needed)
	switch len
		case 1, col([2 3 4 5 6 7],:) = [];
		case 2, col([2 3 4 5 6],:) = [];
		case 3, col([3 4 5 6],:) = [];
		case 4, col([3 5 6],:) = [];
		case 5, col([5 6],:) = [];
		case 6, col(6,:) = [];
	end

	% number of requested colors
	val = zeros(len,3); val(:,3) = linspace(0,1,len)';

	% interpolate to fill in colors
	val(:,1) = interp1q(linspace(0,1,size(col,1))',col(:,1),val(:,3));
	val(:,2) = interp1q(linspace(0,1,size(col,1))',col(:,2),val(:,3));
	val(:,3) = interp1q(linspace(0,1,size(col,1))',col(:,3),val(:,3));
end

function [res] = isint(val)
% determines if value is an integer
% function [res] = isint(val)
%
% inputs  1
% val     value to be checked              class real
%
% outputs 1
% res     result (1 is integer, 0 is not)  class integer
%
% michael arant     may 15, 2004
if nargin < 1; help isint; error('I / O error'); end

% numeric?
if ~isnumeric(val); error('Must be numeric'); end

% check for real number
if isreal(val) & isnumeric(val)
%	check for integer
	if round(val) == val
		res = 1;
	else
		res = 0;
	end
else
	res = 0;
end

return