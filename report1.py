for n in range(2, 10):
    flag = 0
    for x in range(2, n):
        if n % x == 0 and flag == 0:
            print(n, 'equals', x, '*', n//x)
            flag = 1

    if(flag == 0):
        print(n, 'is a prime number')
# end

