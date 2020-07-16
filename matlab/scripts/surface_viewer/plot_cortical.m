function [a,cb]=plot_cortical(data, surface_name, title, background);

% plot_cortical(data, surf, title, background);
% 
% Usage: [a,cb] = plot_cortical(data, surf[, title[, background]]);
% 
% data            = 1 x v vector of data, v=#vertices
% surface_name    = 'fsa5' (default) or 'conte69'
% title           = any string, data name by default.
% background      = background colour, any matlab ColorSpec, such as 
%   'white' (default), 'black'=='k', 'r'==[1 0 0], [1 0.4 0.6] (pink) etc.
%   Letter and line colours are inverted if background is dark (mean<0.5).
%
% a  = vector of handles to the axes, left to right, top to bottom. 
% cb = handle to the colorbar.
%
% Sara Lariviere  |  saratheriver@gmail.com
%
% Last modifications:
% SL | a humid July day 2020

if nargin<2
    surface_name = 'fsa5';
end
if nargin<3 
    title=inputname(1);
end
if nargin<4
    background='white';
end

% load surfaces
if strcmp(surface_name, 'fsa5')
    surf = SurfStatAvSurf({'fsa5_lh', 'fsa5_rh'});
elseif strcmp(surface_name, 'conte69')
    surf = SurfStatAvSurf({'conte69_lh', 'conte69_rh'});
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

% clf;
colormap(spectral(256));


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
set(h,'String',title);

whitebg(gcf,background);
set(gcf,'Color',background,'InvertHardcopy','off');

dcm_obj=datacursormode(gcf);
set(dcm_obj,'UpdateFcn',@SurfStatDataCursor,'DisplayStyle','window');

%% colormaps 
colormap(viridis)

return
end
