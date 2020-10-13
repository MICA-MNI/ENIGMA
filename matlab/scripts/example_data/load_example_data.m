function [cov, metr1_SubVol, metr2_CortThick, metr3_CortSurf] = load_example_data()
%
% Usage:
%   [cov, metr1_SubVol, metr2_CortThick, metr3_CortSurf] = load_example_data()
%
% Description:
%   Loads the ENIGMA example dataset (from one site - MICA-MNI Montreal; 
%   author: @saratheriver)
%
% Outputs:
%       cov (table) - Contains information on covariates
%       metr1 (table) - Contains information on subcortical volume
%       metr2 (table) - Contains information on cortical thickness
%       metr3 (table) - Contains information on surface area
%
%
% Sara Lariviere  |  saratheriver@gmail.com

cov               = readtable('cov.csv');
metr1_SubVol      = readtable('metr1_SubVol.csv');
metr2_CortThick   = readtable('metr2_CortThick.csv');
metr3_CortSurf    = readtable('metr3_CortSurf.csv');

return