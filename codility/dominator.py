
def solution(A):
    len_A = len(A)
    if len_A == 0:
        return -1
    sus_dominator = A[0]
    sus_dominator_power = 0
    sus_dominator_index = 0
    for i in range(len_A):
        if sus_dominator == A[i]:
            sus_dominator_power += 1
        else:
            if sus_dominator_power == 0:
                sus_dominator = A[i]
                sus_dominator_index = i
            else:
                sus_dominator_power -= 1

    if A.count(sus_dominator) > len_A / 2:
        return sus_dominator_index
    else:
        return -1