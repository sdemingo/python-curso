

# 3. Listas, tuplas y diccionarios

Además de los tipos básicos, en Python tenemos tipos más complejos con los que
vamos a poder trabajar. Los tipos "avanzados" que vamos a ver en primer lugar
serían:

* Las listas
* Las tuplas
* Los diccionarios


## Las listas

En Python una lista es una colección de datos que se agrupan todos bajo un mismo
identificador o nombre de variable. Estos datos pueden ser del mismo tipo o de
tipos diferentes. Por ejemplo, vamos a guardar cinco números enteros asociados a
una sola variable, en lugar de utilizar una para cada uno de ellos:

```
    numeros = [4,2,23,112,-5]
```

Una lista puede estar compuesta, como ya hemos dicho, por datos de diferente
tipo. Incluso podría estar compuesta por un dato de tipo lista a su vez:

```
    numerosYmas = [4, -2, "hola", 953, True, "si"]

    listaDelistas= [4, -2, [ 9, 8, 2], "ultimo"]
    
    listaVacia = []
```

En el ejemplo anterior vemos que el tercer elemento de `listaDelistas` es una
lista. Para acceder a los elementos de una lista usaremos el operador `[`
`]`. Usaremos el nombre de la lista seguido de dicho operador y entre los
corchetes meteremos el índice de la lista que queremos consultar. **Es muy
importante tener en cuenta que los índices siempre empiezan en 0**. Por lo que
si queremos consultar el tercer elemento de una lista hemos de usar el índice
`2`. Por ejemplo, para imprimir por pantalla el cuarto elemento de `numerosYmas`
escribiremos `print(numerosYmas[5])`. En caso de que el índice sea negativo, el
acceso será contando desde el final de la lista. Esto es desde la
derecha. Usando un índice de `-1` nos llevará al último elemento de la lista.

El acceso a los miembros de una lista puede ser para su consulta o para su
modificación. Piensa en el siguiente código:

```
    print (numerosYmas[5])   // imprime "si"
    numerosYmas[5]="no"
    print (numerosYmas[5])   // imprime "no"
```

Para añadir miembros a una lista podemos usar el operador `+` pero hemos de
tener en cuenta que los datos de ambos lados del operador deben ser
listas. Vamos a añadir un valor de `2` a la lista `numerosYmas` y lo haremos
convirtiendo el `2` e una lista:

```
    numerosYmas = numerosYmas + [2]
```

También podemos hacer uso del método `append()` sobre la variable de tipo lista
ejecutando `numerosYmas.append(2)`. El resultado sería similar.

Para eliminar elementos de una lista usaremos la instrucción `del` seguido del
elemento que queremos borrar. Por ejemplo:

```
    numeros = [10, 20, 30, 40]
    del numeros[1]
    print (numeros)    //imprime [10, 30, 40]
```

De una lista podemos extraer otra usando el operador `[:]`. Es lo que se llama
rodaja o *slice* en Inglés. Este operador recibe dos enteros que indican los
índices de inicio y de fin de nuestra rodaja Rodajas de listas [:]. El primer
índice siempre forma parte de la rodaja mientras que el último nunca hará. La
rodaja termina en el anterior a este. Si no indicamos el inicio de la rodaja
está toma el inicio de la lista origen y lo mismo pasa con el final y el segundo
índice.

```
    lista = [10, 20, 30, 40, 50, 60]
    print (lista[1:])     // imprime [20, 30, 40, 50, 60]
    print (lista[:3])     // imprime [10, 20, 30]
    print (lista[1:4])    // imprime [20, 30, 40]
```

Conocer si un valor está o no en una lista puede ser muy útil. Esto nos lo
permite el operador `in`. Con este operador obtendremos un valor booleano que
nos indique si el valor está o no:

```
    lista = [10, 20, 30, 40, 50, 60]
    print (10 in lista)     // imprime True
    print (80 in lista)     // imprime False
```

Por último, para saber la longitud o número de miembros de una lista usaremos el
método `len()` que invocaremos directamente sobre la variable lista que queramos.




## Las tuplas

Una tupla en Python es un conjunto de datos que están agrupados. En esto se
parecen a la listas pero poseen una diferencia importante. Una tupla, una vez
creada no puede ser modificada. No podremos agregarle nuevos elementos ni
quitarle uno de los que ya tiene. Tampoco podremos modificar el valor de un
elemento interno.

Para definir una tupla indicaremos los elementos que contiene entre paréntesis:

```
    tupla = (8, "hola", -34)
```

Para acceder a los componentes usaremos el mismo mecanismo que con las
listas. Usando el índice entre corchetes:

```
    print (tupla[1])      // imprime "hola"
```


## Los diccionarios

Los diccionarios son también un tipo de datos que nos permitirá agrupar datos
sobre una sola variable. Se parecen mucho a las listas pero con una salvedad
importante. Podemos modificar el índice asociado a cada valor. Mientras que con
las listas, cada valor quedaba asociado a un índice de tipo entero, con los
diccionarios podemos hacer que este índice sea de otro tipo.

Estos índices se llaman **claves**. Es fundamental que una clave no se repita
dentro de un mismo diccionario. Veamos un ejemplo que almacena datos numéricos
asociados a claves de tipo string:

```
    temperaturas = {"Madrid": 18, "Bilbao": 19, "Sevilla": 22, "Barcelona": 24}
```

Con la anterior declaración hemos creado un diccionario llamado `temperaturas`
que guarda el valor numérico de una temperatura media en una ciudad. Como clave
del diccionario hemos usado el nombre de la ciudad en formato de string. 

Tanto para acceder al valor de una clave como para crear claves nuevas usaremos
los corchetes de forma parecida a como haciamos con las listas:

```
    print (temperaturas["Sevilla"])    // imprime 22
    
    temperaturas["León"] = 14
    print (temperaturas["León"])       // imprime 14
```

Para saber si existe un valor asociado a una clave en un diccionario usaremos el
operador `in` igual que con las listas:

```
    print ( "Madrid" in temperaturas) // imprime True
```

Si queremos crear un diccionario vacío usaremos las llaves sin valores en su
interior. Algo como `dicVacio = {}`.


## Ejercicios

1. Crea una lista que contenga varios nombres a tu elección. Pide al usuario un
   nombre por teclado y muestra por pantalla si es cierto o no que ese nombre
   está en la lista. [Solución](src/nombres.py)
