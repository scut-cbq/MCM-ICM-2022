function population2 = selection(population,value)
% selection
population2 = zeros(2000,1);
totalvalue = sum(value);
value_proportion = value./totalvalue;
plate = cumsum(value_proportion);
ms = sort(rand(2000,1));
nowstate = 1;
i = 1;
while i<=2000
    if(ms(i)<plate(nowstate))
        population2(i,:) = population(nowstate,:);
        i = i+1;
    else
        nowstate = nowstate + 1;
        if(nowstate>2000)
            nowstate = 2000;
        end
    end
end
end

