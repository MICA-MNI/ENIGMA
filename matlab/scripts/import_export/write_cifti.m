function write_cifti(data, varargin)
%
% Usage:
%   write_cifti(data, varargin)
%
% Description:
%   Writes cifti file (authors: @NicoleEic, @saratheriver)  
%
% Inputs:
%   data (single or double) - Data to be saved
%
% Name/value pairs:
%   dpath (string, optional) - Path to location for saving file 
%       (e.g., '/Users/bonjour/'). Default is ''.
%   fname (string, optional) - Name of file 
%       (e.g., 'ello.dscalar.nii'). Default is ''.
%   surface_name (string, optional) - Surface name {'fsa5', 'conte69'}. 
%       Default is 'conte69'.
%   hemi (string, optional) - Name of hemisphere {'lh', 'rh'}. 
%       Default is 'lh'.  
%
% Sara Lariviere  |  saratheriver@gmail.com

p = inputParser;
addParameter(p, 'dpath', '', @ischar);
addParameter(p, 'fname', '', @ischar);
addParameter(p, 'surface_name', 'conte69', @ischar);
addParameter(p, 'hemi', 'lh', @ischar);

% Parse the input
parse(p, varargin{:});
in = p.Results;

% Load reference file
cifti = cifti_read([in.hemi, '.', in.surface_name, '_ref.dscalar.nii']);

% Create new cifti image
cifti.cdata = data;
cifti.diminfo{2} = cifti_diminfo_make_scalars(size(data, 2));
cifti_write(cifti, [in.dpath, in.fname]);

disp(['file saved as: ' in.dpath in.fname ' ... #yolo'])

return