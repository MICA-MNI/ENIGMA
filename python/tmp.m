[gx, reglabels, genelabels] = fetch_ahba();
epigx        = epilepsy_genes();
fh_genes     = find(ismember(genelabels, epigx.focalhs));