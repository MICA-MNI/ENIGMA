function joint_var_matrix = structural_covariance(data)
%
%   HELLO!
%
%   joint_var_matrix = structural_covariance(data)
%
%   Construction of intra-individual brain structural covariance networks
%   Based on Yun et al., 2020, Brain  
%
%   INPUT:
%       data                  = z-scored matrix of morphological features
%                               (e.g., cortical thickness + subcortical
%                               volume) 
%                               Matrix size is #subject x #features
%  
%   OUTPUT:
%       joint_var_matrix      = #parcels x #parcels x #subjects  

%   A hot and humid July 2020 day
%   Sara Lariviere | saratheriver@gmail.com

%% joint variation matrix
joint_var_matrix = zeros(size(data, 2), size(data, 2), size(data, 1));
for kk = 1:size(data, 1)
   for ii = 1:size(data, 2)
      for jj = 1:size(data, 2)
          joint_var_matrix(ii, jj, kk) = 1 / exp((data(kk, ii) - data(kk, jj))^2);
      end
   end
end

end