from timer import timer
from generator import Generator

@timer
def simpleMaxSubArraySum(self, a, size):
    final_sums = []
    for i in range(size):
        sums_from_i = [a[i]]
        for j in range(i + 1, size):
            sums_from_i.append(sums_from_i[len(sums_from_i) - 1] + a[j])
        final_sums.append(max(sums_from_i))
    return max(final_sums)

@timer
def maxSubArraySum(self, a, size):
    local_max_sum = a[0]
    global_max_sum = a[0]
    for i in range(1, size):
        local_max_sum = max(a[i] + local_max_sum, a[i])
        if local_max_sum > global_max_sum:
            global_max_sum = local_max_sum
    return global_max_sum


example_list = Generator.generate_list(10000, min_limit=-1000, max_limit=1000)
# print(example_list)
print(maxSubArraySum("a", [], len(example_list)))