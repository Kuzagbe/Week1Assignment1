import random

def sort():

    list = []

    for i in range(10):
        list.append (random.randrange(1, 100, 1))
    print(list)
    # Sorting the list.
    list.sort()

    print("List Sorted: " +str(list))
sort()