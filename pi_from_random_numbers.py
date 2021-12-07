import random

def est_pi(n):
    num_in_circle = 0
    num_total = 0
    for _ in range(n):
        x = random.uniform(0,1)
        y = random.uniform(0,1)
        distance = x**2 + y**2
        if distance <= 1 :
            num_in_circle += 1
        num_total += 1
    
    return 4 * num_in_circle / num_total
   
 
n = int(input("Enter points total: "))
pi = est_pi(n)
print(pi)
