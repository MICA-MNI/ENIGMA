function [p_shuf, r_dist] = shuf_test(map1, map2, n_rot, type)

% shuf_test(map1, map2, n_rot, type);
% 
% Usage: [p_shuf, r_dist] = spin_test(map1, map2, [n_rot, [type]]);
% 
% INPUTS
%    map1            = one of two subcortical map to be correlated
%    map2            = the other subcortical map to be correlated
%    n_rot           = number of shuffles (default 100)
%    type            = correlation type, 'pearson' (default), 'spearman'
% 
% OUTPUT
%    p_shuf          = permutation p-value
%    r_dist          = distribution of shuffled correlations (number of shuffles * 2)
% 
%  Sara Lariviere | a sunny September day 2020


if nargin<3
    n_rot=1000;
end
if nargin<4
    type='pearson';
end

if size(map1, 1) == 1; map1 = map1.'; end
if size(map2, 1) == 1; map2 = map2.'; end

nroi = length(map1);
r = 0; c = 0; % count successful (r) and unsuccessful (c) iterations
perm_id = zeros(nroi, n_rot); % initialise output array

while (r < n_rot)
    rot_lr_sort = randperm(nroi);
    
    % verify that permutation does not map to itself
    if ~all(rot_lr_sort==1:nroi)
        r = r+1;
        perm_id(:,r) = rot_lr_sort; % if it doesn't, store it
    else
        c = c+1;
        disp(['map to itself n.' num2str(c)])
    end
    
    % track progress
    if mod(r,100)==0; 
        disp(['permutation ' num2str(r) ' of ' num2str(n_rot)]); 
    end
end

    rho_emp = corr(map1, map2, 'type', type, 'rows', 'pairwise');     % empirical correlation
    
    % permutation of measures
    x_perm = zeros(nroi, n_rot);
    y_perm = zeros(nroi, n_rot);
    for r = 1:n_rot
        for i = 1:nroi
            x_perm(i, r) = map1(perm_id(i, r)); % permute x
            y_perm(i, r) = map2(perm_id(i, r)); % permute y
        end
    end

    % corrrelation to unpermuted measures
    rho_null_xy = zeros(n_rot, 1);
    rho_null_yx = zeros(n_rot, 1);
    for r = 1:n_rot
        rho_null_xy(r) = corr(x_perm(:, r), map2, 'type', type, 'rows', 'pairwise'); % correlate permuted x to unpermuted y
        rho_null_yx(r) = corr(y_perm(:, r), map1, 'type', type, 'rows', 'pairwise'); % correlate permuted y to unpermuted x
    end

    % p-value definition depends on the sign of the empirical correlation
    if rho_emp > 0
        p_perm_xy = sum(rho_null_xy > rho_emp)/n_rot;
        p_perm_yx = sum(rho_null_yx > rho_emp)/n_rot;
    else
        p_perm_xy = sum(rho_null_xy < rho_emp)/n_rot;
        p_perm_yx = sum(rho_null_yx < rho_emp)/n_rot;
    end
    
    % null distribution
    r_dist = [rho_null_xy; rho_null_yx];

    % average p-values
    p_shuf = (p_perm_xy + p_perm_yx)/2;

return