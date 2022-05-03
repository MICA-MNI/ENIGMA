function parcel2surf = parcel_to_surface(parcel_data, parcellation, fill)
%
% Usage:
%   parcel2surf = parcel_to_surface(parcel_data, parcellation, fill)
%
% Description:
%   Map parcellated data to the surface (authors : @MICA-MNI, @saratheriver)
%
% Inputs:
%   parcel_data (double array) - Parcel vector, size = [p x 1]. For example, 
%       if Desikan Killiany from ENIGMA data, then parcel_data is size = [68 x 1].
%   parcellation (string, optional) - Default is 'aparc_fsa5'.
%   fill (double, optional) - Value for mask. Default is 0.
%
% Outputs
%   parcel2surf (double array) - Vector of values mapped from a parcellation 
%       to the surface
%
%
% Sara Lariviere  |  saratheriver@gmail.com

if nargin < 2
    parcellation = 'aparc_fsa5';
end
if nargin < 3
    fill = 0;
end

% transpose if data across columns
if size(parcel_data, 2) > size(parcel_data, 1)
    parcel_data = parcel_data.';
end

if contains(parcellation, 'aparc') && any(size(parcel_data) == 68)
    a_idx                 = [2:1:4 6:1:39 41:1:71];     % indices of parcels included in ENIGMA
    data_DK               = ones(71, 1) * fill;               
    data_DK(a_idx)        = parcel_data; 
elseif contains(parcellation, 'schaefer') && mod(max(size(parcel_data)), 100) == 0
    data_DK               = [fill; parcel_data];    % add mask
elseif contains(parcellation, 'glasser') && mod(max(size(parcel_data)), 10) == 0
    data_DK               = [fill; parcel_data];    % add mask
elseif contains(parcellation, 'vosdewael') && mod(max(size(parcel_data)), 10) == 0
    data_DK               = [fill; parcel_data];    % add mask
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
label_vector     = dlmread([parcellation '.csv']); 

% map data to surface
parcel2surf      = zeros(1,size(surf.coord,2)); 
uparcel          = unique(label_vector);
for ii=1:length(uparcel)
    index              = label_vector==uparcel(ii);
    parcel2surf(index) = data_DK(ii); 
end

