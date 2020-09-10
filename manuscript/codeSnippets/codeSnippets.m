%% Figure 1b. Load example data
% Add the path to the ENIGMA TOOLBOX matlab folder
addpath(genpath('/path/to/ENIGMA/matlab/'));

% Load example data
[cov, metr1_SubVol, metr2_CortThick, metr3_CortSurf] = load_example_data();

% Z-score data in patients relative to controls
groups        = cov.Dx;
controlGroup  = 0;
CortThick_Z   = zscore_matrix(metr2_CortThick(:, 2:end-5), groups, controlGroup);
SubVol_Z      = zscore_matrix(metr1_SubVol(:, 2:end-1), groups, controlGroup);

% Extract data for a specific group (e.g., individuals with left TLE)
CortThick_Z_LTLE  = CortThick_Z(find(cov.SDx == 3), :);
SubVol_Z_LTLE     = SubVol_Z(find(cov.SDx == 3), :);


%% Figure 1d. Load summary statistics
% Add the path to the ENIGMA TOOLBOX matlab folder
addpath(genpath('/path/to/ENIGMA/matlab/'));


%% Figure 2. Surface data visualization
% Re-order subcortical data (alphabetically and by hemisphere)

% Mean data across all individuals with left TLE



% Map parcellated data to the surface (cortical values only)


% Project data to the surface templates

                 
                 
                 