import random
def create_chromosome():
    stop_loss = round(random.uniform(1, 99),2)  # Random stop-loss between 1% and 99%
    take_profit = round(random.uniform(1, 99),2)  # Random take-profit between 1% and 99%
    trade_size = round(random.uniform(1, 99), 2)  # Random trade size between 1% and 99%
    return [stop_loss,take_profit,trade_size]

# Step 2: Initialize Population
def initialize_population(size):
    return [create_chromosome() for _ in range(size)]

ppp = initialize_population(4)

print(ppp)

print()

print(random.sample([1,2,3,4, 5, 6], 2))

print(round(random.uniform(0, 2)))
ll = [1.11, 2.20]
for i in ll:
    print(i)