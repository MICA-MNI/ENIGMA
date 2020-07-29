% load connectivity data
[~, ~, fc, ~]     = load_fc();
[~, ~, sc, ~]     = load_sc();

% compute weighted degree centrality
dc_f                = sum(fc, 2);
dc_s                = sum(sc, 2);

% and project the results on the surface brain
f = figure,
    plot_subcortical(dc_f, 'False', 'functional degree centrality')
    colormap([Reds])
    SurfStatColLim([5 10])
    
f = figure,
     plot_subcortical(dc_s, 'False', 'structural degree centrality')
    colormap([Blues])
    SurfStatColLim([100 300])