call_count = 0

def fib3(n):
    """Return a n-th member of Fibonacci series. a recursive version"""
    global call_count #this statement makes outer variable visible
    call_count+=1

    if n < 2:
        return n
    else:
        return fib3(n-1)+fib3(n-2)
#def ends

f1 = fib3(10) #call
print(call_count)

sum_count = 0
def fib2(n):  # return Fibonacci series up to n
    """Return a list containing the Fibonacci series up to n."""
    global sum_count #this statement makes outer variable visible
    result = []
    a = 0
    b = 1
    while a < n:
        sum_count+=1
        result.append(a) #
        a,b = b, a+b
    return result

#Function call returns a value
f2 = fib2(10)
print(sum_count)