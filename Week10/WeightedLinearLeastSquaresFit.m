function [ m,unm,b,unb ] = WeightedLinearLeastSquaresFit( w,x,y )
%WeigthedLinearLeastSquaresFit(w,x,y)
%Take in arrays representing (x,y) values for a set of linearly varying 
%data and an array of weights w and perform a weighted linear least squares
%regression. Return the resulting slope and intercept parameters of the 
%best fit line with their uncertainties.
W = sum(sum(w))
WXY = sum(sum(w.*x.*y))
WX = sum(sum(w.*x))
WY = sum(sum(w.*y))
WXsq = sum(sum(w.*(x.^2)))
    
m = (W.*WXY-WX.*WY)./(W.*WXsq-(WX.^2))
b = (WXsq.*WY-WX.*WXY)./(W.*WXsq-(WX).^2)
    
unm = (W./(W.*WXsq-(WX.^2))).^(.5)
unb = (WXsq./(W.*WXsq-(WX.^2))).^(.5)
    
%return m,unm,b,unb

end

