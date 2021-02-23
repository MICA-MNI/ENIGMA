function [p_spin, r_dist] = spin_test(map1, map2, varargin)
%
% Usage:
%   [p_spin, r_dist] = spin_test(map1, map2, varargin)
%
% Description:
%   Spin permutation (author: @saratheriver)   
%
% Inputs:
%   map1 (double array) - One of two map to be correlated
%   map2 (double array) - The other map to be correlated
%
% Name/value pairs:
%   Surface name (string, optional) - Surface name {'fsa5', 'fsa5_with_sctx'}. 
%       Use 'fsa5' for Conte69. Default is 'fsa5'.
%   parcellation_name (string, optional) - Parcellation name {'aparc', 
%       'aparc_aseg', 'schaefer_100', 'schaefer_200', 'schaefer_300', 
%       'schaefer_400', 'schaefer_500', 'schaefer_600', 'schaefer_700', 
%       'schaefer_800', 'schaefer_900', 'schaefer_1000'}. Default is 'aparc'.
%   n_rot (int, optional) - Number of spin rotations. Default is 1000.
%   type (string, optional) - Correlation type {'pearson', 'spearman'}. 
%       Default is 'pearson'.
%   ventricles (string, optional) - Whether ventricles are present in map1, 
%       map2. Only used when parcellation_name is 'aparc_aseg'. Default 
%       is 'False' (other option is 'True').
%
% Outputs:
%   p_spin (double) - Permutation p-value
%   r_dist (double array) - Null correlations, size = [n_rot*2 x 1].     
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


p = inputParser;
addParameter(p, 'surface_name', 'fsa5', @ischar);
addParameter(p, 'parcellation_name', 'aparc', @ischar);
addParameter(p, 'n_rot', 1000, @isnumeric);
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

