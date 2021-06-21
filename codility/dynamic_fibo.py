def fibo(n):
    last_two = [0, 1]
    if n < 2:
        return n
    num = sum(last_two)
    for i in range(2, n):
        last_two[0], last_two[1] = last_two[1], last_two[0] + last_two[1]
        num = sum(last_two)
       
    return num

print([fibo(i) for i in range(32)])