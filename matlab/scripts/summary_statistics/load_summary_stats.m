function sum_stats = load_summary_stats(disorder)
%
% Usage: sum_stats = load_summary_stats(disorder)
%
% Outputs summary statistics for specific diseases/disorders
% 
%     Input (pick one)
%     ---------------------
%     '22q'
%     'adhd'
%     'asd'
%     'bipolar'
%     'depression'
%     'epilepsy'
%     'ocd'
%     'schizophrenia'
% 
%     Returns
%     -------
%     summary stats        = available summary statistics (table)
%
% Sara Lariviere  |  saratheriver@gmail.com
%
% Last modifications:
% SL | cold September day 2020

if nargin < 1
    disp('must specify a valid disorder...!')
end

switch disorder
    case '22q'                  
        sum_stats.CortThick_case_vs_controls = readtable('22q_case-controls_CortThick.csv');
        sum_stats.CortSurf_case_vs_controls  = readtable('22q_case-controls_CortSurf.csv');
        sum_stats.CortThick_psychP_vs_psychN = readtable('22q_psych+-psych-_CortThick.csv');
        sum_stats.CortSurf_psychP_vs_psychN  = readtable('22q_psych+-psych-_CortSurf.csv');
        
    case 'adhd'
        sum_stats.CortThick_case_vs_controls_allages = readtable('adhdallages_case-controls_CortThick.csv');
        sum_stats.CortSurf_case_vs_controls_allages = readtable('adhdallages_case-controls_CortSurf.csv');
        sum_stats.CortThick_case_vs_controls_adult = readtable('adhdadult_case-controls_CortThick.csv');
        sum_stats.CortSurf_case_vs_controls_adult = readtable('adhdadult_case-controls_CortSurf.csv');
        sum_stats.CortThick_case_vs_controls_adolescent = readtable('adhdadolescent_case-controls_CortThick.csv');
        sum_stats.CortSurf_case_vs_controls_adolescent = readtable('adhdadolescent_case-controls_CortSurf.csv');
        sum_stats.CortThick_case_vs_controls_pediatric = readtable('adhdpediatric_case-controls_CortThick.csv');
        sum_stats.CortSurf_case_vs_controls_pediatric = readtable('adhdpediatric_case-controls_CortSurf.csv');
              
    case 'asd'
        sum_stats.CortThick_case_vs_controls_meta_analysis = readtable('asd_meta-analysis_case-controls_CortThick.csv');
        sum_stats.CortThick_case_vs_controls_mega_analysis = readtable('asd_mega-analysis_case-controls_CortThick.csv');
           
    case 'bipolar'
        sum_stats.CortSurf_case_controls = readtable('bd_case-controls_CortSurf.csv');
        
    case 'depression'
        sum_stats.CortThick_case_vs_controls_adult = readtable('mddadult_case-controls_CortThick.csv');
        sum_stats.CortSurf_case_vs_controls_adult = readtable('mddadult_case-controls_CortSurf.csv');
        sum_stats.CortThick_case_vs_controls_adolescent = readtable('mddadolescent_case-controls_CortThick.csv');
        sum_stats.CortSurf_case_vs_controls_adolescent = readtable('mddadolescent_case-controls_CortSurf.csv');
          
    case 'epilepsy'
        sum_stats.CortThick_case_vs_controls_allepilepsy = readtable('allepi_case-controls_CortThick.csv');
        sum_stats.SubVol_case_vs_controls_allepilepsy = readtable('allepi_case-controls_SubVol.csv');
        sum_stats.CortThick_case_vs_controls_gge = readtable('gge_case-controls_CortThick.csv');
        sum_stats.SubVol_case_vs_controls_gge = readtable('gge_case-controls_SubVol.csv');
        sum_stats.CortThick_case_vs_controls_ltle = readtable('tlemtsl_case-controls_CortThick.csv');
        sum_stats.SubVol_case_vs_controls_ltle = readtable('tlemtsl_case-controls_SubVol.csv');
        sum_stats.CortThick_case_vs_controls_rtle = readtable('tlemtsr_case-controls_CortThick.csv');
        sum_stats.SubVol_case_vs_controls_rtle = readtable('tlemtsr_case-controls_SubVol.csv');
            
    case 'ocd'
        sum_stats.CortThick_case_vs_controls_adult = readtable('ocdadults_case-controls_CortThick.csv');
        sum_stats.CortSurf_case_vs_controls_adult = readtable('ocdadults_case-controls_CortSurf.csv');
        sum_stats.CortThick_medicatedcase_vs_controls_adult = readtable('ocdadults_medicatedcase-controls_CortThick.csv');
        sum_stats.CortSurf_medicatedcase_vs_controls_adult = readtable('ocdadults_medicatedcase-controls_CortSurf.csv');
        sum_stats.CortThick_case_vs_controls_pediatric = readtable('ocdpediatric_case-controls_CortThick.csv');
        sum_stats.CortSurf_case_vs_controls_pediatric = readtable('ocdpediatric_case-controls_CortSurf.csv');
        sum_stats.CortThick_medicatedcase_vs_controls_pediatric = readtable('ocdpediatric_medicatedcase-controls_CortThick.csv');
        sum_stats.CortSurf_medicatedcase_vs_controls_pediatric = readtable('ocdpediatric_medicatedcase-controls_CortSurf.csv');
               
    case 'schizophrenia'
        sum_stats.CortThick_case_vs_controls = readtable('scz_case-controls_CortThick.csv');
        sum_stats.CortSurf_case_vs_controls = readtable('scz_case-controls_CortSurf.csv');
         
end

return