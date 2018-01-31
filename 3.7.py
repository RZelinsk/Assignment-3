# This is Problem 7
import random

r = int(raw_input("select number of random numbers in sample: "))
x = int(raw_input("Select the min integer: "))
y = int(raw_input("Select the max integer. Must be larger than min + number of samples: "))

rand = random.sample(range(x,y), r)

print "'\n'These are the random numbers you generated: ", sorted(rand)

average = float(sum(rand) / len(rand))
center_average = float((sum(rand) - x - y) / (len(rand)-2))

print "'\n'The average is", average
print "The center average is", center_average
