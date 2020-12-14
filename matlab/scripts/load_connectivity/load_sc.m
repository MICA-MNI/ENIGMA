function [strucMatrix_ctx, strucLabels_ctx, strucMatrix_sctx, strucLabels_sctx] = load_sc(parcellation)
%
% Usage: 
%   [strucMatrix_ctx, strucLabels_ctx, strucMatrix_sctx, strucLabels_sctx] = load_fc(parcellation)
%
% Description:
%   Load structural connectivity data (author: @saratheriver)
%
% Inputs:
%   parcellation (string, optional) - Name of parcellation (with n cortical parcels). Default is
%   'aparc'. Other options are 'schaefer_100', 'schaefer_200', 'schaefer_300',
%   'schaefer_400'.
%
% Outputs:
%   strucMatrix_ctx (double array) - Cortico-cortical connectivity, size = [n x n]
%   strucLabels_ctx (cell array) - Cortical labels, size = [1 x n]
%   strucMatrix_sctx (double array) - Subcortico-cortical connectivity, size = [14 x n]
%   strucLabels_sctx (cell array) - Subcortical labels, size = [1 x 14]
%
% Sara Lariviere  |  saratheriver@gmail.com

if nargin < 1 || strcmp(parcellation, 'aparc')
    sctmp = load('hcp_structural_data.mat');

    strucMatrix_ctx   = sctmp.sc.strucMatrix_ctx;
    strucLabels_ctx   = sctmp.sc.strucLabels_ctx;
    strucMatrix_sctx  = sctmp.sc.strucMatrix_sctx;
    strucLabels_sctx  = sctmp.sc.strucLabels_sctx;   
else
    sctmp = load(['hcp_structural_data_' parcellation '.mat']);

    strucMatrix_ctx   = sctmp.sc.strucMatrix_ctx;
    strucLabels_ctx   = sctmp.sc.strucLabels_ctx;
    strucMatrix_sctx  = sctmp.sc.strucMatrix_sctx;
    strucLabels_sctx  = sctmp.sc.strucLabels_sctx;  
end

return