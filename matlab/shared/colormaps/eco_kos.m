function cm_data=eco_kos(m)
cm = [0 0 0; 
        126 40 127;
        51 104 156;
        167 210 140;
        254 205 8;
        255 253 25]/255;

if nargin < 1
    cm_data = cm;
else
    hsv=rgb2hsv(cm);
    cm_data=interp1(linspace(0,1,size(cm,1)),hsv,linspace(0,1,m));
    cm_data=hsv2rgb(cm_data);
  
end
end