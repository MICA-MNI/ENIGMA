function X = chop(Xin,n,unit)
%CHOP   CHOP(X,n) rounds elements of X to n significant figures.
%       CHOP(X,n,unit) rounds the elements of X to n significant
%   figures whose digits (mantissa) are exactly divisible
%   by unit. 
%       
%       e.g. chop(3.141592,5)   returns 3.141600000..
%       e.g. chop(3.141592,3,5) returns 3.150000000..
%            chop(3.141592,3,3) returns 3.150000000..
%            chop(3.141592,3,2) returns 3.140000000..
%      

%   Copyright 1986-2002 The MathWorks, Inc. 

% Set last sig. fig. rounding to 1 if only two input arguments.
if nargin<3,
   unit=1; 
end

% Cater for -ve numbers  and numbers = 0.
X = abs(Xin) +(Xin==0);
[nx,mx] = size(X);
exponent = unit.*((10*ones(nx,mx)).^(floor(log10(X))-n+1));
X = round(X./exponent).*exponent;

% Put back sign and zeros
X = sign(Xin).*X.*(Xin~=0);

% end chop
