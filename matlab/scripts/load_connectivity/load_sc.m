function [strucMatrix_ctx, strucLabels_ctx, strucMatrix_sctx, strucLabels_sctx] = load_sc()
%
% Usage: 
%   [strucMatrix_ctx, strucLabels_ctx, strucMatrix_sctx, strucLabels_sctx] = load_fc()
%
% Description:
%   Load structural connectivity data parcellated using Desikan Killiany (author: @saratheriver)
%
% Outputs:
%   strucMatrix_ctx (double array) ? Cortico-cortical connectivity, size = [68 x 68]
%   strucLabels_ctx (cell array) ? Cortical labels, size = [1 x 68]
%   strucMatrix_sctx (double array) ? Subcortico-cortical connectivity, size = [14 x 68]
%   strucLabels_sctx (cell array) ? Subcortical labels, size = [1 x 14]
%
% Sara Lariviere  |  saratheriver@gmail.com

sctmp = load('hcp_structural_data.mat');

strucMatrix_ctx   = sctmp.sc.strucMatrix_ctx;
strucLabels_ctx   = sctmp.sc.strucLabels_ctx;
strucMatrix_sctx  = sctmp.sc.strucMatrix_sctx;
strucLabels_sctx  = sctmp.sc.strucLabels_sctx;

return