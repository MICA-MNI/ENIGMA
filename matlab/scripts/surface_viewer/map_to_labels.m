function map2surf = map_to_labels(parcel_data, parcellation)
%
% map2surf = map_to_labels(parcel_data, parcellation)
%
% INPUTS
%   parcel_data  = p x 1 parcel vector (e.g., if Desikan Killiany from ENIGMA data, then 68 x 1)
%   parcellation = 'aparc_fsa5.csv' (default)
%
% OUTPUTS
%   maps a 1 x p parcellation vector to a 1 x m surface vector 
%
% author: boris@bic.mni.mcgill.ca
%
% Last modifications
% SL  |  July July July 2020 


if nargin < 2
    parcellation = 'aparc_fsa5.csv';
end

if any(size(parcel_data) == 68)
    a_idx                 = [2:1:4 6:1:39 41:1:71];     % indices of parcels included in ENIGMA
    data_DK               = zeros(71, 1);               
    data_DK(a_idx)        = parcel_data; 
else
    data_DK               = parcel_data;
end

% load surfaces
if contains(parcellation, 'fsa5')
    surf         = SurfStatAvSurf({'fsa5_lh', 'fsa5_rh'});
elseif contains(parcellation, 'conte69')
    surf         = SurfStatAvSurf({'conte69_lh', 'conte69_rh'});
end

% load label vector
label_vector     = dlmread(parcellation); 

% map data to surface
map2surf         = zeros(1,size(surf.coord,2)); 
uparcel          = unique(label_vector);
for ii=1:length(uparcel)
    index           = label_vector==uparcel(ii);
    map2surf(index) = data_DK(ii); 
end

