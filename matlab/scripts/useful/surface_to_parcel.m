function surf2parcel = surface_to_parcel(surf_data, parcellation)
% 

if nargin < 2
    parcellation = 'aparc_fsa5';
end

% load label vector
label_vector     = dlmread([parcellation '.csv']); 

uparcel          = unique(label_vector); 
surf2parcel      = zeros(size(surf_data, 1), length(uparcel)); 

for ii = 1:length(uparcel) 
    thisparcel          = uparcel(ii); 
    surf2parcel(:, ii)  = mean(surf_data(:, label_vector == thisparcel), 2);
end

end
