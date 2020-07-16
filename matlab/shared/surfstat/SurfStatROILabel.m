function ROI = SurfStatROILabel( lhlabel, rhlabel, nl, nr );

%ROI from a FreeSurfer .label file.
%
% Usage: ROI = SurfStatROILabel( lhlabel [, rhlabel [, nl, nr]] );
%
% lhlabel = FreeSurfer .label file for the left  hemisphere, or empty [].
% rhlabel = FreeSurfer .label file for the right hemisphere, or empty [].
% nl       = number of vertices in the left  hemisphere, 163842 by default.
% nr       = number of vertices in the right hemisphere, 163842 by default.
%
% ROI = 1 x (nl+nr) logical vector, 1=labelled point, 0=otherwise.

if nargin<2
    rhlabel=[];
end
if nargin<3 | isempty(nl)
    nl=163842;
end
if nargin<4 | isempty(nr)
    nr=163842;
end
ROI=logical(zeros(1,nl+nr));

if ~isempty(lhlabel)
    [v,x,y,z,t]=textread(lhlabel,'%f %f %f %f %f','headerlines',2);
    ROI(v)=1;
end

if ~isempty(rhlabel)
    [v,x,y,z,t]=textread(rhlabel,'%f %f %f %f %f','headerlines',2);
    ROI(v+nl)=1;
end

return
end



