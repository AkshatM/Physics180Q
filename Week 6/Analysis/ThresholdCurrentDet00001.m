% This script reproduces the data we need for threshold current determination

% For TEK0001.csv

data = 1000*csvread('TEK0001.csv',19,0);
slice_step = 100;

% Fourth column corresponds to channel 1; fifth column to channel 2

smooth_data = interp1(data(1:slice_step:end,4),data(1:slice_step:end,5),data(:,4));
current = 18.06 + (50/10)*(1/1000)*data(:,4);

figure(1)
subplot(1,2,1)
plot(data(:,4),'b')
title('Threshold Current Determination')
xlabel('Time (default Tektronix units)')
ylabel('Channels (mV)')
hold on
plot(data(:,5),'r')
legend('Channel 1', 'Channel 2', 'location', 'northwest')
hold off
subplot(1,2,2)
plot(current,data(:,5),'b')
title('Threshold Current Determination')
xlabel('Current (mA)')
ylabel('Channel 2 (mV)')
hold on
slope = diff(smooth_data)./diff(current);
points_of_change = find(slope == max(slope));
plot(current,smooth_data,'r')
plot(current(points_of_change),smooth_data(points_of_change),'ko')
legend('Channel 2', 'Smoothed Channel 2', 'location','northwest')
hold off

