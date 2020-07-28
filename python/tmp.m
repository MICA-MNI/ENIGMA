% load connectivity data
[fc, ~, ~, ~]     = load_fc();
[sc, ~, ~, ~]     = load_sc();

% compute weighted degree centrality
dc_f                = sum(fc);
dc_s                = sum(sc);

% map parcellated data to surface
dc_f_fsa5           = map_to_labels(dc_f, 'aparc_fsa5.csv');
dc_s_fsa5           = map_to_labels(dc_s, 'aparc_fsa5.csv');

% and project the results on the surface brain
f = figure,
    plot_cortical(dc_f_fsa5, 'fsa5', 'functional degree centrality')
    colormap([Reds])
    SurfStatColLim([20 30])
    
f = figure,
    plot_cortical(dc_s_fsa5, 'fsa5', 'structural degree centrality')
    colormap([Blues])
    SurfStatColLim([100 300])