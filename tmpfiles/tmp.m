[gx, reglabels, genelabels] = fetch_ahba();

% epsi-tle
epigx        = risk_genes('epilepsy');
fh_genes     = find(ismember(genelabels, epigx.focalhs));
fh_gx        = gx(:, fh_genes);
fh_gx_fsa5   = map_to_labels(rescale(mean(fh_gx(1:68, :), 2)), 'aparc_fsa5.csv');

f = figure,
  plot_cortical(fh_gx_fsa5, 'fsa5', 'focal hs-related gene expression')
  colormap([Reds])
  SurfStatColLim([0 1])

f = figure,
  plot_subcortical(rescale(mean(fh_gx(69:end, :), 2)), 'False', 'focal hs-related gene expression')
  colormap([Reds])
  SurfStatColLim([0 1])
  
% asd
asdgx        = risk_genes('asd');
asd_genes     = find(ismember(genelabels, asdgx));
asd_gx        = gx(:, asd_genes);
asd_gx_fsa5   = map_to_labels(rescale(mean(asd_gx(1:68, :), 2)), 'aparc_fsa5.csv');

f = figure,
  plot_cortical(asd_gx_fsa5, 'fsa5', 'asd-related gene expression')
  colormap([Reds])
  SurfStatColLim([0 1])
f = figure,
  plot_subcortical(rescale(mean(asd_gx(69:end, :), 2)), 'False', 'asd-related gene expression')
  colormap([Reds])
  SurfStatColLim([0 1])  
  
% bipolar
bipgx        = risk_genes('bipolar');
bip_genes     = find(ismember(genelabels, bipgx));
bip_gx        = gx(:, bip_genes);
bip_gx_fsa5   = map_to_labels(rescale(mean(bip_gx(1:68, :), 2)), 'aparc_fsa5.csv');

f = figure,
  plot_cortical(bip_gx_fsa5, 'fsa5', 'bipolar-related gene expression')
  colormap([Reds])
  SurfStatColLim([0 1])
f = figure,
  plot_subcortical(rescale(mean(bip_gx(69:end, :), 2)), 'False', 'bipolar-related gene expression')
  colormap([Reds])
  SurfStatColLim([0 1])    
  
% depression
depgx        = risk_genes('depression');
dep_genes     = find(ismember(genelabels, depgx));
dep_gx        = gx(:, dep_genes);
dep_gx_fsa5   = map_to_labels(rescale(mean(dep_gx(1:68, :), 2)), 'aparc_fsa5.csv');

f = figure,
  plot_cortical(dep_gx_fsa5, 'fsa5', 'depression-related gene expression')
  colormap([Reds])
  SurfStatColLim([0 1])
f = figure,
  plot_subcortical(rescale(mean(dep_gx(69:end, :), 2)), 'False', 'depression-related gene expression')
  colormap([Reds])
  SurfStatColLim([0 1])  
  
  
% schizophrenia
sczgx        = risk_genes('schizophrenia');
scz_genes     = find(ismember(genelabels, sczgx));
scz_gx        = gx(:, scz_genes);
scz_gx_fsa5   = map_to_labels(rescale(mean(scz_gx(1:68, :), 2)), 'aparc_fsa5.csv');

f = figure,
  plot_cortical(scz_gx_fsa5, 'fsa5', 'schiz-related gene expression')
  colormap([Reds])
  SurfStatColLim([0 1])
f = figure,
  plot_subcortical(rescale(mean(scz_gx(69:end, :), 2)), 'False', 'schizophrenia-related gene expression')
  colormap([Reds])
  SurfStatColLim([0 1])  