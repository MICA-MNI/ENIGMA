function [strucMatrix, strucLabels] = load_sc_as_one(parcellation)
%
% Usage: 
%   [strucMatrix_ctx, strucLabels_ctx] = load_sc_as_one(parcellation)
%
% Description:
%   Load structural connectivity data (cortical + subcortical in one matrix) 
%       (author: @saratheriver)
%
% Inputs:
%   parcellation (string, optional) - Name of parcellation (with n cortical parcels). Default is
%   'aparc'. Other options are 'schaefer_100', 'schaefer_200', 'schaefer_300',
%   'schaefer_400'.
%
% Outputs:
%   strucMatrix (double array) - Structural connectivity, size = [n+14 x n+14]
%   strucLabels (cell array) - Region labels, size = [1 x n+14]
%
% Sara Lariviere  |  saratheriver@gmail.com

if nargin < 1 || strcmp(parcellation, 'aparc')
    sctmp = load('hcp_structural_data_with_sctx.mat');

    strucMatrix   = sctmp.sc.strucMatrix;
    strucLabels   = sctmp.sc.strucLabels;
else
    sctmp = load(['hcp_structural_data_' parcellation '_with_sctx.mat']);

    strucMatrix   = sctmp.sc.strucMatrix;
    strucLabels   = sctmp.sc.strucLabels;
    
end

return