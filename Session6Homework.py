'''# Exercise 2.3
A= int(input('Enter A Value'))
B= int(input('Enter B Value'))
def gcd(A,B):
    if A == 0:
        print(B)
    elif B == 0:
        print(A)   
    else:
        if A > B:
            result= A % B
            A= B
            B= result
            return(gcd(A,B))
        elif B>A:
            result= B % A
            B= A
            A= result
            return(gcd(A,B))
        else:
            B == A
            return(A)
print(gcd(A,B))

'''
# Exercise 2.4
def tower(height, source, bridge, destination):
    if height >= 1:
        tower(height - 1, source, destination, bridge)
        print('%s --> %s' %(source, destination))
        tower(height - 1, bridge, source, destination)
tower(4,'A','B','C') 