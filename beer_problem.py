import random

players = ['Alice', 'Benny', 'Carol', 'David', 'Ethel', 'Fred']
players_count = [0 for player in players]



def pass_beer():
    
    
    tasted = [False for player in players]
    tasted[0] = True
    curr_beer = 0
    last_tasted = 0
    
    while False in tasted:
        num = random.randint(1,2)
        if num == 1:
            if curr_beer == 0:
                curr_beer = len(players) - 1
            else:
                curr_beer = curr_beer - 1
        else:
            if curr_beer == len(players) - 1:
                curr_beer = 0
            else:
                curr_beer = curr_beer + 1
        
        tasted[curr_beer] = True
        last_tasted = curr_beer
    players_count[last_tasted] += 1

print(""" 
Pass The Beer : A problem of probability
     
     Suppose you (Alice) are sitting in a circle with your friends. You start drinking beer and 
     then start passing it to your left or right with probability 1/2. Then your neighbor does 
     the same-pass to his left or right with probability 1/2 and so on. The problem is which 
     person around the table is most likely to be the last one to  try the beer?

     The surprising answer is that ALL participants are equally likely!

     Let's try it here.
 """)

N = int(input('How many times you wish to conduct this experiment?'))

for i in range(N):
    pass_beer()

#print(players_count)

ratio_list = [0.00]
for i in range(1, len(players_count)):
    ratio = players_count[i]/N
    ratio_list.append(ratio)

print(f"""  
After conducting the experiment {N} times, we got the following results :

Player \t\t Chance of getting the beer last
 """)

for i in range (1, len(players)):
    print(f"{players[i]} \t\t {ratio_list[i]}")

