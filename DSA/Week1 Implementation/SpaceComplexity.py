import random
# random is being imported because I want to generate random number for the algorithm
# or the function below

from memory_profiler import memory_usage
# memory_profiler is used for getting the memory or spaced taken or used by an algorithm

def function(f):
    lists = []
    # # An empty list is passed which will contain the random values produce below.
    for a in range(0,f):
        f = random.randint(0,100001, 10)
        # this appends the random values in the list but with range from 0 to 10001 which
        # which as a step of 10 so it going to be 1,11,21...etc.
        lists.append(f)
    return lists

UsedSpace = memory_usage()
print(UsedSpace,"MiB")