% This script reproduces figures for above and below threshold spectrum
% measurements, as well as temperature-current variations

data = csvread('Lab6AxHanwen-BelThresh.csv',19,0);
% First column corresponds to wavelength (x-axis); second column to
% intensity

desired_range = data(:,1) < 665 & data (:,1) > 645;

figure(1)
plot(data(desired_range,1),(1/10000)*data(desired_range,2))
xlabel('Wavelength (nm)')
ylabel('Intensity divided by 10k (arbitrary units)')
title('Spectrum at 16.61 mA')
hold off

saveas(gcf,'BelThresh1.png')

data = csvread('Lab6AxHanwen-BelThresh2.csv',19,0);
% First column corresponds to wavelength (x-axis); second column to
% intensity

desired_range = data(:,1) < 665 & data (:,1) > 645;

figure(2)
plot(data(desired_range,1),(1/10000)*data(desired_range,2))
xlabel('Wavelength (nm)')
ylabel('Intensity divided by 10k (arbitrary units)')
title('Spectrum at 16.43 mA')
hold off

saveas(gcf,'BelThresh2.png')

% This script reproduces figures for above and below threshold spectrum
% measurements

data = csvread('Lab6AxHanwen-AboThresh.csv',19,0);
% First column corresponds to wavelength (x-axis); second column to
% intensity

desired_range = data(:,1) < 665 & data (:,1) > 645;

figure(3)
plot(data(desired_range,1),(1/10000)*data(desired_range,2))
xlabel('Wavelength (nm)')
ylabel('Intensity divided by 10k (arbitrary units)')
title('Spectrum at 19.06 mA')
hold off

saveas(gcf,'AboThresh.png')

%% TEMPERATURE-CURRENT Variations

data = csvread('Lab6AxHanwen-15mAT10p643.csv',19,0);
% First column corresponds to wavelength (x-axis); second column to
% intensity

temperature = 3977/(log(11/10) + (3977/298));

desired_range = data(:,1) < 665 & data (:,1) > 645;

figure(4)
plot(data(desired_range,1),(1/10000)*data(desired_range,2))
xlabel('Wavelength (nm)')
ylabel('Intensity divided by 10k (arbitrary units)')
title(['Spectrum at 15 mA and temperature ' num2str(temperature) ' K'])
hold off

%saveas(gcf,'15mAT10p643.png')


% data = csvread('Lab6AxHanwen-16p04mAT10p643.csv',19,0);
% 
% temperature = 3977/(log(10.643/10) + (3977/298));
% 
% desired_range = data(:,1) < 665 & data (:,1) > 645;
% 
% figure(5)
% plot(data(desired_range,1),(1/10000)*data(desired_range,2))
% xlabel('Wavelength (nm)')
% ylabel('Intensity divided by 10k (arbitrary units)')
% title(['Spectrum at 16.04 mA and temperature ' num2str(temperature) ' K'])
% hold off
% 
% saveas(gcf,'16p04mAT10p643.png')
% 
% 
% data = csvread('Lab6AxHanwen-17mAT9p214.csv',19,0);
% 
% temperature = 3977/(log(9.214/10) + (3977/298));
% 
% desired_range = data(:,1) < 665 & data (:,1) > 645;
% 
% figure(6)
% plot(data(desired_range,1),(1/10000)*data(desired_range,2))
% xlabel('Wavelength (nm)')
% ylabel('Intensity divided by 10k (arbitrary units)')
% title(['Spectrum at 17 mA and temperature ' num2str(temperature) ' K'])
% hold off
% 
% saveas(gcf,'17mAT9p214.png')
% 
% 
% 
% 
% data = csvread('Lab6AxHanwen-18mAT9p214.csv',19,0);
% 
% temperature = 3977/(log(9.214/10) + (3977/298));
% 
% desired_range = data(:,1) < 665 & data (:,1) > 645;
% 
% figure(7)
% plot(data(desired_range,1),(1/10000)*data(desired_range,2))
% xlabel('Wavelength (nm)')
% ylabel('Intensity divided by 10k (arbitrary units)')
% title(['Spectrum at 18 mA and temperature ' num2str(temperature) ' K'])
% hold off
% 
% saveas(gcf,'18mAT9p214.png')
% 
% 
% data = csvread('Lab6AxHanwen-18mAT10p643.csv',19,0);
% 
% temperature = 3977/(log(10.643/10) + (3977/298));
% 
% desired_range = data(:,1) < 665 & data (:,1) > 645;
% 
% figure(8)
% plot(data(desired_range,1),(1/10000)*data(desired_range,2))
% xlabel('Wavelength (nm)')
% ylabel('Intensity divided by 10k (arbitrary units)')
% title(['Spectrum at 18 mA and temperature ' num2str(temperature) ' K'])
% hold off
% 
% saveas(gcf,'18mAT10p643.png')
% 
