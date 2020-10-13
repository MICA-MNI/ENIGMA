function [p_spin, r_dist] = spin_test(map1, map2, varargin)

% spin_test(map1, map2, varargin);
% 
% Usage: p_spin = spin_test(map1, map2, varargin);
% 
% REQUIRED INPUTS
%   map1               = one of two maps to be correlated
%   map2               = the other map to be correlated
%
% OPTIONAL INPUTS
%   surface_name       = 'fsa5' (default) or 'conte69'
%   parcellation_name  = 'aparc' (default)', 'aparc_aseg' (ctx + sctx)
%   n_rot              = number of spin rotations (default 100)
%   type               = correlation type, 'pearson' (default), 'spearman'
%   ventricles         = 'False' (default), only for 'aparc_aseg'
%
% OUTPUTS
%   p_spin          = permutation p-value
%   r_dist          = distribution of shuffled correlations (number of spins * 2)
% 
%
% *** Only works for parcellations in fsaverage5 for now ***
%
% Functions at the bottom from here 
%       https://github.com/frantisekvasa/rotate_parcellation
%
% Last modifications:
% SL | a rainy September day 2020
% SL | a beautiful Fall day, October 2020

p = inputParser;
addParameter(p, 'surface_name', 'fsa5', @ischar);
addParameter(p, 'parcellation_name', 'aparc', @ischar);
addParameter(p, 'n_rot', 100, @isnumeric);
addParameter(p, 'type', 'pearson', @ischar);
addParameter(p, 'ventricles', 'False', @ischar);

% Parse the input
parse(p, varargin{:});
in = p.Results;

% load spheres
if strcmp(in.surface_name, 'fsa5')
    lsphere = SurfStatReadSurf1('fsa5_sphere_lh');
    rsphere = SurfStatReadSurf1('fsa5_sphere_rh');
    
elseif strcmp(in.surface_name, 'fsa5_with_sctx')
    lsphere = SurfStatReadSurf1('fsa5_with_sctx_sphere_lh');
    rsphere = SurfStatReadSurf1('fsa5_with_sctx_sphere_rh');
    
elseif strcmp(in.surface_name, 'conte69')
    error('Not yet implemented :/')
    lsphere = SurfStatReadSurf1('conte69_sphere_lh');
    rsphere = SurfStatReadSurf1('conte69_sphere_rh');
end


% 1 - get sphere coordinates of parcels
if strcmp(in.parcellation_name, 'aparc_aseg')
    lh_centroid = centroid_extraction_sphere(lsphere.coord.', [in.surface_name '_lh_' in.parcellation_name '.mat']);
    rh_centroid = centroid_extraction_sphere(rsphere.coord.', [in.surface_name '_lh_' in.parcellation_name '.mat']);
else
    lh_centroid = centroid_extraction_sphere(lsphere.coord.', [in.surface_name '_lh_' in.parcellation_name '.annot']);
    rh_centroid = centroid_extraction_sphere(rsphere.coord.', [in.surface_name '_rh_' in.parcellation_name '.annot']);
end

% 2 - Generate permutation maps
perm_id = rotate_parcellation(lh_centroid, rh_centroid, in.n_rot);

% 3 - Generate spin permutated p-value
if size(map1, 1) == 1; map1 = map1.'; end
if size(map2, 1) == 1; map2 = map2.'; end
[p_spin, r_dist] = perm_sphere_p(map1, map2, perm_id, in.type);

return

