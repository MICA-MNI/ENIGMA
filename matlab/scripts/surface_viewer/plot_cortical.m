function [a, cb] = plot_cortical(data, varargin);
%
% Usage:
%   [a, cb] = plot_cortical(data, varargin);   
%
% Description:
%   Plot cortical surface with lateral and medial views (authors: @MICA-MNI, @saratheriver)
%
% Inputs:
%   data (double array) - vector of data, size = [1 x v]
%
% Name/value pairs:
%   surface_name (string, optional) - Name of surface {'fsa', 'fsa5', 'conte69}. 
%       Default is 'fsa5'.
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
addParameter(p, 'surface_name', 'fsa5', @ischar);
addParameter(p, 'label_text', "", @ischar);
addParameter(p, 'background', 'white', @ischar);
addParameter(p, 'color_range', [min(data) max(data)], @isnumeric);
addParameter(p, 'cmap', 'RdBu_r', @ischar);

% Parse the input
parse(p, varargin{:});
in = p.Results;

% load surfaces
if strcmp(in.surface_name, 'fsa5')
    surf = SurfStatAvSurf({'fsa5_lh', 'fsa5_rh'});
elseif strcmp(in.surface_name, 'fsa')
    surf = SurfStatAvSurf({'fsa_lh', 'fsa_rh'});
elseif strcmp(in.surface_name, 'conte69')
    surf = SurfStatAvSurf({'conte69_lh', 'conte69_rh'});
elseif strcmp(in.surface_name, 'ss')
    surf = SurfStatAvSurf({'fsa5_with_sctx_sphere_lh', 'fsa5_with_sctx_sphere_lh'});
end

v=length(data);
vl=1:(v/2);
vr=vl+v/2;
t=size(surf.tri,1);
tl=1:(t/2);
tr=tl+t/2;
clim=[min(data),max(data)];
if clim(1)==clim(2)
    clim=clim(1)+[-1 0];
end


h=0.25;
w=0.20;

a(1)=axes('position',[0.1 0.3 w h]);
trisurf(surf.tri(tl,:),surf.coord(1,vl),surf.coord(2,vl),surf.coord(3,vl),...
    double(data(vl)),'EdgeColor','none');
view(-90,0)
daspect([1 1 1]); axis tight; camlight; axis vis3d off;
lighting phong; material dull; shading flat;

a(2)=axes('position',[0.1+w 0.3 w h]);
trisurf(surf.tri(tl,:),surf.coord(1,vl),surf.coord(2,vl),surf.coord(3,vl),...
    double(data(vl)),'EdgeColor','none');
view(90,0); 
daspect([1 1 1]); axis tight; camlight; axis vis3d off;
lighting phong; material dull; shading flat;

a(3)=axes('position',[0.1+2*w 0.3 w h]);
trisurf(surf.tri(tr,:)-v/2,surf.coord(1,vr),surf.coord(2,vr),surf.coord(3,vr),...
    double(data(vr)),'EdgeColor','none');
view(-90,0); 
daspect([1 1 1]); axis tight; camlight; axis vis3d off;
lighting phong; material dull; shading flat;

a(4)=axes('position',[0.1+3*w 0.3 w h]);
trisurf(surf.tri(tr,:)-v/2,surf.coord(1,vr),surf.coord(2,vr),surf.coord(3,vr),...
    double(data(vr)),'EdgeColor','none');
view(90,0);
daspect([1 1 1]); axis tight; camlight; axis vis3d off;
lighting phong; material dull; shading flat;


for i=1:length(a)
    set(a(i),'CLim',clim);
    set(a(i),'Tag',['SurfStatView ' num2str(i) ]);
end


cb=colorbar('location','South');
set(cb,'Position',[0.35 0.18 0.3 0.03]);
set(cb,'XAxisLocation','bottom');
h=get(cb,'Title');
set(h,'String', in.label_text);

whitebg(gcf, in.background);
set(gcf,'Color', in.background, 'InvertHardcopy', 'off');

dcm_obj = datacursormode(gcf);
set(dcm_obj, 'UpdateFcn', @SurfStatDataCursor, 'DisplayStyle', 'window');

%% set colorbar range 
colorbar_range(in.color_range);

%% set colormaps 
enigma_colormap(in.cmap);

return
end
