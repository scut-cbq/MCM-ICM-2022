function population2 = cross(population,pc)
% cross
% pc means the probality of cross
population2 = zeros(2000,1);
iscross = rand(2000);
father = 1;
t = 0;
for i = 1:2000
    if(iscross(i)<pc)
        if(t==1)
            t = 0;
            k = randi(1);
            population2(father,:) = [population(father,1:k),population(i,k+1:1)];
            population2(i,:) = [population(i,1:k),population(father,k+1:1)];
        else
            t = 1;
            father = i;
        end
    else
            population2(i,:) = population(i,:);
    end
end
end

