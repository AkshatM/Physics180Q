% Another attempt at threshold current determination

% For F0000CH2.csv

data1 = 1000*csvread('F0000CH1.csv',19,0);
data2 = 1000*csvread('F0000CH2.csv',19,0);

data1(:,5) = data1(:,5)-nanmean(data1(:,5));

slice_step = 100;

% Fourth column corresponds to channel 1; fifth column to channel 2

smooth_data = interp1(data2(1:slice_step:end,4),data2(1:slice_step:end,5),data2(:,4));
current = 18.06 + (50/10)*(1/1000)*data1(:,5);

figure(1)
subplot(1,2,1)
plot(data1(:,5),'b')
title('Threshold Current Determination')
xlabel('Time (default Tektronix units)')
ylabel('Channels (mV)')
hold on
plot(data2(:,5),'r')
legend('Channel 1', 'Channel 2', 'location', 'northwest')
hold off
subplot(1,2,2)
plot(current,data2(:,5),'b')
title('Threshold Current Determination')
xlabel('Current (mA)')
ylabel('Channel 2 (mV)')
hold on
slope = diff(smooth_data)./diff(data1(:,5));
%points_of_change = find(slope == max(slope));
plot(current,smooth_data,'r')
%plot(data1(points_of_change,5),smooth_data(points_of_change),'ko')
legend('Channel 2', 'Smoothed Channel 2', 'location','northeast')
hold off

%%

data1 = 1000*csvread('F0003CH1.csv',19,0);
data2 = 1000*csvread('F0003CH2.csv',19,0);

slice_step = 100;
data1(2104:2353,5) = NaN;
data2(2104:2353,5) = NaN;

data1(:,5) = data1(:,5)-nanmean(data1(:,5));

% Fourth column corresponds to channel 1; fifth column to channel 2

smooth_data = interp1(data2(1:slice_step:end,4),data2(1:slice_step:end,5),data2(:,4));
current = 18.06 + (50/10)*(1/1000)*data1(:,5);
disp(current(683))

figure(2)
subplot(1,3,1)
plot(data1(:,5),'b')
title('Channels vs. Time')
xlabel('Time (default Tektronix units)')
ylabel('Channels (mV)')
hold on
plot(data2(:,5),'r')
legend('Channel 1', 'Channel 2', 'location', 'northwest')
hold off
subplot(1,3,2)
plot(current,data2(:,5),'b')
title('Parametric Plot - Voltage vs. Current')
xlabel('Current (mA)')
ylabel('Channel 2 (mV)')
hold on
slope = diff(smooth_data)./diff(data1(:,5));
plot(current,smooth_data,'r')
legend('Channel 2', 'Smoothed Channel 2', 'location','northeast')
hold off
subplot(1,3,3)
plot(data1(:,5),data2(:,5),'b')
title('Parametric Plot - Voltage vs. Voltage')
xlabel('Channel 1 (mV)')
ylabel('Channel 2 (mV)')
hold on
plot(data1(:,5),smooth_data,'r')
slope = diff(smooth_data)./diff(data(:,5));
plot(data1(slope == max(slope)+1,5),smooth_data(slope == max(slope)+1),'k')
legend('Channel 2', 'Smoothed Channel 2', 'location','northeast')
hold off


