function [p_perm, null_dist] = perm_sphere_p(x, y, perm_id, corr_type)
%
% Usage:
%   [p_perm, null_dist] = perm_sphere_p(x, y, perm_id, corr_type)
%
% Description:
%   Generate a p-value for the spatial correlation between two parcellated
%       cortical surface maps (authors: @frantisekvasa, @saratheriver)
%
% Inputs:
%   x (double array) - One of two map to be correlated
%   y (double array) - The other map to be correlated
%   perm_id (double array) - Array of permutations, size = [m x nrot]  
%   corr_type (string, optional) - Correlation type {'pearson', 'spearman'}. 
%       Default is 'pearson'.
%
% Outputs:
%   p_perm (double) - Permutation p-value
%   null_dist (double array) - Null correlations, size = [n_rot*2 x 1].
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

% default correlation
if nargin < 4
    corr_type = 'pearson';
end

nroi = size(perm_id,1);  % number of regions
nperm = size(perm_id,2); % number of permutations

rho_emp = corr(x, y, 'type', corr_type, 'rows', 'pairwise');     % empirical correlation

% permutation of measures
x_perm = zeros(nroi,nperm);
y_perm = zeros(nroi,nperm);
for r = 1:nperm
    for i = 1:nroi
        x_perm(i,r) = x(perm_id(i,r)); % permute x
        y_perm(i,r) = y(perm_id(i,r)); % permute y
    end
end

% corrrelation to unpermuted measures
rho_null_xy = zeros(nperm,1);
for r = 1:nperm
    rho_null_xy(r) = corr(x_perm(:,r), y, 'type', corr_type, 'rows', 'pairwise'); % correlate permuted x to unpermuted y
    rho_null_yx(r) = corr(y_perm(:,r), x, 'type', corr_type, 'rows', 'pairwise'); % correlate permuted y to unpermuted x
end

% p-value definition depends on the sign of the empirical correlation
if rho_emp > 0
    p_perm_xy = sum(rho_null_xy > rho_emp)/nperm;
    p_perm_yx = sum(rho_null_yx > rho_emp)/nperm;
else
    p_perm_xy = sum(rho_null_xy < rho_emp)/nperm;
    p_perm_yx = sum(rho_null_yx < rho_emp)/nperm;
end

% null distributions
null_dist = [rho_null_xy; rho_null_yx.'];

% average p-values
p_perm = (p_perm_xy + p_perm_yx)/2;

% print(['p = ' num2str(sum(rho.null>rho.emp)/nperm)])

return
