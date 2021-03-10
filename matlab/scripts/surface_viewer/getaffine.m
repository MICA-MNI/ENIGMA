function M = getaffine(surface_name, hemisphere);
%
% Usage:
%   M = getaffine(surface_name, hemisphere);
%
% Description:
%   Returns vox2ras transform for a surface (author: @saratheriver)
%
% Inputs:
%   surface_name (string) - Name of surface {'fsa5', 'conte69'}
%   hemisphere (string) - Name of hemisphere {'lh', 'rh', 'both'}
% Outputs:
%   M (double array) - [4, 4] vox2ras transform
%
% Sara Lariviere  |  saratheriver@gmail.com

if strcmp(hemisphere, 'conte69')
    if strcmp(hemisphere, 'lh') || strcmp(hemisphere, 'rh')
        M = [-1,0,0,16246;0,0,1,-0.500000000000000;0,-1,0,0.500000000000000;0,0,0,1];
    elseif strcmp(hemisphere, 'both')
        % M =
    end

elseif strcmp(hemisphere, 'fsa5')
    if strcmp(hemisphere, 'lh') || strcmp(hemisphere, 'rh')
        M = [-1,0,0,5121;0,0,1,-0.500000000000000;0,-1,0,0.500000000000000;0,0,0,1];
    elseif strcmp(hemisphere, 'both')
        % M =    
    end
    
end




return