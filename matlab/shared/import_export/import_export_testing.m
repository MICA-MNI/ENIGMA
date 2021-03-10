
%% HAVE EM ALL IN SAME DIMENSION

%% IMPORT

data_path = '/Users/saratheriver/Desktop/McGill_PhD/ENIGMA/enigmatoolbox/datasets/import_export/';

% .txt/.csv
data_lh = dlmread([data_path 'lh.conte69_32k_thickness.txt']);
data_rh = dlmread('/Users/saratheriver/Desktop/McGill_PhD/ENIGMA/enigmatoolbox/datasets/import_export/rh.conte69_32k_thickness.txt');
CT = [data_lh data_rh];

% FreeSurfer "curv" file type (e.g., ?h.thickness) - https://github.com/neurodebian/freesurfer/tree/debian-sloppy/matlab
data_lh = read_curv('/Users/saratheriver/Desktop/McGill_PhD/ENIGMA/enigmatoolbox/datasets/import_export/lh.conte69_32k_thickness');
data_rh = read_curv('/Users/saratheriver/Desktop/McGill_PhD/ENIGMA/enigmatoolbox/datasets/import_export/rh.conte69_32k_thickness');
CT = [data_lh; data_rh].';

% .mgh/.mgz - https://surfer.nmr.mgh.harvard.edu/fswiki/FsTutorial/MghFormat
data_lh = load_mgh('/Users/saratheriver/Desktop/McGill_PhD/ENIGMA/enigmatoolbox/datasets/import_export/lh.conte69_32k_thickness.mgh');
data_rh = load_mgh('/Users/saratheriver/Desktop/McGill_PhD/ENIGMA/enigmatoolbox/datasets/import_export/rh.conte69_32k_thickness.mgh');
CT = [data_lh; data_rh].';

% GIfTI - https://github.com/gllmflndn/gifti
data_lh = gifti('/Users/saratheriver/Desktop/McGill_PhD/ENIGMA/enigmatoolbox/datasets/import_export/lh.conte69_32k_thickness.gii');
data_rh = gifti('/Users/saratheriver/Desktop/McGill_PhD/ENIGMA/enigmatoolbox/datasets/import_export/rh.conte69_32k_thickness.gii');
CT = [data_lh.cdata; data_rh.cdata].';


%% EXPORT
% .txt/.csv
writetable(array2table(data_lh), '/Users/saratheriver/Desktop/McGill_PhD/ENIGMA/enigmatoolbox/datasets/import_export/lh.conte69_32k_thickness.txt', 'WriteVariableNames', 0)
writetable(array2table(data_rh), '/Users/saratheriver/Desktop/McGill_PhD/ENIGMA/enigmatoolbox/datasets/import_export/rh.conte69_32k_thickness.txt', 'WriteVariableNames', 0)

% FreeSurfer curv file type (e.g., ?h.thickness)
SurfStatWriteData('/Users/saratheriver/Desktop/McGill_PhD/ENIGMA/enigmatoolbox/datasets/import_export/lh.conte69_32k_thickness', data_lh)
SurfStatWriteData('/Users/saratheriver/Desktop/McGill_PhD/ENIGMA/enigmatoolbox/datasets/import_export/rh.conte69_32k_thickness', data_rh)

% .mgh/.mgz - https://surfer.nmr.mgh.harvard.edu/fswiki/FsTutorial/MghFormat - need affine matrix M ... used load_mgh to load template
save_mgh(data_lh, '/Users/saratheriver/Desktop/McGill_PhD/ENIGMA/enigmatoolbox/datasets/import_export/lh.conte69_32k_thickness2.mgh', M);
save_mgh(data_rh, '/Users/saratheriver/Desktop/McGill_PhD/ENIGMA/enigmatoolbox/datasets/import_export/rh.conte69_32k_thickness2.mgh', M);

% GIfTI - https://github.com/gllmflndn/gifti - rename gifti/@gifti/save.m as gifti/@gifti/savegifti.m - data_?h must be a GIfTI object
savegifti(data_lh, '/Users/saratheriver/Desktop/McGill_PhD/ENIGMA/enigmatoolbox/datasets/import_export/lh.conte69_32k_thickness.gii', 'Base64Binary');
savegifti(data_rh, '/Users/saratheriver/Desktop/McGill_PhD/ENIGMA/enigmatoolbox/datasets/import_export/rh.conte69_32k_thickness.gii', 'Base64Binary');
