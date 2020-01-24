import timeit
# I import timeit because its not going to print just two decimal places
# and also I want to print the amount of time takes the algorithm to execute.

import random
# random is being imported because I want to generate random number for the algorithm
# or the function below

def sort(r):
    lists = []
    # An empty list is passed which will contain the random values produce below.
    for a in range(0,r):
        lists.append(random.randint(1,10001,10))
    #     this appends the random values in the list but with range from 0 to 10001 which
    #      which as a step of 10 so it going to be 1,11,21...etc.
    MySortedLists = sorted(lists)
    return MySortedLists

for a in range(1):
    time1 = timeit.Timer("a,sort(a)", "from __main__ import sort, a")
    timeused = time1.timeit(number=100000)
    # this code Estimate how long each algorithm would take with repect to the size of each input.
    print("Time is", timeused, "seconds")