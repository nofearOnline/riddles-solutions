def possible_flags(peaks: [int], flags_num: int):
    len_peaks = len(peaks)
    peak_index = 1
    current_min_peak = peaks[0]

    for flag in range(1, flags_num):
        current_min_peak += flags_num
        
        while peak_index < len_peaks and current_min_peak > peaks[peak_index]:
            peak_index += 1
        if peak_index == len_peaks:
            return False
        else:
            current_min_peak = peaks[peak_index]
        
    return True


def solution(A):
    peaks = []
    len_A = len(A)
    if len_A < 3:
        return 0
    
    for i in range(1, len_A - 1):
        if A[i] > A[i -1] and A[i] > A[i+1]:
            peaks.append(i)

    len_peaks = len(peaks)
    if len_peaks == 0:
        return 0

    i = 2
    while i * i <= len_A + i - 2:
        if not possible_flags(peaks, i):
            break
        i += 1

    return i - 1
