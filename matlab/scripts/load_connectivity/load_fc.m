function [funcMatrix_ctx, funcLabels_ctx, funcMatrix_sctx, funcLabels_sctx] = load_fc()
%
% Usage: 
%   [funcMatrix_ctx, funcLabels_ctx, funcMatrix_sctx, funcLabels_sctx] = load_fc()
%
% Description:
%   Load structural connectivity data parcellated using Desikan Killiany (author: @saratheriver)
%
% Outputs:
%   funcMatrix_ctx (double array) ? Cortico-cortical connectivity, size = [68 x 68]
%   funcLabels_ctx (cell array) ? Cortical labels, size = [1 x 68]
%   funcMatrix_sctx (double array) ? Subcortico-cortical connectivity, size = [14 x 68]
%   funcLabels_sctx (cell array) ? Subcortical labels, size = [1 x 14]
%
% Sara Lariviere  |  saratheriver@gmail.com

fctmp = load('hcp_functional_data.mat');

funcMatrix_ctx   = fctmp.fc.funcMatrix_ctx;
funcLabels_ctx   = fctmp.fc.funcLabels_ctx;
funcMatrix_sctx  = fctmp.fc.funcMatrix_sctx;
funcLabels_sctx  = fctmp.fc.funcLabels_sctx;

return