function [p_shuf, r_dist] = shuf_test(map1, map2, varargin)
%
% Usage:
%   [p_shuf, r_dist] = shuf_test(map1, map2, varargin)
%
% Description:
%   Shuf permuation (author: @saratheriver)  
%
% Inputs:
%   map1 (double array) - One of two map to be correlated
%   map2 (double array) - The other map to be correlated
%
% Name/value pairs:
%   n_rot (int, optional) - Number of spin rotations. Default is 1000.
%   type (string, optional) - Correlation type {'pearson', 'spearman'}. 
%       Default is 'pearson'.
%
% Outputs:
%   p_shuf (double) - Permutation p-value
%   r_dist (double array) - Null correlations, size = [n_rot*2 x 1].     
%
% Sara Lariviere  |  saratheriver@gmail.com


p = inputParser;
addParameter(p, 'n_rot', 1000, @isnumeric);
addParameter(p, 'type', 'pearson', @ischar);

% Parse the input
parse(p, varargin{:});
in = p.Results;

if size(map1, 1) == 1; map1 = map1.'; end
if size(map2, 1) == 1; map2 = map2.'; end

nroi = length(map1);
r = 0; c = 0; % count successful (r) and unsuccessful (c) iterations
perm_id = zeros(nroi, in.n_rot); % initialise output array

while (r < in.n_rot)
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
        disp(['permutation ' num2str(r) ' of ' num2str(in.n_rot)]); 
    end
end

    rho_emp = corr(map1, map2, 'type', in.type, 'rows', 'pairwise');     % empirical correlation
    
    % permutation of measures
    x_perm = zeros(nroi, in.n_rot);
    y_perm = zeros(nroi, in.n_rot);
    for r = 1:in.n_rot
        for i = 1:nroi
            x_perm(i, r) = map1(perm_id(i, r)); % permute x
            y_perm(i, r) = map2(perm_id(i, r)); % permute y
        end
    end

    % corrrelation to unpermuted measures
    rho_null_xy = zeros(in.n_rot, 1);
    rho_null_yx = zeros(in.n_rot, 1);
    for r = 1:in.n_rot
        rho_null_xy(r) = corr(x_perm(:, r), map2, 'type', in.type, 'rows', 'pairwise'); % correlate permuted x to unpermuted y
        rho_null_yx(r) = corr(y_perm(:, r), map1, 'type', in.type, 'rows', 'pairwise'); % correlate permuted y to unpermuted x
    end

    % p-value definition depends on the sign of the empirical correlation
    if rho_emp > 0
        p_perm_xy = sum(rho_null_xy > rho_emp)/in.n_rot;
        p_perm_yx = sum(rho_null_yx > rho_emp)/in.n_rot;
    else
        p_perm_xy = sum(rho_null_xy < rho_emp)/in.n_rot;
        p_perm_yx = sum(rho_null_yx < rho_emp)/in.n_rot;
    end
    
    % null distribution
    r_dist = [rho_null_xy; rho_null_yx];

    % average p-values
    p_shuf = (p_perm_xy + p_perm_yx)/2;

return