function population2 = mutation(population,pm)
% mutation
% pm means the probablity of mutation 
population2 = population;
ismutation = rand(2000,1);
for i=1:2000
    for j=1:1
        if(ismutation(i,j)<pm)
            population2(i,j) = rand;
        end
    end
end
end

