from random import randint
import time

def sortTime():
    random_list = [randint(1, 1000) for i in range(100)]
    random_list2 = random_list
    start = time.perf_counter()
    bubble_sort(random_list)
    finish = time.perf_counter()
    print(finish-start)
    start = time.perf_counter()
    def_sort(random_list)
    finish = time.perf_counter()
    print(finish - start)
def bubble_sort(random_list):
    N = len(random_list)
    for i in range(N-1):
        for j in range(N-1-i):
            if random_list[j] > random_list[j+1]:
                random_list[j], random_list[j+1] = random_list[j+1], random_list[j]
    return random_list
def def_sort(random_list2):
    return sorted(random_list2)
sortTime()
