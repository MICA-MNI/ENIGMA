function [cov, metr1_SubVol, metr2_CortThick, metr3_CortSurf] = load_example_data()
%
% Usage: [cov, metr1_SubVol, metr2_CortThick, metr3_CortSurf] = load_example_data()
%
% Simple script to load our example data (processed according to ENIGMA
% protocols!)
%
%   Outputs:
%       cov   = contains information on covariates (20 x 9 table)
%       metr1 = contains information on subcortical volume (20 x 18 table)
%       metr2 - contains information on cortical thickness (20 x 74 table)
%       metr3 = contains information on surface area (20 x 74 table)
%
%
% Sara Lariviere  |  saratheriver@gmail.com
%
% Last modifications:
% SL | still a hot and humid day in August 2020 (whatta summer!)

cov               = readtable('cov.csv');
metr1_SubVol      = readtable('metr1_SubVol.csv');
metr2_CortThick   = readtable('metr2_CortThick.csv');
metr3_CortSurf    = readtable('metr3_CortSurf.csv');

return