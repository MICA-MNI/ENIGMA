function [sc, fc] = load_connectivity()
%
% Simple script to load connectivity data
%
%
sc = load('hcp_structural_data.mat');
sc = sc.hcpStruc;
fc = load('hcp_functional_data.mat');
fc = fc.hcpFunc;
return