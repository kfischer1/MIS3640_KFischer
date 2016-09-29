#compute a factorial integer (n)

def factorial(n):
    if n == 1:
        return 1
    print('current n=', n)
    return n * factorial(n-1)

print(factorial(1))
print(factorial(3))

 
