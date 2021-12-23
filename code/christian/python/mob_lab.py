years_counter = 0
population = [0,0]
while len(population) < 1000:
    years_counter += 1
    for i, age in enumerate(population):
        population[i] = age + 1
    for age in population:
        if age in range(4,8):
            population.append(0)
    for age in population:
        if age == 10:
            population.remove(age)
print(f'It takes {years_counter} to reproduce {len(population)} jackalopes.')


    