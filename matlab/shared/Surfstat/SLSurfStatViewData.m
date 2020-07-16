function [a,cb]=BoSurfStatViewData(data,surf,title,background);

%BoSurfStatViewData is a simple viewer for surface data.
% 
% Usage: [a,cb]=BoSurfStatViewData(data, surf [,title [,background]]);
% 
% data        = 1 x v vector of data, v=#vertices
% surf.coord  = 3 x v matrix of coordinates.
% surf.tri    = 3 x t matrix of triangle indices, 1-based, t=#triangles.
% title       = any string, data name by default.
% background  = background colour, any matlab ColorSpec, such as 
%   'white' (default), 'black'=='k', 'r'==[1 0 0], [1 0.4 0.6] (pink) etc.
%   Letter and line colours are inverted if background is dark (mean<0.5).
%
% a  = vector of handles to the axes, left to right, top to bottom. 
% cb = handle to the colorbar.

if nargin<3 
    title=inputname(1);
end
if nargin<4
    background='white';
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
% view(0,90);
view(-90,0)
daspect([1 1 1]); axis tight; camlight; axis vis3d off;
lighting phong; material dull; shading flat;

a(2)=axes('position',[0.1+w 0.3 w h]);
trisurf(surf.tri(tl,:),surf.coord(1,vl),surf.coord(2,vl),surf.coord(3,vl),...
    double(data(vl)),'EdgeColor','none');
view(90,0); 
% view(90,-90)
daspect([1 1 1]); axis tight; camlight; axis vis3d off;
lighting phong; material dull; shading flat;

a(3)=axes('position',[0.1+2*w 0.3 w h]);
trisurf(surf.tri(tr,:)-v/2,surf.coord(1,vr),surf.coord(2,vr),surf.coord(3,vr),...
    double(data(vr)),'EdgeColor','none');
view(-90,0); 
% view(-90,-90)
daspect([1 1 1]); axis tight; camlight; axis vis3d off;
lighting phong; material dull; shading flat;

a(4)=axes('position',[0.1+3*w 0.3 w h]);
trisurf(surf.tri(tr,:)-v/2,surf.coord(1,vr),surf.coord(2,vr),surf.coord(3,vr),...
    double(data(vr)),'EdgeColor','none');
view(90,0);
% view(0,90);
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
% matlab original (boring)
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% colormap([.7 .7 .7; parula(256)])

% colorbrewer 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% colormap(brewermap(256,'*PuBuGn'))
% colormap(brewermap(256,'*PuBu'))
% colormap(brewermap(256,'*BuPu'))
% colormap(brewermap(256,'OrRd'))
% colormap(brewermap(500,'Blues'))
% colormap(brewermap(256,'RdBu'))

% my own creations
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% yellowCmap=[linspace(1,1,256)',linspace(.98,.82,256)',linspace(.94,0,256)'];
% colormap(yellowCmap);
% redCmap=[linspace(1,.65,256)',linspace(.98,0.0588,256)',linspace(.94,0.0824,256)'];
% colormap(redCmap);
% tealCmap=[.88 .88 .88; 0 .7 .7; 165/255 29/255 0; 0 0 0];
% colormap(tealCmap)
% grayCmap=[.88 .88 .88];
% colormap(grayCmap)
% topBot=[.9 .9 .9; 1 .82 0; .9 .9 .9; .03 .19 .42 ];
% colormap(topBot);
% topBot=[.9 .9 .9; 0.0300    0.1900    0.4200];
% colormap(topBot);
% grayish2redCmap=[linspace(247,103,256)',linspace(247,0,256)',linspace(247,31,256)'];
% grayish2redCmap=grayish2redCmap/255;
% colormap(grayish2redCmap);
% grayish2blueCmap=[linspace(247,5,256)',linspace(247,48,256)',linspace(247,97,256)'];
% grayish2blueCmap=grayish2blueCmap/255;
% colormap(grayish2blueCmap);
% teal2gray = [linspace(78,245,128)',linspace(178,245,128)',linspace(210,245,128)'];
% gray2salmon = [linspace(245,178,128)',linspace(245,24,128)',linspace(245,43,128)'];
% teal2salmon = [teal2gray; gray2salmon];
% teal2salmon=teal2salmon/255;
% colormap(teal2salmon);
cmap      = brewermap(256,'RdGy');
cmap_inv  = 1-brewermap(256,'*RdGy');
newmap    = [cmap_inv(1:end/2,:); cmap_inv(end/2+1:end,:)]; 
colormap([1 1 1; flipud(newmap)]);
blueGhost = newmap;


% viridis
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% cm_plasma=plasma(500);
% colormap(cm_plasma);
% cm_inferno=inferno(500);
% colormap(cm_inferno); 
% cm_fake_parula=fake_parula(500);
% colormap(cm_fake_parula); 
% cm_viridis=viridis(500);
% colormap([.9 .9 .9; cm_viridis]); 
% colormap(cm_viridis); 

return
end
