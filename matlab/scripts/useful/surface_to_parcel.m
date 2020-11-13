function surf2parcel = surface_to_parcel(surf_data, parcellation)
%
% Usage:
%   surf2parcel = surface_to_parcel(surf_data, parcellation)
%
% Description:
%   Map surface data to a parcellation (authors : @MICA-MNI, @saratheriver)
%
% Inputs:
%   surf_data (double array) - Surface vector, size = [v x 1].
%   parcellation (string, optional) - Default is 'aparc_fsa5'
%
% Outputs:
%   surf2parcel (double array) - Vector of values mapped from a surface 
%       to a parcellation     
%
% Sara Lariviere  |  saratheriver@gmail.com

if nargin < 2
    parcellation = 'aparc_fsa5';
end

% load label vector
label_vector     = dlmread([parcellation '.csv']); 

uparcel          = unique(label_vector); 
surf2parcel      = zeros(size(surf_data, 1), length(uparcel)); 

for ii = 1:length(uparcel) 
    thisparcel          = uparcel(ii); 
    surf2parcel(:, ii)  = nanmean(surf_data(:, label_vector == thisparcel), 2);
end

end
