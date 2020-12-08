function genes = fetch_ahba(csvfile)
%
% Usage: genes = fetch_ahba(csvfile);
%
% Description
%   Fetch Allen Human Brain Atlas microarray expression data from all 
%   donors and all genes (author: @saratheriver)
%
% Inputs:
%   csvfile (empty or string, optional) - Path to downloaded csvfile. 
%   If empty, fetches microarray expression data from the internet.
%
% Outputs: 
%   genes (table) - Gene co-expression data, size = [82 x 15634]
%
% Sara Lariviere  |  saratheriver@gmail.com

if nargin < 1
    % Fetch the csv table from github and load it locally | option 1
    url   = 'https://raw.githubusercontent.com/saratheriver/enigma-extra/master/ahba/allgenes_stable20.csv';
    urlwrite(url, '.gtmp.csv');
    genes = readtable('.gtmp.csv');

    % remove table locally | option 1
    delete('.gtmp.csv');

else
    genes = readtable(csvfile);
end
    
return