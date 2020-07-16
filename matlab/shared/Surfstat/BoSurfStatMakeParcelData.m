function map2surf = BoSurfStatMakeParcelData(mapOnParcel, S, parcel)
% map2surf = BoSurfStatMakeParcelData(mapOnParcel, S, parcel)
% makes a surfacefile with 1 x v points from a 1 x p parcellation data, 
% needs to supply a 1 x p surface parcellation (with p unique elements) 
%
% author: boris@bic.mni.mcgill.ca

map2surf = zeros(1,size(S.coord,2)); 
uparcel = unique(parcel);
for i=1:length(uparcel)
    index = parcel==uparcel(i);
    map2surf(index) = mapOnParcel(i); 
end

