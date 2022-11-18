

def mayus(lista):
    i=0
    while i<len(lista):
        lista[i] = lista[i].upper()
        i=i+1



animales = ["perro", "gato", "ratón", "tortuga"]
personas = ["sergio", "luis", "marta", "josé", "maría"]


mayus(animales)
print (animales)

mayus(personas)
print (personas)
