A1 = normrnd(0,1);
A2 = normrnd(0,1);
A3 = normrnd(0,1);
A4 = normrnd(0,1);
A5 = normrnd(0,1);

f = 0.1;

t = 0:0.1:25;

figure;
plot(t, A1*sin(2*pi*f*t)); hold on;
plot(t, A2*sin(2*pi*f*t)); 
plot(t, A3*sin(2*pi*f*t)); 
plot(t, A4*sin(2*pi*f*t)); 
plot(t, A5*sin(2*pi*f*t)); hold off;

xlabel('time');
ylabel('amplitude');
