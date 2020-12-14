function [funcMatrix_ctx, funcLabels_ctx, funcMatrix_sctx, funcLabels_sctx] = load_fc(parcellation)
%
% Usage: 
%   [funcMatrix_ctx, funcLabels_ctx, funcMatrix_sctx, funcLabels_sctx] = load_fc(parcellation)
%
% Description:
%   Load functional connectivity data (author: @saratheriver)
%
% Inputs:
%   parcellation (string, optional) - Name of parcellation (with n cortical parcels). Default is
%   'aparc'. Other options are 'schaefer_100', 'schaefer_200', 'schaefer_300',
%   'schaefer_400'.
%
% Outputs:
%   funcMatrix_ctx (double array) - Cortico-cortical connectivity, size = [n x n]
%   funcLabels_ctx (cell array) - Cortical labels, size = [1 x n]
%   funcMatrix_sctx (double array) - Subcortico-cortical connectivity, size = [14 x n]
%   funcLabels_sctx (cell array) - Subcortical labels, size = [1 x 14]
%
% Sara Lariviere  |  saratheriver@gmail.com

if nargin < 1 || strcmp(parcellation, 'aparc')
    fctmp = load('hcp_functional_data.mat');

    funcMatrix_ctx   = fctmp.fc.funcMatrix_ctx;
    funcLabels_ctx   = fctmp.fc.funcLabels_ctx;
    funcMatrix_sctx  = fctmp.fc.funcMatrix_sctx;
    funcLabels_sctx  = fctmp.fc.funcLabels_sctx;
else
    fctmp = load(['hcp_functional_data_' parcellation '.mat']);

    funcMatrix_ctx   = fctmp.fc.funcMatrix_ctx;
    funcLabels_ctx   = fctmp.fc.funcLabels_ctx;
    funcMatrix_sctx  = fctmp.fc.funcMatrix_sctx;
    funcLabels_sctx  = fctmp.fc.funcLabels_sctx;
end
    
return