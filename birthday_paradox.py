import random 

days = []

months1 = ['Jan', 'Mar', 'May', 'Jul', 'Aug', 'Oct', 'Dec']
months2 = ['Apr', 'Jun', 'Sep', 'Nov']

for i in range(1, 32):
    for month in months1:
        days.append(f"{month} {i}")
    if i < 31:
        for month in months2:
            days.append(f"{month} {i}")
    if i < 30:
        days.append(f"Feb {i}")

# for day in days:
#     print(day)

def take_random(N):
    counter = 0
    print("Generating Random Birthdays...")
    
    for i in range(10000):
        
        test_days = []
        for j in range (N):
            ind = random.randint(0, 365)
            test_days.append(days[ind])
        
        test_set = set(test_days)
        
        if len(test_days) != len(test_set):
            counter += 1
            
        if i == 0:
            print("First set of birthdays --", end="")
            print(test_days)
            print("0% Completed..")
        elif i == 2000:
            print("20% Completed..")
        elif i == 4000:
            print("40% Completed..")
        elif i == 6000:
            print("60% Completed..")
        elif i == 8000:
            print("80% Completed..")
        elif i == 9999:
            print("100% Completed..\n")
            

    return counter


print ( """  Welcome to the Birthday Paradox. It is hard to believe but theoritically
proved that if 80 persons are chosen in random, then we have a 99.99 percent chance that 
at least two of them share their birthday. Let's test it.

    Enter a number, the number of people chosen ==> """, end="" )


people = int(input())

success = take_random(people)

print(f"Out of 10000 cases, we found out that {success} times at least two persons share their birthday.")
percent = success/100
print(f"That is {percent} percent success rate!")
