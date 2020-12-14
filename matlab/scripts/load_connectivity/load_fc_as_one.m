function [funcMatrix, funcLabels] = load_fc_as_one(parcellation)
%
% Usage: 
%   [funcMatrix_ctx, funcLabels_ctx] = load_fc_as_one(parcellation)
%
% Description:
%   Load functional connectivity data (cortical + subcortical in one matrix) 
%       (author: @saratheriver)
%
% Inputs:
%   parcellation (string, optional) - Name of parcellation (with n cortical parcels). Default is
%   'aparc'. Other options are 'schaefer_100', 'schaefer_200', 'schaefer_300',
%   'schaefer_400'.
%
% Outputs:
%   funcMatrix (double array) - Functional connectivity, size = [n+14 x n+14]
%   funcLabels (cell array) - Region labels, size = [1 x n+14]
%
% Sara Lariviere  |  saratheriver@gmail.com

if nargin < 1 || strcmp(parcellation, 'aparc')
    fctmp = load('hcp_functional_data_with_sctx.mat');

    funcMatrix   = fctmp.fc.funcMatrix;
    funcLabels   = fctmp.fc.funcLabels;
else
    fctmp = load(['hcp_functional_data_' parcellation '_with_sctx.mat']);

    funcMatrix   = fctmp.fc.funcMatrix;
    funcLabels   = fctmp.fc.funcLabels;
    
end

return