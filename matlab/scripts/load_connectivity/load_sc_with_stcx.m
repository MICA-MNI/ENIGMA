function [strucMatrix, strucLabels] = load_sc_with_stcx()
%
% Usage: 
%   [strucMatrix_ctx, strucLabels_ctx] = load_sc_with_stcx()
%
% Description:
%   Load structural connectivity data (cortical + subcortical in one matrix) 
%       parcellated using Desikan Killiany (author: @saratheriver)
%
% Outputs:
%   strucMatrix (double array) - Structural connectivity, size = [82 x 82]
%   strucLabels (cell array) - Region labels, size = [1 x 82]
%
% Sara Lariviere  |  saratheriver@gmail.com

sctmp = load('hcp_structural_data_with_sctx.mat');

strucMatrix   = sctmp.sc.strucMatrix;
strucLabels   = sctmp.sc.strucLabels;

return