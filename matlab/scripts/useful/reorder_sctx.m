function data_r = reorder_sctx(data)
%
% Usage: data_r = reorder_sctx(data)
%
% Re-orders subcortical volume data alphabetically, and by hemisphere (left, then right)
%
%   Input:
%      data         = data matrix (e.g. metr1_SubVol)
%
%   Output:
%       data_r      = re-ordered data (L-acc, L-amyg, L-caud, L-hip ... R-thalamus, R-ventricle)
%
%
% Sara Lariviere  |  saratheriver@gmail.com
%
% Last modifications:
% SL | August 2020 (watching NHL playoffs (CBJ-TBL) ... one of the longest matches ever!
%      Fo' real... they're in 8th period... cray cray)
%           Update 1: TBL won 3-2
%           Update 2: That was the 4th longest NHL match ever!
%           Update 3: The losing goalie made 85 saves!!! That's an all-time NHL record!!!

    if size(data, 2) == 18;
        new_order    = [1, 16, 14, 6, 12, 10, 8, 4, 2, 17, 15, 7, 13, 11, 9, 5, 3, 18];
        data_r       = data(:, new_order);
        
    elseif size(data, 2) == 16;
        new_order        = [15, 13, 5, 11, 9, 7, 3, 1, 16, 14, 6, 12, 10, 8, 4, 2];
        data_r           = data(:, new_order);
        
    end

return