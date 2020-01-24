import timeit
import random
from matplotlib import pyplot as plt
# matplotlib is used to plot any graph

def sort(r):
    lists = []
    for a in range(0,r):
        lists.append(random.randint(1,100))
    MySortedLists = sorted(lists)
    return MySortedLists

TimeUsed = []
Time = []

for a in range(1, 101, 10):
    plottime = timeit.Timer("a,sort(a)", "from __main__ import sort, a")
    timeused = plottime.timeit(number=1)

    TimeUsed.append(timeused)
    Time.append(a)

# I am using this to get access to the matplot i imported to draw the graph
plt.plot(TimeUsed,Time, label = "Time taken")
plt.xlabel("Time")
plt.ylabel("Inputs")
plt.title("Time vs input")
plt.legend(loc = "lower right")
plt.show()