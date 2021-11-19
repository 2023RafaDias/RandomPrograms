def factorial(n):
    if n == 1:
        return 1
    else:
        n = n*factorial(n-1)
        return n


#n = int(input())
#print(factorial(n))

def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        n = fibonacci(n-1)+fibonacci(n-2)
        return n

n = int(input())
print(fibonacci(n))
