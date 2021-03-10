function numfaces = nfaces(surface_name, hemisphere);
%
% Usage:
%   numfaces = numfaces(surface_name);
%
% Description:
%   Returns number of faces/triangles for a surface (authors: @MICA-MNI, @saratheriver)
%
% Inputs:
%   surface_name (string) - Name of surface {'fsa5', 'conte69'}
%   hemisphere (string) - Name of hemispherer {'lh', 'rh', 'both'}
% Outputs:
%   numfaces (double) - number of faces/triangles
%
% Sara Lariviere  |  saratheriver@gmail.com

if strcmp(hemisphere, 'lh')
    numfaces = SurfStatReadSurf([surface_name '_lh']);
    numfaces = size(numfaces.tri, 1);
elseif strcmp(hemisphere, 'rh')
    numfaces = SurfStatReadSurf([surface_name '_lh']);
    numfaces = size(numfaces.tri, 1);
elseif strcmp(hemisphere, 'both')
    numfaces = SurfStatAvSurf({[surface_name '_lh'], [surface_name '_rh']});
    numfaces = size(numfaces.tri, 1);
end

return