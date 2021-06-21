def subArraySum( arr, n, s): 
        current_sum = 0
        start = 0
        i = 0
        while i < n:
            current_sum += arr[i]
            
            while current_sum > s and start < i:
                current_sum -= arr[start]
                start += 1
                
            if s == current_sum:
                return [start + 1, i + 1]
                
            i += 1
        return [-1]


print(subArraySum([1,2,3,7,5], 5, 12))
print(subArraySum([1], 1, 1))

print(subArraySum([135, 101, 170, 125, 79, 159, 163, 65, 106, 146, 82, 28, 162, 92, 196, 143, 28, 37, 192, 5, 103, 154, 93, 183, 22, 117, 119, 96, 48, 127, 172, 139, 70, 113, 68, 100, 36, 95, 104, 
12, 123, 134], 42, 468))

