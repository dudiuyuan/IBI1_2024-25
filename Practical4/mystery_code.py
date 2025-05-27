# What does this piece of code do?
# Answer: This code simulates a loop that repeatedly generates two random integers between 1 and 6 (inclusive). 
# For each iteration, if the two numbers are different, the variable progress is incremented by 1. 
# The loop continues until the two randomly generated numbers are equal with a 1/6 probability.

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

progress=0
while progress>=0:
	progress+=1                      # If the conditions for the cycle are met (progress>=0), the progress variable is incremented by 1.
	first_n = randint(1,6)
	second_n = randint(1,6)
	if first_n == second_n:          # if the two numbers are the same, the loop breaks, which means that the probability of end is 1/6. Otherwise, restrat the cycle from line 17.
		print(progress)
		break

