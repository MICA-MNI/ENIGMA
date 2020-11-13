function data_r = reorder_sctx(data)
%
% Usage:
%   data_r = reorder_sctx(data)
%
% Description:
%   Re-order subcortical volume data alphabetically and by hemisphere (left then right; author: @saratheriver)
%
% Inputs:
%   data (table) - Data matrix
%
% Outputs:
%   data_r (table) - Re-ordered data
%
% Sara Lariviere  |  saratheriver@gmail.com

    if size(data, 2) == 18;
        new_order    = [1, 16, 14, 6, 12, 10, 8, 4, 2, 17, 15, 7, 13, 11, 9, 5, 3, 18];
        data_r       = data(:, new_order);
        
    elseif size(data, 2) == 16;
        new_order        = [15, 13, 5, 11, 9, 7, 3, 1, 16, 14, 6, 12, 10, 8, 4, 2];
        data_r           = data(:, new_order);
        
    end
    
return