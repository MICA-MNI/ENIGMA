function exportfigbo(f,name,format,fontsize)
% shortcut to a longer exportfig command
%
    exportfig(f, name, 'Format',format,'FontMode', 'fixed',...
              'FontSize', fontsize, 'color', 'cmyk','Resolution', 300);