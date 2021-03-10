function numfaces = nfaces(surface_name, hemisphere);
%
% Usage:
%   numfaces = nfaces(surface_name, hemisphere);
%
% Description:
%   Returns number of faces/triangles for a surface (author: @saratheriver)
%
% Inputs:
%   surface_name (string) - Name of surface {'fsa5', 'conte69'}
%   hemisphere (string) - Name of hemisphere {'lh', 'rh', 'both'}
%
% Outputs:
%   numfaces (double) - Number of faces/triangles
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