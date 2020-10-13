function genes = fetch_ahba()
%
% Usage: genes = fetch_ahba();
%
% Description
%   Fetch Allen Human Brain Atlas microarray expression data from all 
%   donors and all genes (author: @saratheriver)
%
% Inputs:
%   csvfile (empty or string, optional) ? Path to downloaded csvfile. 
%   If empty (default), fetches microarray expression data from the internet.
%
% Outputs: 
%   genes (table) - Gene co-expression data, size = [82 x 15634]
%
% Sara Lariviere  |  saratheriver@gmail.com

if nargin < 1
    % Fetch the csv table from github and load it locally | option 1
    url = 'https://raw.githubusercontent.com/saratheriver/enigma-extra/master/ahba/allgenes.csv';
    urlwrite(url, '.gtmp.csv');
    g = readtable('.gtmp.csv');

    % Extract relevant information
    genes          = table2array(g(:, 2:end));
    reglabels   = table2array(g(:, 1));
    genelabels  = g.Properties.VariableNames(2:end);

    % remove table locally | option 1
    delete('.gtmp.csv');

else
    genes = readtable(csvfile);
end
    
return