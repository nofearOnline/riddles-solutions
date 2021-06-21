from timer import timer
from generator import Generator

@timer
def countTriplet(self, arr, n):
    i = j = triplets = 0
    hash_list = set(arr)
    for i in range(n):
        for j in range(i + 1, n):
            possible_sum = arr[i] + arr[j]
            if possible_sum in hash_list:
                triplets += 1
    return triplets


example_list = list(set(Generator.generate_list(1000, max_limit=1000)))
print(countTriplet("a", example_list, len(example_list)))
