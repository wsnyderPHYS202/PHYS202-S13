experiment = importdata('radioactivedecay.dat')
t = experiment.data(:,1);
N = experiment.data(:,2);
disp(t)
disp(N)
figure(42)
plot(t,N,'.b')
tdata = [2 3 4 5 6 7 8 9 10 11 12 13 14 15];
Ndata = [5.49 4.02 2.74 2.02 1.5 1.09 0.68 0.57 0.37 0.31 0.19 0.15 0.13 0.11];
%%
hold on
func = @(x) 1./x;
fittedmodel = fit(t',N',func,'StartPoint',[15 0 15])
%plot(fittedmodel,'r-');
hold off