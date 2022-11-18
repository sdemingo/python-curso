

def construyePares(limite):
    pares=[]
    for i in range(1,limite+1):
        if (i % 2 == 0):
            pares.append(i)
            
    return pares




lista = construyePares(11)

print (lista)
