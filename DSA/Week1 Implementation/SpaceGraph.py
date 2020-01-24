import random
from memory_profiler import memory_usage
from matplotlib import pyplot as plt

SpaceUsed = memory_usage()
def function(r):
    lists = []
    for a in range(0, r):
        r = random.randint(0,100)
        lists.append(r)
    return lists

Memory = []
ReceivedIn = []

for a in range(1,100,10):
    SpaceUsed = memory_usage()
    Memory.append(SpaceUsed)
    ReceivedIn.append(a)

# I am using this to get access to the matplot i imported to draw the graph
plt.plot(ReceivedIn,Memory, label = "space taken")
plt.xlabel("Inputs")
plt.ylabel("Spaced Used")
plt.title("Used Space vs Inputs Difference")
plt.legend(loc = "upper right")
plt.show()