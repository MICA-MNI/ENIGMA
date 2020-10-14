function Z = zscore_matrix(data, group, controlCode)
%
% Usage:
%   Z = zscore_matrix(data, group, controlCode)
%
% Description:
%   Z-score data relative to a given group (author: @saratheriver)
%
% Inputs:
%   data (double array) - Data matrix (e.g., thickness data), 
%       size = [n_subject x n_region] group (double array) - Vector of 
%       values for group assignment (e.g, [0 0 0 1 1 1], same length as 
%       n_subject. controlCode (int) - Value that corresponds to 
%       "baseline" group.
%
% Outputs:
%   Z (doule array) - Z-scored data relative to control code   
%
% Sara Lariviere  |  saratheriver@gmail.com

data_orig = data;
if istable(data_orig)
    data = table2array(data);
else
    data = data_orig;
end

if isstring(controlCode)
    C = strcmp(group, controlCode); 
elseif isreal(controlCode)
    C = find(group == controlCode);
end

n = length(group);
Z = (data - repmat(mean(data(C, :), 1), n, 1)) ...
    ./ std(data(C, :));

if istable(data_orig)
    Z  = array2table(Z, 'VariableNames', data_orig.Properties.VariableNames);
end

return