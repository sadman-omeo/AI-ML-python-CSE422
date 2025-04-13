import random
import math

def strength(a):
    calc = math.log2(a + 1) + a/10
    return calc

def utility(maxV, minV, i):
    calc = (strength(maxV) - strength(minV) + (-1)**i * (random.randint(1, 10) / 10))
    return calc

def alpha_beta_minimax(depth, is_max, alpha, beta, maxV, minV):
    if depth == 0: #Leaf node
        a = random.randint(0, 1)
        return utility(maxV, minV, a)
    
    if is_max == True:
        maxpoint = float('-inf')
        for i in range(0, 2, 1): # sice two moves
            new_maxp = alpha_beta_minimax(depth - 1, False, alpha, beta, maxV, minV)
            maxpoint = max(maxpoint, new_maxp)
            alpha = max(new_maxp, alpha)
                
            if alpha >= beta:
                break # break when a >= b
        
        return maxpoint 
    
    else:
        minpoint =  float('inf')
        for i in range(0, 2, 1):
            new_minp = alpha_beta_minimax(depth - 1, True, alpha, beta, maxV, minV)
            minpoint = min(minpoint, new_minp)
            beta = min(beta, new_minp)
            if alpha >= beta:
                break #pruning/cutoff
        
        return minpoint


def gameplay(starting_p, maxV, minV):
    
    if starting_p == 0:  #Carlsen is max 
        winner_val = alpha_beta_minimax(5, True, float('-inf'), float('inf'), maxV, minV)
    
        if winner_val > 0:
            winner = 'Magnus Carlsen (Max)'
        elif winner_val == 0:
            winner = 'Draw'
        else:
            winner = 'Fabiano Caruana (Min)'
    
    else: #Fabiano is max
        winner_val = alpha_beta_minimax(5, True, float('-inf'), float('inf'), minV, maxV)
        
        if winner_val > 0:
            winner = 'Fabiano Caruana (Max)'
        elif winner_val == 0:
            winner = 'Draw'
        else:
            winner = 'Magnus Carlsen (Min)'
    
    return winner_val, winner



##  DRIVER CODE  ##

result = []
draw = 0
carlsen_wins = 0
caruana_wins = 0

starting_p = int(input("Enter starting player for game-1 [0 for Magnus Carlsen, 1 for Fabiano Caruana]: "))
maxV = float(input("Enter base strength for Magnus Carlsen: "))
minV = float(input('Enter base strength for Fabiano Caruana: '))

#game starts

for game in range(0, 4, 1):
    if game % 2 == 0:
        win_val, winner = gameplay(starting_p, maxV, minV)
    else:
        win_val, winner = gameplay(1 - starting_p, maxV, minV)
    
    temp = (winner, win_val)
    result.append(temp)
    
    if 'Magnus Carlsen' in winner:
        carlsen_wins += 1
    elif 'Fabiano Caruana' in winner:
        caruana_wins += 1
    else:
        draw += 1
    
    print(f"Game {game + 1} Winner: {winner} (Utility value: {round(win_val, 2)})")


print()
print("Overall Results:")
print(f"Magnus Carlsen wins: {carlsen_wins}")
print(f"Fabiano Caruana wins: {caruana_wins}")
print(f"Draws: {draw}")
print()
if carlsen_wins > caruana_wins:
    print("Overall Winner: Magnus Carlsen")
elif caruana_wins > carlsen_wins:
    print('Overall Winner: Fabiano Caruana')
else:
    print('Overall Winner: Draw')
    

### Problem 2 ###

print('###### Problem 2 solve #######')

    
        
    