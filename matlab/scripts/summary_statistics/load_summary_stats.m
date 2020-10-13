function summary_stats = load_summary_stats(disorder)
%
% Usage: 
%   summary_stats = load_summary_stats(disorder)
%
% Description:
%   Outputs summary statistics for a given disorder (author: @saratheriver)
% 
% Inputs:
%   disorder ({?22q?, ?adhd?, ?asd?, ?bipolar?, ?depression?, ?epilepsy?,
%   ?ocd?, ?schizophrenia?}) ? Disorder name, must pick one.
% 
% Outputs:
%	summary stats (table) - Available summary statistics
%
% Sara Lariviere  |  saratheriver@gmail.com

if nargin < 1
    disp('must specify a valid disorder...!')
end

switch disorder
    case '22q'                  
        summary_stats.CortThick_case_vs_controls = readtable('22q_case-controls_CortThick.csv');
        summary_stats.CortSurf_case_vs_controls  = readtable('22q_case-controls_CortSurf.csv');
        summary_stats.CortThick_psychP_vs_psychN = readtable('22q_psych+-psych-_CortThick.csv');
        summary_stats.CortSurf_psychP_vs_psychN  = readtable('22q_psych+-psych-_CortSurf.csv');
        
    case 'adhd'
        summary_stats.CortThick_case_vs_controls_allages = readtable('adhdallages_case-controls_CortThick.csv');
        summary_stats.CortSurf_case_vs_controls_allages = readtable('adhdallages_case-controls_CortSurf.csv');
        summary_stats.CortThick_case_vs_controls_adult = readtable('adhdadult_case-controls_CortThick.csv');
        summary_stats.CortSurf_case_vs_controls_adult = readtable('adhdadult_case-controls_CortSurf.csv');
        summary_stats.CortThick_case_vs_controls_adolescent = readtable('adhdadolescent_case-controls_CortThick.csv');
        summary_stats.CortSurf_case_vs_controls_adolescent = readtable('adhdadolescent_case-controls_CortSurf.csv');
        summary_stats.CortThick_case_vs_controls_pediatric = readtable('adhdpediatric_case-controls_CortThick.csv');
        summary_stats.CortSurf_case_vs_controls_pediatric = readtable('adhdpediatric_case-controls_CortSurf.csv');
              
    case 'asd'
        summary_stats.CortThick_case_vs_controls_meta_analysis = readtable('asd_meta-analysis_case-controls_CortThick.csv');
        summary_stats.CortThick_case_vs_controls_mega_analysis = readtable('asd_mega-analysis_case-controls_CortThick.csv');
           
    case 'bipolar'
        summary_stats.CortSurf_case_controls = readtable('bd_case-controls_CortSurf.csv');
        
    case 'depression'
        summary_stats.CortThick_case_vs_controls_adult = readtable('mddadult_case-controls_CortThick.csv');
        summary_stats.CortSurf_case_vs_controls_adult = readtable('mddadult_case-controls_CortSurf.csv');
        summary_stats.CortThick_case_vs_controls_adolescent = readtable('mddadolescent_case-controls_CortThick.csv');
        summary_stats.CortSurf_case_vs_controls_adolescent = readtable('mddadolescent_case-controls_CortSurf.csv');
          
    case 'epilepsy'
        summary_stats.CortThick_case_vs_controls_allepilepsy = readtable('allepi_case-controls_CortThick.csv');
        summary_stats.SubVol_case_vs_controls_allepilepsy = readtable('allepi_case-controls_SubVol.csv');
        summary_stats.CortThick_case_vs_controls_gge = readtable('gge_case-controls_CortThick.csv');
        summary_stats.SubVol_case_vs_controls_gge = readtable('gge_case-controls_SubVol.csv');
        summary_stats.CortThick_case_vs_controls_ltle = readtable('tlemtsl_case-controls_CortThick.csv');
        summary_stats.SubVol_case_vs_controls_ltle = readtable('tlemtsl_case-controls_SubVol.csv');
        summary_stats.CortThick_case_vs_controls_rtle = readtable('tlemtsr_case-controls_CortThick.csv');
        summary_stats.SubVol_case_vs_controls_rtle = readtable('tlemtsr_case-controls_SubVol.csv');
            
    case 'ocd'
        summary_stats.CortThick_case_vs_controls_adult = readtable('ocdadults_case-controls_CortThick.csv');
        summary_stats.CortSurf_case_vs_controls_adult = readtable('ocdadults_case-controls_CortSurf.csv');
        summary_stats.CortThick_medicatedcase_vs_controls_adult = readtable('ocdadults_medicatedcase-controls_CortThick.csv');
        summary_stats.CortSurf_medicatedcase_vs_controls_adult = readtable('ocdadults_medicatedcase-controls_CortSurf.csv');
        summary_stats.CortThick_case_vs_controls_pediatric = readtable('ocdpediatric_case-controls_CortThick.csv');
        summary_stats.CortSurf_case_vs_controls_pediatric = readtable('ocdpediatric_case-controls_CortSurf.csv');
        summary_stats.CortThick_medicatedcase_vs_controls_pediatric = readtable('ocdpediatric_medicatedcase-controls_CortThick.csv');
        summary_stats.CortSurf_medicatedcase_vs_controls_pediatric = readtable('ocdpediatric_medicatedcase-controls_CortSurf.csv');
               
    case 'schizophrenia'
        summary_stats.CortThick_case_vs_controls = readtable('scz_case-controls_CortThick.csv');
        summary_stats.CortSurf_case_vs_controls = readtable('scz_case-controls_CortSurf.csv');
         
end

return