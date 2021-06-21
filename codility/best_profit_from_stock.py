def solution(A):
    max_profit = max_till_now = 0
    for i in range(1, len(A)):
        profit = A[i] - A[i - 1] + max_till_now
        max_till_now = max(0, profit)
        max_profit = max(max_profit, max_till_now)

    return max_profit