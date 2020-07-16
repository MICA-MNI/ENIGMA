function mask = SurfStatMaskCut( surf );

%Mask that excludes the inter-hemisphere cut.
%
% Usage: mask = SurfStatMaskCut( surf );
%
% surf.coord   = 3 x v matrix of surface coordinates, v=#vertices.
%
% mask         = 1 x v vector, 1=inside, 0=outside, v=#vertices.
%
% It looks in -50<y<50 and -20<z<40, and mask vertices where |x|>thresh,
% where thresh = 1.5 x arg max of a histogram of |x|. 

f=(abs(surf.coord(2,:))<50 ...
    & abs(surf.coord(3,:)-10)<30 ...
    & abs(surf.coord(1,:))<3);
b=(0:0.02:3);
h=hist(abs(surf.coord(1,f)),b);
t=b(find(h==max(h)))*1.5;
mask=~(abs(surf.coord(1,:))<t & f);

return
end
