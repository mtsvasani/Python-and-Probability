# monty hall problem

import random 

doors = ['goat', 'goat', 'car']
order = [0, 1, 2]

def play(N):
    
    switch_success = 0
    no_switch_success = 0

    for j in range (N):

        goat_door = -1
        new_choice = -1
        random.shuffle(doors)
        choice = random.randint(0,2)
        
        random.shuffle(order)
        for i in order:
            if i != choice and doors[i] == 'goat':
                goat_door = i
                #print(f'Door number {i} has a goat.')
                break
            
        for i in range(3):
            if (i != goat_door) and (i != choice):
                new_choice  = i

        if doors[new_choice] == 'car':
            switch_success += 1
        else:
            no_switch_success += 1
    
    return [switch_success, no_switch_success]

print(''' Here we are going to simulate  the infamous  Monty Hall problem. In this problem, there
are 3 doors, behind two of which are goats and behind the one remaining door is a car. You get to
keep whatever is behind the door chosen by you.First, you are allowed to choose a door. Then, the 
host opens one of the remaining two doors revealing a goat inside. Then you are given a chance to 
switch your choice.
    Would (should) you switch? Let's find out. ''')

N = int(input('''\nHow many times do you want to perform this experiment?
(For greater accuracy a large number like 1000 is suggested) : '''))

result = play(N)

print (f''' \nAfter carrying out the experiment {N} times, we found out that - 
If you switch, you get success on {result[0]} ocassions and
If you don't switch, you get success on {result[1]} ocassions. ''')

switch_win_probability = result[0]/N
other = 1 - switch_win_probability

print(f''' \nHence, the probability of success if you switch the doors = {switch_win_probability} and
the probability of success if you don't switch the doors = {other}''')

