function [value] = calvalue(population)
% calculate the value
EI = 0.9;
ECI = 0.229 + 0.648 - EI;
value(:,1) = ECI.*0.42.*population(:,1)+0.296.*EI.*(1-population(:,1))+EI...
    .*0.165.*3.*population(:,1).*(1-population(:,1));

end


