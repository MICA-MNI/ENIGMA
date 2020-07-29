% load connectivity data
[~, l1, ~, l2]     = load_fc();

% load all genes
ag = readtable('allgenes.csv');
% column names
ag.Properties.VariableNames;

% regios
ag(:,1)