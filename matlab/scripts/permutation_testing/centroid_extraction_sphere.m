function centroid = centroid_extraction_sphere(sphere_coords, annotfile)
% Function to extract centroids of a cortical parcellation on the
% Freesurfer sphere, for subsequent input to code for the performance of a
% spherical permutation. Runs on individual hemispheres.
%
% Inputs:
% sphere_coords   sphere coordinates (n x 3)
% annot_file      e.g., 'fsa5_lh_aparc.annot' (string)
%
% Output:
% centroid      coordinates of the centroid of each region on the sphere
%
% Rafael Romero-Garcia, 2017
% Modified by Sara Lariviere (for ENIGMA), September 2020

% for cortical annotation files only
if ~contains(annotfile, 'aparc_aseg')
    [~, label_annot, colortable] = read_annotation(annotfile);                       % read in parcel membership of vertices

    ind = 0;                                                                         % iteration counter
    centroid = [];                                                                   % initialisation of centroid array
    for ic = 1:colortable.numEntries                                                 % loop over parcellated structures
        if isempty(strfind(colortable.struct_names{ic},'unknown')) && ...
           isempty(strfind(colortable.struct_names{ic},'corpus'))                    % exclude "unknown" structures and corpus callosum from the parcellation 
            ind = ind + 1;                                                           % increment counter for every valid region
            label = colortable.table(ic,5);                                          % ID of current parcel
            centroid(ind,:) = mean(sphere_coords(label_annot == label, :));          % average coordinates of all vertices within the current parcel to generate the centroid
        end
    end

% for combined cortical and subcortical
elseif contains(annotfile, 'aparc_aseg')
    annot_sctx = load(annotfile);
  
    ind = 0;                                                                         
    centroid = [];     
    for ic = 1:length(annot_sctx.label)
        if isempty(strfind(annot_sctx.structure{ic},'unknown')) && ...
           isempty(strfind(annot_sctx.structure{ic},'corpus')) && ...
           isempty(strfind(annot_sctx.structure{ic}, 'vent'))                   
            ind = ind + 1;                                                         
            label = annot_sctx.label(ic);                                          
            centroid(ind,:) = mean(sphere_coords(annot_sctx.label_annot == label, :));          
        end
    end
end

return
