function [fc, fcl, fcs, fcsl] = load_fc()
%
% Usage: [fc, fcl, fcs, fcsl] = load_fc()
%
% Simple script to load functional connectivity data
%   Outputs:
%       fc    = functional cortico-cortical connectivity matrix (68 x 68)
%       fcl   = name of cortical regions (in same order as fc; 1 x 68)
%       fcs   = functional subcortico-cortical connectivity matrix (14 x 68)
%       fcsl  = name of subcortical regions (in same order as fcs; 1 x 14)
%
% Please see Lariviere et al., 2020, bioRxiv for details on HCP
% participants, data processing, and connectivity matrix generation
%
%
% Sara Lariviere  |  saratheriver@gmail.com
%
% Last modifications:
% SL | a hot and humid July day 2020

fctmp = load('hcp_functional_data.mat');

fc    = fctmp.fc.funcMatrix_ctx;
fcl   = fctmp.fc.funcLabels_ctx;
fcs   = fctmp.fc.funcMatrix_sctx;
fcsl  = fctmp.fc.funcLabels_sctx;

return