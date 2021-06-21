def solution(A):
    min_avg = (A[0] + A[1]) / 2
    avg_start = 0
    i = 0

    while i < len(A) - 2:
        next_2_avg = (A[i] + A[i + 1]) / 2
        next_3_avg = (A[i] + A[i + 1] + A[i + 2]) / 3
        local_min_avg = min(next_2_avg, next_3_avg)

        if local_min_avg < min_avg:
            min_avg = local_min_avg
            avg_start = i
        i += 1

    last_2_avg = (A[i] + A[i + 1]) / 2
    if last_2_avg < min_avg:
        min_avg = last_2_avg
        avg_start = i

    return avg_start

print(solution([-3, -5, -8, -4, -10]))