function summary_stats = load_summary_stats(disorder)
%
% Usage: 
%   summary_stats = load_summary_stats(disorder)
%
% Description:
%   Outputs summary statistics for a given disorder (author: @saratheriver)
% 
% Inputs:
%   disorder ({'22q', 'adhd', 'asd', 'bipolar', 'depression', 'epilepsy',
%   'ocd', 'schizophrenia'}) - Disorder name, must pick one.
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
        summary_stats.SubVol_case_vs_controls = readtable('22q_case-controls_SubVol.csv');
        summary_stats.SubVol_case_vs_controls_AD = readtable('22q_case-controls_SubVol_AD.csv');
        summary_stats.SubVol_case_vs_controls_AB = readtable('22q_case-controls_SubVol_AB.csv');
        summary_stats.SubVol_AB_vs_AD = readtable('22q_AB-AD_SubVol.csv');   
        summary_stats.SubVol_psychP_vs_psychN = readtable('22q_psych+-psych-_SubVol.csv');
        
    case 'adhd'
        summary_stats.CortThick_case_vs_controls_allages = readtable('adhdallages_case-controls_CortThick.csv');
        summary_stats.CortSurf_case_vs_controls_allages = readtable('adhdallages_case-controls_CortSurf.csv');
        summary_stats.CortThick_case_vs_controls_adult = readtable('adhdadult_case-controls_CortThick.csv');
        summary_stats.CortSurf_case_vs_controls_adult = readtable('adhdadult_case-controls_CortSurf.csv');
        summary_stats.CortThick_case_vs_controls_adolescent = readtable('adhdadolescent_case-controls_CortThick.csv');
        summary_stats.CortSurf_case_vs_controls_adolescent = readtable('adhdadolescent_case-controls_CortSurf.csv');
        summary_stats.CortThick_case_vs_controls_pediatric = readtable('adhdpediatric_case-controls_CortThick.csv');
        summary_stats.CortSurf_case_vs_controls_pediatric = readtable('adhdpediatric_case-controls_CortSurf.csv');
        summary_stats.SubVol_case_vs_controls_allages = readtable('adhdallages_case-controls_SubVol.csv');
        summary_stats.SubVol_case_vs_controls_adult = readtable('adhdadult_case-controls_SubVol.csv');
        summary_stats.SubVol_case_vs_controls_adolescent = readtable('adhdadolescent_case-controls_SubVol.csv');
        summary_stats.SubVol_case_vs_controls_pediatric = readtable('adhdpediatric_case-controls_SubVol.csv');
              
    case 'asd'
        summary_stats.CortThick_case_vs_controls_meta_analysis = readtable('asd_meta-analysis_case-controls_CortThick.csv');
        summary_stats.CortThick_case_vs_controls_mega_analysis = readtable('asd_mega-analysis_case-controls_CortThick.csv');
        summary_stats.SubVol_case_vs_controls_meta_analysis = readtable('asd_meta-analysis_case-controls_SubVol.csv');
           
    case 'bipolar'
        summary_stats.CortThick_case_vs_controls_adult = readtable('bd_case-controls_CortThick_adult.csv');
        summary_stats.CortSurf_case_vs_controls_adult = readtable('bd_case-controls_CortSurf_adult.csv');
        summary_stats.CortThick_typeI_vs_typeII_adult = readtable('bd_typeI-typeII_CortThick_adult.csv');
        summary_stats.CortSurf_typeI_vs_typeII_adult = readtable('bd_typeI-typeII_CortSurf_adult.csv');
        summary_stats.CortThick_case_vs_controls_adolecscent = readtable('bd_case-controls_CortThick_adolescent.csv');
        summary_stats.CortSurf_case_vs_controls_adolecscent = readtable('bd_case-controls_CortSurf_adolescent.csv');
        summary_stats.CortThick_typeI_vs_typeII_adolecscent = readtable('bd_typeI-typeII_CortThick_adolescent.csv');
        summary_stats.CortSurf_case_vs_controls_adolecscent = readtable('bd_typeI-typeII_CortSurf_adolescent.csv');
        summary_stats.SubVol_case_vs_controls_typeI = readtable('bd_case-controls_SubVol_typeI.csv');
        summary_stats.SubVol_case_vs_controls_typeII = readtable('bd_case-controls_SubVol_typeII.csv');
        summary_stats.SubVol_typeII_vs_typeI = readtable('bd_typeII-typeI_SubVol.csv');
        
    case 'depression'
        
        summary_stats.CortThick_case_vs_controls_adult = readtable('mddadult_case-controls_CortThick.csv');
        summary_stats.CortSurf_case_vs_controls_adult = readtable('mddadult_case-controls_CortSurf.csv');
        summary_stats.CortThick_case_vs_controls_adult_firstepisode = readtable('mddadult_case-controls_CortThick_firstepisode.csv');
        summary_stats.CortSurf_case_vs_controls_adult_firstepisode  = readtable('mddadult_case-controls_CortSurf_firstepisode.csv');
        summary_stats.CortThick_case_vs_controls_adult_recurrent  = readtable('mddadult_case-controls_CortThick_recurrent.csv');
        summary_stats.CortSurf_case_vs_controls_adult_recurrent  = readtable('mddadult_case-controls_CortSurf_recurrent.csv');
        summary_stats.CortThick_firstepisode_vs_recurrent_adult  = readtable('mddadult_firstepisode-recurrent_CortThick.csv');
        summary_stats.CortSurf_firstepisode_vs_recurrent_adult  = readtable('mddadult_firstepisode-recurrent_CortSurf.csv');
        summary_stats.CortThick_case_vs_controls_adult_early  = readtable('mddadult_case-controls_CortThick_early.csv');
        summary_stats.CortSurf_case_vs_controls_adult_early  = readtable('mddadult_case-controls_CortSurf_early.csv');
        summary_stats.CortThick_case_vs_controls_adult_late  = readtable('mddadult_case-controls_CortThick_late.csv');
        summary_stats.CortSurf_case_vs_controls_adult_late  = readtable('mddadult_case-controls_CortSurf_late.csv');
        summary_stats.CortThick_early_vs_late_adult  = readtable('mddadult_early-late_CortThick.csv');
        summary_stats.CortSurf_early_vs_late_adult  = readtable('mddadult_early-late_CortSurf.csv');        
        
        summary_stats.CortThick_case_vs_controls_adolescent = readtable('mddadolescent_case-controls_CortThick.csv');
        summary_stats.CortSurf_case_vs_controls_adolescent = readtable('mddadolescent_case-controls_CortSurf.csv');
        summary_stats.CortThick_case_vs_controls_adolescent_firstepisode = readtable('mddadolescent_case-controls_CortThick_firstepisode.csv');
        summary_stats.CortSurf_case_vs_controls_adolescent_firstepisode  = readtable('mddadolescent_case-controls_CortSurf_firstepisode.csv');
        summary_stats.CortThick_case_vs_controls_adolescent_recurrent  = readtable('mddadolescent_case-controls_CortThick_recurrent.csv');
        summary_stats.CortSurf_case_vs_controls_adolescent_recurrent  = readtable('mddadolescent_case-controls_CortSurf_recurrent.csv');
        summary_stats.CortThick_firstepisode_vs_recurrent_adolescent  = readtable('mddadolescent_firstepisode-recurrent_CortThick.csv');
        summary_stats.CortSurf_firstepisode_vs_recurrent_adolescent  = readtable('mddadolescent_firstepisode-recurrent_CortSurf.csv');
        
        summary_stats.SubVol_case_vs_controls = readtable('mdd_case-controls_SubVol.csv');
        summary_stats.SubVol_case_vs_controls_late = readtable('mddlate_case-controls_SubVol.csv');
        summary_stats.SubVol_case_vs_controls_early = readtable('mddlate_case-controls_SubVol.csv');
        summary_stats.SubVol_late_vs_early = readtable('mdd_late-early_SubVol.csv');
        summary_stats.SubVol_case_vs_controls_firstepisode = readtable('mddfirstepisode_case-controls_SubVol.csv');
        summary_stats.SubVol_case_vs_controls_recurrent = readtable('mddrecurrent_case-controls_SubVol.csv');
        summary_stats.SubVol_recurrent_vs_firstepisode = readtable('mdd_recurrent-firstepisode_SubVol.csv');
          
    case 'epilepsy'
        summary_stats.CortThick_case_vs_controls_allepilepsy = readtable('allepi_case-controls_CortThick.csv');
        summary_stats.SubVol_case_vs_controls_allepilepsy = readtable('allepi_case-controls_SubVol.csv');
        summary_stats.CortThick_case_vs_controls_gge = readtable('gge_case-controls_CortThick.csv');
        summary_stats.SubVol_case_vs_controls_gge = readtable('gge_case-controls_SubVol.csv');
        summary_stats.CortThick_case_vs_controls_ltle = readtable('tlemtsl_case-controls_CortThick.csv');
        summary_stats.SubVol_case_vs_controls_ltle = readtable('tlemtsl_case-controls_SubVol.csv');
        summary_stats.CortThick_case_vs_controls_rtle = readtable('tlemtsr_case-controls_CortThick.csv');
        summary_stats.SubVol_case_vs_controls_rtle = readtable('tlemtsr_case-controls_SubVol.csv');
        summary_stats.CortThick_case_vs_controls_allotherepilepsy = readtable('allotherepi_case-controls_CortThick.csv');
        summary_stats.SubVol_case_vs_controls_allotherepilepsy = readtable('allotherepi_case-controls_SubVol.csv');
            
    case 'ocd'
        summary_stats.CortThick_case_vs_controls_adult = readtable('ocdadults_case-controls_CortThick.csv');
        summary_stats.CortSurf_case_vs_controls_adult = readtable('ocdadults_case-controls_CortSurf.csv');
        summary_stats.CortThick_medicatedcase_vs_controls_adult = readtable('ocdadults_medicatedcase-controls_CortThick.csv');
        summary_stats.CortSurf_medicatedcase_vs_controls_adult = readtable('ocdadults_medicatedcase-controls_CortSurf.csv');
        summary_stats.CortThick_case_vs_controls_pediatric = readtable('ocdpediatric_case-controls_CortThick.csv');
        summary_stats.CortSurf_case_vs_controls_pediatric = readtable('ocdpediatric_case-controls_CortSurf.csv');
        summary_stats.CortThick_medicatedcase_vs_controls_pediatric = readtable('ocdpediatric_medicatedcase-controls_CortThick.csv');
        summary_stats.CortSurf_medicatedcase_vs_controls_pediatric = readtable('ocdpediatric_medicatedcase-controls_CortSurf.csv');
        
        summary_stats.SubVol_case_vs_controls_adult = readtable('ocdadult_case-controls_SubVol.csv');
        summary_stats.SubVol_medicatedcase_vs_controls_adult = readtable('ocdadult_medicatedcase-controls_SubVol.csv');
        summary_stats.SubVol_unmedicatedcase_vs_controls_adult = readtable('ocdadult_unmedicatedcase-controls_SubVol.csv');
        summary_stats.SubVol_medicatedcase_vs_unmedicated_adult = readtable('ocdadult_medicatedcase-unmedicatedcase_SubVol.csv');
        summary_stats.SubVol_case_vs_controls_adult_late = readtable('ocdadult_case-controls_SubVol_late.csv');
        summary_stats.SubVol_case_vs_controls_adult_early = readtable('ocdadult_case-controls_SubVol_early.csv');
        summary_stats.SubVol_late_vs_early_adult = readtable('ocdadult_late-early_SubVol.csv');
        summary_stats.SubVol_case_vs_controls_adult_depression = readtable('ocdadult_case-controls_SubVol_depression.csv');
        summary_stats.SubVol_case_vs_controls_adult_nodepression = readtable('ocdadult_case-controls_SubVol_nodepression.csv');
        summary_stats.SubVol_depression_vs_nodepression_adult = readtable('ocdadult_depression-nodepression_SubVol.csv');
        summary_stats.SubVol_case_vs_controls_adult_anxiety = readtable('ocdadult_case-controls_SubVol_anxiety.csv');
        summary_stats.SubVol_case_vs_controls_adult_noanxiety = readtable('ocdadult_case-controls_SubVol_noanxiety.csv');
        summary_stats.SubVol_anxiety_vs_noanxiety_adult = readtable('ocdadult_anxiety-noanxiety_SubVol.csv');
        
        summary_stats.SubVol_case_vs_controls_pediatric = readtable('ocdpediatric_case-controls_SubVol.csv');
        summary_stats.SubVol_medicatedcase_vs_controls_pediatric = readtable('ocdpediatric_medicatedcase-controls_SubVol.csv');
        summary_stats.SubVol_unmedicatedcase_vs_controls_pediatric = readtable('ocdpediatric_unmedicatedcase-controls_SubVol.csv');
        summary_stats.SubVol_medicatedcase_vs_unmedicated_pediatric = readtable('ocdpediatric_medicatedcase-unmedicatedcase_SubVol.csv');
               
    case 'schizophrenia'
        summary_stats.CortThick_case_vs_controls = readtable('scz_case-controls_CortThick.csv');
        summary_stats.CortSurf_case_vs_controls = readtable('scz_case-controls_CortSurf.csv');
        summary_stats.SubVol_case_vs_controls = readtable('scz_case-controls_SubVol.csv');
        summary_stats.SubVol_case_vs_controls_mean = readtable('scz_case-controls_SubVol_mean.csv');
end

return