

%% IMPORT
% .txt/.csv
data_lh = dlmread('/Users/saratheriver/Desktop/McGill_PhD/ENIGMA/enigmatoolbox/datasets/import_export/lh.conte69_32k_thickness.txt');
data_rh = dlmread('/Users/saratheriver/Desktop/McGill_PhD/ENIGMA/enigmatoolbox/datasets/import_export/rh.conte69_32k_thickness.txt');

% FreeSurfer "curv" file type (e.g., ?h.thickness)
data_lh = SurfStatReadData1('lh.conte69_32k_thickness');
data_rh = SurfStatReadData1('rh.conte69_32k_thickness');

% .mgh/.mgz
[data_lh, ~, ~,~] = load_mgh('lh.conte69_32k_thickness.mgh');
[data_rh, ~, ~,~] = load_mgh('lh.conte69_32k_thickness.mgh');

%% EXPORT
% .txt/.csv
writetable(array2table(data_lh), '/Users/saratheriver/Desktop/McGill_PhD/ENIGMA/enigmatoolbox/datasets/import_export/lh.conte69_32k_thickness.txt', 'WriteVariableNames', 0)
writetable(array2table(data_rh), '/Users/saratheriver/Desktop/McGill_PhD/ENIGMA/enigmatoolbox/datasets/import_export/rh.conte69_32k_thickness.txt', 'WriteVariableNames', 0)

% FreeSurfer curv file type (e.g., ?h.thickness)
SurfStatWriteData('lh.conte69_32k_thickness', data_lh)
SurfStatWriteData('lh.conte69_32k_thickness', data_rh)

% .mgh/.mgz

