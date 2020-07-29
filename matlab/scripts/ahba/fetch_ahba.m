function [gx, reglabels, genelabels] = fetch_ahba()
%
% Usage: [gx, reglabels, genelabels] = fetch_ahba()
%
% Simple script to fetch microarray expression data (pre-computed)
%   Outputs:
%       gx          = matrix of gene expression data (82 x 15633)
%       reglabels   = name of cortical regions in same order as gx
%                     (82 x 1 cell array)
%       genelabels  = name of genes in same order as gx
%                     (1 x 15633 cell array)
%
% Data pre-computed using the abagen toolbox (https://github.com/rmarkello/abagen)
%   - includes all donors
%   - all genes
%   - re-ordered Desikan-Killiany labels to match ENIGMA-derived matrices
%
% Sara Lariviere  |  saratheriver@gmail.com
%
% Last modifications:
% SL | a rainy July day 2020

% Fetch the csv table from github and load it locally
url = 'https://raw.githubusercontent.com/saratheriver/enigma-extra/master/ahba/allgenes.csv';
urlwrite(url, '.gtmp.csv');
g = readtable('.gtmp.csv');

% Extract relevant information
gx          = table2array(g(:, 2:end));
reglabels   = table2array(g(:, 1));
genelabels  = g.Properties.VariableNames(2:end);

% remove table locally
delete('.gtmp.csv');

return