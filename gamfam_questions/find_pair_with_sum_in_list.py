

def find_pair_with_sum(arr, sum_num):
    needed_memory = set()
    for element in arr:
        if element in needed_memory:
            return True
        else:
            needed_memory.add(sum_num - element)
    return False


ans = find_pair_with_sum([1,-2,-3,-4,5,6], 5)

print(ans)