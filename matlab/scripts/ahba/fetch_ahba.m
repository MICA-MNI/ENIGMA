function [gx, reglabels, genelabels] = fetch_ahba(csvfile)
%
% Usage: [gx, reglabels, genelabels] = fetch_ahba();
%
% Simple script to fetch microarray expression data (pre-computed)
%   Input (OPTIONAL):
%       If the allgenes.csv file is already downloaded locally, then
%       specific its path as follows: 
%       [gx, reglabels, genelabels] = fetch_ahba('/path/to/allgenes.csv');
%
%       Leave empty to fetch data file from the internet (requires a good
%       connection!)
%
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
% SL | the day after the rainy day (it's now sunny)

if nargin < 1
    % Fetch the csv table from github and load it locally | option 1
    url = 'https://raw.githubusercontent.com/saratheriver/enigma-extra/master/ahba/allgenes.csv';
    urlwrite(url, '.gtmp.csv');
    g = readtable('.gtmp.csv');

    % Extract relevant information
    gx          = table2array(g(:, 2:end));
    reglabels   = table2array(g(:, 1));
    genelabels  = g.Properties.VariableNames(2:end);

    % remove table locally | option 1
    delete('.gtmp.csv');

else
    g = readtable(csvfile);
    gx          = table2array(g(:, 2:end));
    reglabels   = table2array(g(:, 1));
    genelabels  = g.Properties.VariableNames(2:end);
end
    
return