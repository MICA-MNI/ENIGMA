function perm_id = rotate_parcellation(coord_l, coord_r, nrot)
%
% Usage:
%   perm_id = rotate_parcellation(coord_l, coord_r, nrot)
%
% Description:
%   Rotate parcellation (authors: @frantisekvasa, @saratheriver)
%
% Inputs:
%   coord_l (double array) - Coordinates of left hemisphere regions on the sphere, size = [m x 3]
%   coord_r (double array) - Coordinates of right hemisphere regions on the sphere, size = [m x 3]
%   nrot (int, optional) - Number of rotations. Default is 1000.
%
% Outputs:
%   perm_id (double array) - Array of permutations, size = [m x nrot]
%
% References:
%   Alexander-Bloch A, Shou H, Liu S, Satterthwaite TD, Glahn DC, Shinohara RT, 
%       Vandekar SN and Raznahan A (2018). On testing for spatial correspondence 
%       between maps of human brain structure and function. NeuroImage, 178:540-51.
%   Vása F, Seidlitz J, Romero-Garcia R, Whitaker KJ, Rosenthal G, Vértes PE, 
%       Shinn M, Alexander-Bloch A, Fonagy P, Dolan RJ, Goodyer IM, the NSPN 
%       consortium, Sporns O, Bullmore ET (2017). Adolescent tuning of association 
%       cortex in human structural brain networks. Cerebral Cortex, 28(1):281?294.
%
% Sara Lariviere  |  saratheriver@gmail.com

% check that coordinate dimensions are correct
if or(size(coord_l,2)~=3,size(coord_r,2)~=3)
   if and(size(coord_l,1)==3,size(coord_r,1)==3)
       disp('transposing coordinates to be of dimension nROI x 3')
       coord_l = coord_l';
       coord_r = coord_r';
   end
end

% default number of rotations
if nargin < 3
    nrot = 1000;
end

nroi_l = size(coord_l,1);   % n(regions) in the left hemisphere
nroi_r = size(coord_r,1);   % n(regions) in the right hemisphere
nroi = nroi_l+nroi_r;       % total n(regions)

perm_id = zeros(nroi,nrot); % initialise output array
r = 0; c = 0; % count successful (r) and unsuccessful (c) iterations

% UPDATED 5/9/2019 - set up updated permutation scheme 
I1 = eye(3,3); I1(1,1) = -1;
% main loop -  use of "while" is to ensure any rotation that maps to itself is excluded (this is rare, but can happen)
while (r < nrot)

    % UPDATED 5/9/2019 - uniform sampling procedure
    A = normrnd(0,1,3,3);
    [TL, temp] = qr(A);
    TL = TL*diag(sign(diag(temp)));
    if(det(TL)<0)
        TL(:,1) = -TL(:,1);
    end
    % reflect across the Y-Z plane for right hemisphere
    TR = I1 * TL * I1;
    coord_l_rot = coord_l * TL;
    coord_r_rot = coord_r * TR;
    
    % after rotation, find "best" match between rotated and unrotated coordinates
    % first, calculate distance between initial coordinates and rotated ones
    dist_l = zeros(nroi_l);
    dist_r = zeros(nroi_r);
    % UPDATED 5/9/2019 - change of rotated variable name to "coord_l/r_rot" (from coord_l/r_rot_xyz)
    for i = 1:nroi_l; for j = 1:nroi_l; dist_l(i,j) = sqrt(sum((coord_l(i,:)-coord_l_rot(j,:)).^2)); end; end % left
    for i = 1:nroi_r; for j = 1:nroi_r; dist_r(i,j) = sqrt(sum((coord_r(i,:)-coord_r_rot(j,:)).^2)); end; end % right
    
    % LEFT
    % calculate distances, proceed in order of "most distant minimum"
    % -> for each unrotated region find closest rotated region (minimum), then assign the most distant pair (maximum of the minima), 
    % as this region is the hardest to match and would only become harder as other regions are assigned
    temp_dist_l = dist_l;
    rot_l = []; ref_l = [];
    for i = 1:1:nroi_l
        % max(min) (described above)
        ref_ix = find(nanmin(temp_dist_l,[],2)==max(nanmin(temp_dist_l,[],2)));     % "furthest" row
        rot_ix = find(temp_dist_l(ref_ix,:)==nanmin(temp_dist_l(ref_ix,:)));        % closest region
        % % alternative option: mean of row - take the closest match for unrotated region that is on average furthest from rotated regions
        % ref_ix = find(nanmean(temp_dist_l,2)==nanmax(nanmean(temp_dist_l,2)));    % "furthest" row
        % rot_ix = find(temp_dist_l(ref_ix,:)==nanmin(temp_dist_l(ref_ix,:)));      % closest region    
        ref_l = [ref_l ref_ix]; % store reference and rotated indices
        rot_l = [rot_l rot_ix];
        temp_dist_l(:,rot_ix) = NaN; % set temporary indices to NaN, to be disregarded in next iteration
        temp_dist_l(ref_ix,:) = NaN;
    end
    
    % RIGHT
    % calculate distances, proceed in order of "most distant minimum"
    % -> for each unrotated region find closest rotated region (minimum), then assign the most distant pair (maximum of the minima), 
    % as this region is the hardest to match and would only become harder as other regions are assigned
    temp_dist_r = dist_r;
    rot_r = []; ref_r = [];
    for i = 1:1:nroi_r
        % max(min) (described above)
        ref_ix = find(nanmin(temp_dist_r,[],2)==max(nanmin(temp_dist_r,[],2)));     % "furthest" row
        rot_ix = find(temp_dist_r(ref_ix,:)==nanmin(temp_dist_r(ref_ix,:)));        % closest region
        % % alternative option: mean of row - take the closest match for unrotated region that is on average furthest from rotated regions
        % ref_ix = find(nanmean(temp_dist_r,2)==nanmax(nanmean(temp_dist_r,2)));    % "furthest" row
        % rot_ix = find(temp_dist_r(ref_ix,:)==nanmin(temp_dist_r(ref_ix,:)));      % closest region
        ref_r = [ref_r ref_ix]; % store reference and rotated indices
        rot_r = [rot_r rot_ix];
        temp_dist_r(:,rot_ix) = NaN; % set temporary indices to NaN, to be disregarded in next iteration
        temp_dist_r(ref_ix,:) = NaN;
    end
    
    % mapping is x->y
    % collate vectors from both hemispheres + sort mapping according to "reference" vector
    ref_lr = [ref_l,nroi_l+ref_r]; 
    rot_lr = [rot_l,nroi_l+rot_r];
    [b,ix] = sort(ref_lr); 
    rot_lr_sort = rot_lr(ix);
    
    % verify that permutation does not map to itself
    if ~all(rot_lr_sort==1:nroi)
        r = r+1;
        perm_id(:,r) = rot_lr_sort; % if it doesn't, store it
    else
        c = c+1;
        disp(['map to itself n.' num2str(c)])
    end
    
    % track progress
    if mod(r,100)==0; 
        disp(['permutation ' num2str(r) ' of ' num2str(nrot)]); 
    end
    
end

return
