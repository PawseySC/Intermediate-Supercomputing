from random import random

num_trials = 2*10**6
r = 1.0
r2 = r * r
Ncirc = 0

for _ in range(num_trials):
    x = random() 
    y = random()
    if x**2 + y**2 < r2:
        Ncirc += 1 

pi = 4.0 * (float(Ncirc) / float(num_trials)) 

print(f"Computing pi in serial:\n\tFor {num_trials} trials, pi = {pi}\n")
