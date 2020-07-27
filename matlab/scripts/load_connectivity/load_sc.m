function [sc, scl, scs, scsl] = load_sc()
%
% Usage: [sc, scl, scs, scsl] = load_sc()
%
% Simple script to load structural connectivity data
%   Outputs:
%       sc    = structural cortico-cortical connectivity matrix (68 x 68)
%       scl   = name of cortical regions (in same order as sc; 1 x 68)
%       scs   = structural subcortico-cortical connectivity matrix (14 x 68)
%       scsl  = name of subcortical regions (in same order as scs; 1 x 14)
%
%
% Sara Lariviere  |  saratheriver@gmail.com
%
% Last modifications:
% SL | a hot and humid July day 2020

sctmp = load('hcp_structural_data.mat');

sc    = sctmp.sc.strucMatrix_ctx;
scl   = sctmp.sc.strucLabels_ctx;
scs   = sctmp.sc.strucMatrix_sctx;
scsl  = sctmp.sc.strucLabels_sctx;

return