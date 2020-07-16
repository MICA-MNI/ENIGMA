function [parceldata parcelstd] = Bo_surfData2parcelData(surfdata, surfparcel)
% function [parceldata parcelstd] = Bo_surfData2parcelData(surfdata, surfparcel)
% computes means in each of the parcels and writes out a new matrix
% 
% input:    surfdata   = k * v surface data (k subjects, v vertices) 
%           surfparcel = 1 * v surface parcellation (u unique labels)
% output:   parceldata = k * u parcel mean matrix 
%           parcelstd  = k * u parcel variance matrix
% 
% author:   boris@bic.mni.mcgill.ca
% date:     October 2017
% version:  1

uparcel         = unique(surfparcel); 
parceldata      = zeros(size(surfdata,1),length(uparcel)); 
parcelstd      = zeros(size(surfdata,1),length(uparcel)); 

for i = 1:length(uparcel) 
    thisparcel      = uparcel(i); 
    parceldata(:,i) = mean(surfdata(:,surfparcel==thisparcel),2);
    parcelstd(:,i) = std(surfdata(:,surfparcel==thisparcel),0,2);
end
    