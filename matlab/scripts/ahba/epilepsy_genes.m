function epigx = epilepsy_genes()
%
% Usage: epigx = epilepsy_genes()
%
% Simple script to fetch microarray expression data (pre-computed)
%   Outputs:
%       Outputs names of epilepsy-related risk genes based on previous GWAS
%       (ILAE on Complex Epilepsies, 2018, Nat Comms)
%
%       epigx : structured array with names of genes for epilepsy subtypes
%
%
% Sara Lariviere  |  saratheriver@gmail.com
%
% Last modifications:
% SL | a quiet July evening 2020 watching NHL hockey (like whaaaat)

epigx.allepilepsy         = [{'FANCL'}, {'BCL11A'}, {'SCN3A'}, {'SCN2A'}, {'TTC21B'}, ...
                             {'SCN1A'}, {'HEATR3'}, {'BRD7'}];
epigx.focalepilepsy       = [{'SCN3A'}, {'SCN2A'}, {'TTC21B'}, {'SCN1A'}];
epigx.generalizedepilepsy = [{'FANCL'}, {'BCL11A'}, {'SCN3A'}, {'SCN2A'}, {'TTC21B'}, ...
                             {'SCN1A'}, {'STAT4'}, {'PCDH7'}, {'GABRA2'}, {'KCNN2'}, ...
                             {'ATXN1'}, {'PNPO'}, {'GRIK1'}];
epigx.jme                 = [{'STX1B'}];
epigx.cae                 = [{'FANCL'}, {'BCL11A'}, {'ZEB2'}];
epigx.focalhs             = [{'C3orf33'}, {'SLC33A1'}, {'KCNAB1'}, {'GJA1'}];



return