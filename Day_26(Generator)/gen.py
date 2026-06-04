""" Generator """

def isPrime(n):
    for i in range(2,n):
        if(n%i==0):
            return False


    return True


def nextPrime(n):
    while not isPrime(n:=n+1):
        pass
    return n

def primeGenerator(n):
    x = 2
    while n:
        if(isPrime(x)):
            n = n-1
            yield x
        x = nextPrime(x)

prime_list = [num for num in primeGenerator(10)]
print(prime_list)


#------ OUTPUT -------

[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

















'''
def Gen():
    yield 10
    yield 20
    yield 30
    
    
x = Gen()
for i in x:
    print(i)
    '''