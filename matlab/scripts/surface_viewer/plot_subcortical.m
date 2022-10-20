function [a, cb] = plot_subcortical(data, varargin);
%
% Usage:
%   [a, cb] = plot_subcortical(data, varargin);   
%
% Description:
%   Plot subcortical surface with lateral and medial views (authors: @saratheriver)
%
% Inputs:
%   data (double array) - vector of data, size = [1 x v]. One value per 
%       subcortical structure, in this order: L-accumbens, L-amygdala, 
%       L-caudate, L-hippocampus, L-pallidum L-putamen, L-thalamus, 
%       L-ventricle, R-accumbens, R-amygdala, R-caudate, R-hippocampus, 
%       R-pallidum, R-putamen, R-thalamus, R-ventricle
%
% Name/value pairs:
%   ventricles (string, optional) - If 'True' (default) shows the ventricles 
%       (data must be size = [1 x 16]). If 'False', then ventricles are not 
%       shown and data must be size = [1 x 14].
%   label_text (string, optional) - Label text for colorbar. Default is empty.
%   background (string, double array, optional) - Background color. 
%       Default is 'white'.
%   color_range (double array, optional) - Range of colorbar. Default is 
%       [min(data) max(data)].
%   cmap (string, double array, optional) - Colormap name. Default is 'RdBu_r'.
%
% Outputs:
%   a (axes) - vector of handles to the axes, left to right, top to bottom
%   cb (colorbar) - colorbar handle
%
% Sara Lariviere  |  saratheriver@gmail.com

p = inputParser;
addParameter(p, 'ventricles', 'True', @ischar);
addParameter(p, 'label_text', "", @ischar);
addParameter(p, 'background', 'white', @ischar);
addParameter(p, 'color_range', [min(data) max(data)], @isnumeric);
addParameter(p, 'cmap', 'RdBu_r', @ischar);

% Parse the input
parse(p, varargin{:});
in = p.Results;

% load subcortical templates
surf_lh = SurfStatReadSurf('sctx_lh');
surf_rh = SurfStatReadSurf('sctx_rh');

% super inefficient way to attribute vertices to subcortical areas
if strcmp(in.ventricles, 'True')
    data = [repmat(data(1), 867, 1); repmat(data(2), 1419, 1); ...
            repmat(data(3), 3012, 1); repmat(data(4), 3784, 1); ...
            repmat(data(5), 1446, 1); repmat(data(6), 4003, 1); ...
            repmat(data(7), 3726, 1); repmat(data(8), 7653, 1);...
            repmat(data(9), 838, 1); repmat(data(10), 1457, 1); ...
            repmat(data(11), 3208, 1); repmat(data(12), 3742, 1); ...
            repmat(data(13), 1373, 1); repmat(data(14), 3871, 1); ...
            repmat(data(15), 3699, 1); repmat(data(16), 7180, 1)];
elseif strcmp(in.ventricles, 'False')
    data1 = nan(16, 1);
    data1([1:7 9:15]) = data;
    
    data = [repmat(data1(1), 867, 1); repmat(data1(2), 1419, 1); ...
            repmat(data1(3), 3012, 1); repmat(data1(4), 3784, 1); ...
            repmat(data1(5), 1446, 1); repmat(data1(6), 4003, 1); ...
            repmat(data1(7), 3726, 1); repmat(data1(8), 7653, 1);...
            repmat(data1(9), 838, 1); repmat(data1(10), 1457, 1); ...
            repmat(data1(11), 3208, 1); repmat(data1(12), 3742, 1); ...
            repmat(data1(13), 1373, 1); repmat(data1(14), 3871, 1); ...
            repmat(data1(15), 3699, 1); repmat(data1(16), 7180, 1)];
    
    data([18258:25910 44099:end]) = nan;
end
            
vl   = 1:size(surf_lh.coord, 2);
vr   = [1:size(surf_rh.coord, 2)] + max(size(surf_lh.coord, 2));

tl   = 1:size(surf_lh.tri, 1);
tr   = [1:size(surf_rh.tri, 1)] + max(size(surf_lh.tri, 1));
clim = [min(data),max(data)];
if clim(1) == clim(2)
    clim = clim(1) + [-1 0];
end

h=0.25;
w=0.20;

a(1)=axes('position',[0.1 0.3 w h]);
trisurf(surf_lh.tri,surf_lh.coord(1,:),surf_lh.coord(2,:),surf_lh.coord(3,:),...
    double(data(vl)),'EdgeColor','none');
% view(0,90);
view(-90,0)
daspect([1 1 1]); axis tight; camlight; axis vis3d off;
lighting phong; material dull; shading flat;

a(2)=axes('position',[0.1+w 0.3 w h]);
trisurf(surf_lh.tri,surf_lh.coord(1,:),surf_lh.coord(2,:),surf_lh.coord(3,:),...
    double(data(vl)),'EdgeColor','none');
view(90,0); 
% view(90,-90)
daspect([1 1 1]); axis tight; camlight; axis vis3d off;
lighting phong; material dull; shading flat;

a(3)=axes('position',[0.1+2*w 0.3 w h]);
trisurf(surf_rh.tri,surf_rh.coord(1,:),surf_rh.coord(2,:),surf_rh.coord(3,:),...
    double(data(vr)),'EdgeColor','none');
view(-90,0); 
% view(-90,-90)
daspect([1 1 1]); axis tight; camlight; axis vis3d off;
lighting phong; material dull; shading flat;

a(4)=axes('position',[0.1+3*w 0.3 w h]);
trisurf(surf_rh.tri,surf_rh.coord(1,:),surf_rh.coord(2,:),surf_rh.coord(3,:),...
    double(data(vr)),'EdgeColor','none');
view(90,0);
% view(0,90);
daspect([1 1 1]); axis tight; camlight; axis vis3d off;
lighting phong; material dull; shading flat;


for i=1:length(a)
    set(a(i),'CLim',clim);
    set(a(i),'Tag',['SurfStatView ' num2str(i)]);
end


cb=colorbar('location','South');
set(cb,'Position',[0.35 0.18 0.3 0.03]);
set(cb,'XAxisLocation','bottom');
h=get(cb,'Title');
set(h,'String', in.label_text);

whitebg(gcf, in.background);
set(gcf,'Color', in.background, 'InvertHardcopy', 'off');

dcm_obj=datacursormode(gcf);
set(dcm_obj,'UpdateFcn',@SurfStatDataCursor,'DisplayStyle','window');

%% set colorbar range 
colorbar_range(in.color_range);

%% set colormaps 
enigma_colormap(in.cmap);

return
end
