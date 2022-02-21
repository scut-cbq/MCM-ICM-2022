% set the params
pc = 0.7;
pm = 0.07;
% init
population = rand(2000,1);
[value] = calvalue(population);
[final_value,final_index] = max(value);
final_answer = population(final_index,:);
for i = 1:1000 
    population = selection(population,value); % selection
	population = mutation(population,pm); % mutation
	[value] = calvalue(population);
	[max_value,max_index] = max(value);
	max_answer = population(max_index,:);
	if(final_value<max_value)
        final_value = max_value;
        final_answer = max_answer; 
    end
end

    