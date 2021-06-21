

def solution(A):
    max_ds = max_ds_till_now = 0
    middle_min = 0
    absolute_min = A[1]
    negative_flag = False
    for i in range(1, len(A) - 1):
        # This if can happen only if A[i] is negative
        if A[i] < middle_min:
            # I am adding the last middle min
            double_slice = middle_min + max_ds_till_now
            middle_min = A[i]
            negative_flag = True
        else:
            double_slice = A[i] + max_ds_till_now

        if double_slice < 0:
            middle_min = 0
            max_ds_till_now = 0
        else:
            max_ds_till_now = double_slice

        max_ds = max(max_ds, max_ds_till_now)

        # Calculating the minimum value in case of all positive array
        if A[i] < absolute_min:
            absolute_min = A[i]

    if negative_flag:
        return max_ds
    else:
        return max_ds - absolute_min