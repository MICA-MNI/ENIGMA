function p_shuf = shuf_test(map1, map2, n_rot, type)

% shuf_test(map1, map2, n_rot, type);
% 
% Usage: p_shuf = spin_test(map1, map2, [n_rot, [type]]);
% 
% INPUTS
%    map1            = one of two subcortical map to be correlated
%    map2            = the other subcortical map to be correlated
%    n_rot           = number of shuffles (default 100)
%    type            = correlation type, 'pearson' (default), 'spearman'
% 
% OUTPUT
%    p_shuf          = permutation p-value
% 
%  Sara Lariviere | a sunny September day 2020


if nargin<3
    n_rot=1000;
end
if nargin<4
    type='pearson';
end

one                    = dctmps;
two                    = tval_tle_sctx; 

nperm                  = 10000;
shufidx                = zeros(nperm, size(one, 2));
for ii = 1:nperm
    tmpshuf             = randperm(size(one, 2));
    shufidx(ii, :)      = one([tmpshuf]);
end

[r_orig, pval_orig]    = corrcoef(dctmps, tval_tle_sctx, 'rows', 'pairwise');
[r_spin, pval_spin]    = corr(one.', shufidx.', 'rows', 'pairwise');
n_sig                  = length(find(abs(r_spin) > abs(r_orig(1,2))));
n_sig/nperm

return