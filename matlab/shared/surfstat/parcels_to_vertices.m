function map2surf = parcels_to_vertices(parcel_data, surface_name)
%
% map2surf = parcels_to_vertices(parcel_vector, surface, label_vector)
%
% INPUTS
%   p x 1 parcel vector (e.g., if Desikan Killiany, then 71 x 1)
%   m x 1 label vector (with p unique elements) 
%   surface_name = 'fsa5' (default) or 'conte69'
%
% OUTPUTS
%   maps a 1 x p parcellation vector to a 1 x m surface vector 
%
% author: boris@bic.mni.mcgill.ca
%
% Last modifications
% SL  |  July July July 2020 

if nargin < 2
    surface_name = 'fsa5';
end

% load surfaces
if strcmp(surface_name, 'fsa5')
    surf         = SurfStatAvSurf({'fsa5_lh', 'fsa5_rh'});
    label_vector = dlmread('aparc_fsa5.csv'); 
elseif strcmp(surface_name, 'conte69')
    surf = SurfStatAvSurf({'conte69_lh', 'conte69_rh'});
    label_vector = dlmread('aparc_conte69.csv'); 
end

map2surf = zeros(1,size(surf.coord,2)); 
uparcel = unique(label_vector);
for i=1:length(uparcel)
    index = label_vector==uparcel(i);
    map2surf(index) = parcel_data(i); 
end

