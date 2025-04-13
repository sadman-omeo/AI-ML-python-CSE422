
import random

capital = 1000
historical_prices = [-1.2, 3.4, -0.8, 2.1, -2.5, 1.7, -0.3, 5.8, -1.1, 3.5]
population_size = 4
genz = 10

def chromosome():
    stop_loss = round(random.uniform(1, 99), 2)
    take_profit = round(random.uniform(1, 99), 2)
    trade_size = round(random.uniform(1, 99), 2)
    
    pop = [stop_loss, take_profit, trade_size]
    return pop
    #return [2, 5, 20] # delete this after verfication

def population_init(size = 4):
    ppp = []
    for i in range(size):
        ppp.append(chromosome())
    return ppp

def fitness(chromo):
    cap = capital
    trade_size_percent = chromo[2] / 100
    
    for pricecng in historical_prices:
        trade_amm = cap * trade_size_percent
        if pricecng < (-chromo[0]):
            #Stop loss 
            loss = trade_amm *  (chromo[0] / 100)
            cap -= loss
        
        elif pricecng > chromo[1]:
            #take profit
            profit = trade_amm * (chromo[1] / 100)
            cap += profit
        
        elif pricecng >= -chromo[0] and pricecng <= chromo[1]:
            lossorprof = trade_amm * (pricecng / 100)
            cap += lossorprof
            
        else:
            pass
    
    final_cap = round(cap, 2)
    return round(final_cap - capital, 2)

def chromosome_to_string(ch):
    str2 = ''
    for i in ch:
        if len(str(i)) == 3:
            str2 += '0' + str(i) + '0'
        if len(str(i)) == 5:
            str2 += str(i)
        else:
            if i < 10:
                str2 += '0' + str(i)
            else:
                str2 += str(i) + '0'
    str2 = str2.replace('.', '')
    return str2


def string_to_chromosome(string):
    ch = []
    for i in range(0, len(string), 4):
        num = string[i:i+4:1]
        num = num[:2] + '.' + num[2:]
        ch.append(float(num))
    
    return ch


def parents_selection(population):
    winners = random.sample(population, 2) #randomly selected 2 parents from a list of population
    return winners

def crossover(par1, par2):
    par1 = chromosome_to_string(par1)
    par2 = chromosome_to_string(par2)
    
    #single point random crossing
    
    cross_point = round(random.uniform(0, 12))
    child1 = ''
    child2 = ''
    for i in range(12):
        if i < cross_point:
            child1 += par1[i]
            child2 += par2[i]
        else:
            child1 += par2[i]
            child2 += par1[i]
    
    child1 = string_to_chromosome(child1)
    child2 = string_to_chromosome(child2)
    return child1, child2
    pass
    
    
def mutation(chromosome):
    mutation_rate = 0.05
    whattomute = [1, 2, 3] #1 for stop loss, 2 for take profit, 3 for trade size
    choose = random.sample(whattomute, 1)
    if random.random() < mutation_rate:
        if choose == 1:
            chromosome[0] = round(random.uniform(1, 99), 2)
        elif choose == 2:
            chromosome[1] = round(random.uniform(1, 99), 2)
        elif choose == 3:
            chromosome[2] = round(random.uniform(1, 99), 2)
    
    return chromosome     
        
    pass

def new_genz(population):
    new_population =  []
    while len(new_population) < population_size:
        par1, par2 = parents_selection(population)
        child1, child2 = crossover(par1, par2)
        child1 = mutation(child1)
        child2 = mutation(child2)
        new_population.append(child1)
        new_population.append(child2)
    return new_population[:population_size]
           
    pass
    


def genetic_algo():
    population_list = population_init(population_size)
    initial_population = population_list.copy()

    for i in range(genz): #loop for each generation
        fitness_scoresl = []   #resetting fitness score for each gen
        for ch in population_list:
            fitness_scoresl.append(fitness(ch))
        
        #Select best Individuals
        best_fitness = max(fitness_scoresl)
        best_index = fitness_scoresl.index(best_fitness)
        best_population = [population_list[best_index]]
        
        second_best_index = None
        for idx in range(len(fitness_scoresl)):
            if idx != best_index:
                if second_best_index == None or fitness_scoresl[idx] > fitness_scoresl[second_best_index]:
                    second_best_index = idx
        
        if second_best_index != None:
            best_population.append(population_list[second_best_index])
                    
        
        #New population
        population_list = new_genz(best_population)
    final_scores = []
    for ch in population_list:
        final_scores.append(fitness(ch))
    best_index = final_scores.index(max(final_scores))
    best_strategy = population_list[best_index]
    best_fitness = final_scores[best_index]
        
    print(f"Best Strategy: {best_strategy}\nFinal Profit: ${best_fitness}")
    return best_strategy, best_fitness, initial_population

#Driver for part 1
best_strategy, best_fitness, initial_population = genetic_algo()

#part 2


def two_point_crossover(initial_pop):
    par1, par2 = parents_selection(initial_pop)
    str1 = chromosome_to_string(par1)
    str2 = chromosome_to_string(par2)

    #time to crossover
    cross_point1 = round(random.uniform(0, 12))
    cross_point2 = round(random.uniform(0, 12))
    cross_list = [cross_point1, cross_point2]
    cross_list.sort()
    cross_point1 = cross_list[0]
    cross_point2 = cross_list[1]
    child1 = ''
    child2 = ''
    for i in range(12):
        if i < cross_point1 or i > cross_point2:
            child1 += str1[i]
            child2 += str2[i]
        else:
            child1 += str2[i]
            child2 += str1[i]
    
    child1 = string_to_chromosome(child1)
    child2 = string_to_chromosome(child2)
    print(f"Selected parents(chromosome) are:\n {par1}, {par2}")
    print(f"Their resulting Offsprings are:\nChild 1: {child1}, Child 2: {child2}")
    
#Driver for part 2
print()
print('Part 2')
two_point_crossover(initial_population)

    
    