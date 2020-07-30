addpath(genpath('/path/to/ENIGMA/matlab/'));

%% Following the above code, we can then map epilepsy-related gene expression to the cortical surface!
mean_fh_gx           = mean(fh_gx, 2);
fh_gx_fsa5           = map_to_labels(mean_fh_gx(1:68), 'aparc_fsa5.csv');

f = figure,
  plot_cortical(fh_gx_fsa5, 'fsa5', 'focal hs-related gene expression')
  colormap([Reds])
  SurfStatColLim([.4 .55])

%% And to the subcortical surface!!
f = figure,
  plot_subcortical(mean_fh_gx(69:end), 'False', 'focal hs-related gene expression')
  colormap([Reds])
  SurfStatColLim([.4 .65])
