Mf = 5;         %Celcius degree
Ms = 23;        %Celcius degree
As = 29;        %Celcius degree
Af = 51;        %Celcius degree
Ca = 4.5;       %MPa/Celcius degree
Cm = 11.3;      %MPa
Ya = 32500;     %GPa
Ym = 13000;     %GPa
Sl = 0.07;      % 7% maximum strain 
Pi = 3.1416;
T_cr_s = 100;   % MPa
T_cr_f = 170;   % MPa
% Predict T-S curve for SMA at isothermal Condition;
theta = 52;
% 1. What is SMA's behaviour at the given condition ?
%  Could be super elastic due to the theta given greater than Af
% 2. Draw stress cycle on the phase diagram
% 3. Sketch graphically T-S curve with different specific regions?
% 4. Evaluate stress  at the transitional points n the T-S curve


Td = linspace(0,427.7,20);
Sd = Td/Ya;


figure;
plot(Sd, Td);

function y = nitiM2A(x, Ms, Mf,theta)
    stress = theta;
    stress0 = 
    am = pi/(Ms - Mf);
    
    angel = am
    y(1) = Y*(s - SL*shi) - Y0*(s0 - SL*shi0) - (stress - stress0);
    y(2) = shi -0.5*(cos(angle) + 1);
end


initA2M = (1/2)*((cos
initM2A = (1/2)*(cos(am*(theta-Mf) - am/Cm*T) + 1/2