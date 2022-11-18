
def esPrimo(n):
    for i in range (2,n-1):
        if ( n % i == 0):
            return False

    return True



for numero in range (1,100):
    if esPrimo(numero):
        print (numero)
