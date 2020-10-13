function perm_id = rotate_parcellation(coord_l, coord_r, nrot)

% Function to generate a permutation map from a set of cortical regions of interest to itself, 
% while (approximately) preserving contiguity and hemispheric symmetry.
% The function is based on a rotation of the FreeSurfer projection of coordinates
% of a set of regions of interest on the sphere.
%
% Inputs:
% coord_l       coordinates of left hemisphere regions on the sphere        array of size [n(LH regions) x 3]
% coord_r       coordinates of right hemisphere regions on the sphere       array of size [n(RH regions) x 3]
% nrot          number of rotations (default = 10'000)                      scalar
%
% Output:
% perm_id      array of permutations, from set of regions to itself        array of size [n(total regions) x nrot]
%
% František Váša, fv247@cam.ac.uk, June 2017 - June 2018
%       Updated on 5/9/2019 with permutation scheme that uniformly samples the space of permutations on the sphere
%       See github repo (@frantisekvasa) and references within for details

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
    nrot = 100;
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
