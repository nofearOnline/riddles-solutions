def binary_search(arr, n):
    start = 0
    end = len(arr) - 1
    result = -1
    while start <= end:
        mid = (start + end) // 2
        mid_val = arr[mid]
        if mid_val == n:
            result = mid
            break
        elif mid_val > n:
            end = mid - 1
        else:
            start = mid + 1
    return result

print([binary_search([-6, 0], i) for i in range(-6,10)])