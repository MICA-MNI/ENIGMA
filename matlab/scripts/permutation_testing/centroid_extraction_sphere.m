function centroid = centroid_extraction_sphere(sphere_coords, annotfile)
%
% Usage:
%   centroid = centroid_extraction_sphere(sphere_coords, annotfile)
%
% Description:
%   Extract centroids of a cortical parcellation on a surface sphere (authors: 
%       @frantisekvasa, @saratheriver)
%
% Inputs:
%   sphere_coords (double array) - Sphere coordinates, size = [n x 3]
%   annotfile (string) - Name of annotation file {'fsa5_lh_aparc.annot', 
%       'fsa5_rh_aparc.annot, 'fsa5_with_sctx_lh_aparc_aseg.csv', etc.}
%   ventricles (string, optional) - Whether ventricle data are present. 
%       Only used when 'annotfile' is fsa5_with_sctx_lh_aparc_aseg or 
%       fsa5_with_sctx_lh_aparc_aseg. Default is 'False'.
%
% Outputs:
%   coord (double array) - Coordinates of the centroid of each region on the sphere, size = [m x 3].
%
% References:
%   Alexander-Bloch A, Shou H, Liu S, Satterthwaite TD, Glahn DC, Shinohara RT, 
%       Vandekar SN and Raznahan A (2018). On testing for spatial correspondence 
%       between maps of human brain structure and function. NeuroImage, 178:540-51.
%   Vása F, Seidlitz J, Romero-Garcia R, Whitaker KJ, Rosenthal G, Vértes PE, 
%       Shinn M, Alexander-Bloch A, Fonagy P, Dolan RJ, Goodyer IM, the NSPN 
%       consortium, Sporns O, Bullmore ET (2017). Adolescent tuning of association 
%       cortex in human structural brain networks. Cerebral Cortex, 28(1):281?294.
%
% Sara Lariviere  |  saratheriver@gmail.com

% for cortical annotation files only
if ~contains(annotfile, 'aparc_aseg')
    [~, label_annot, colortable] = read_annotation(annotfile);                       % read in parcel membership of vertices

    ind = 0;                                                                         % iteration counter
    centroid = [];                                                                   % initialisation of centroid array
    for ic = 1:colortable.numEntries                                                 % loop over parcellated structures
        if isempty(strfind(colortable.struct_names{ic},'unknown')) && ...
           isempty(strfind(colortable.struct_names{ic},'corpus')) && ...
           isempty(strfind(colortable.struct_names{ic},'corpuscallosum')) && ...
           isempty(strfind(colortable.struct_names{ic},'medialwall')) && ...
           isempty(strfind(colortable.struct_names{ic},'Background+FreeSurfer_Defined_Medial_Wall')) % exclude "unknown" structures and corpus callosum from the parcellation 
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
