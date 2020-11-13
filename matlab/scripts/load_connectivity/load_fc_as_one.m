function [funcMatrix, funcLabels] = load_fc_as_one()
%
% Usage: 
%   [funcMatrix_ctx, funcLabels_ctx] = load_fc_as_one()
%
% Description:
%   Load functional connectivity data (cortical + subcortical in one matrix) 
%       parcellated using Desikan Killiany (author: @saratheriver)
%
% Outputs:
%   funcMatrix (double array) - Functional connectivity, size = [82 x 82]
%   funcLabels (cell array) - Region labels, size = [1 x 82]
%
% Sara Lariviere  |  saratheriver@gmail.com

fctmp = load('hcp_functional_data_with_sctx.mat');

funcMatrix   = fctmp.fc.funcMatrix;
funcLabels   = fctmp.fc.funcLabels;

return