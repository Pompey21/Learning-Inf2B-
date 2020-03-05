import numpy as np
# seed the pseudorandom number generator
from random import seed
from random import random

# EXERCISE 2: Case a
outcomes = []
def headstails(x):
	if x > 0.5:
		return 'T'
	elif x < 0.5:
		return 'F'
	else:
		headstails(rand(x))

for i in range(10):
	a = random()
	outcomes.append(headstails(a))
	print(outcomes)






