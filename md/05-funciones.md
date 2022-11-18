

# 5. Funciones

Las funciones en programación se utilizan para agrupar bloques de código bajo un
nombre. Esta técnica permite a los programadores reutilizar estos bloques
siempre que quieran sin necesidad de volver a escribirlos, usando solo el nombre
del bloque para referirse a ellos.


```
    def saludo():
        nombre = input("Escribe tu nombre: ")
        print ("Hola "+nombre+", ¿cómo estás?")
```

Por ejemplo, en el recuadro anterior hemos creado una función llamada `saludo`
que pida al usuario su nombre y le salude. A esto se le suele llamar **declarar
una función**. Tras declararla usando la palabra `def`, la podremos usar en
cualquier parte de nuestro programa usando solo el nombre de la función seguido
de `()`.

```
    saludo()
```

A esto se le llama **invocar o llamar a una función**. Podremos crear tantas
funciones como queramos y estas pueden contener en su interior las instrucciones
que necesitemos. La creación de funciones que agrupen los pequeños problemas que
conforman el problema general que quieres solucionar, es la piedra angular de la
programación.


## Uso de parámetros

Cuando invocas a una función existe la posibilidad de pasarme diferentes
parámetros con información. Esto permite a la función realizar tareas con datos
que no están "en su interior" sino que vienen de fuera, del código
llamante. Puede sonar complejo pero en realidad no lo es. Veamos esto con un
ejemplo. Hemos creado una función llamada `mayus` que recibe una lista de
palabras. Como le haremos llegar esta lista a la función en el momento de su
invocación todavía no nos preocupa. El caso es que `mayus` recibe una lista y la
recorre convirtiendo las palabras de esta lista en mayúscula. Veamos el código
de su declaración:

```
    def mayus(lista):
        i=0
        while i<len(lista):
            lista[i] = lista[i].upper()
            i=i+1

```

el código de `mayus` es sencillo. Declara una variable numérica `i` como 0 y usa
una instrucción `while` para ejecutar su bloque de instrucciones tantas veces
como elementos haya en la lista. Por eso la expresión asociada a `while` es
`i<len(lista)`. En cada ejecución del bucle se accede la palabra de la lista que
ocupa esa posición: primero la palabra 0, luego la 1, luego 2, etc. Y se le
asigna un nuevo valor: el de esa misma palabra pero transformada en mayúsculas
gracias al método `upper()`. Por último incrementamos `i` en uno y ejecutamos el
bucle una vez más. No nos importa lo larga o corta que sea la lista, la
recorreremos siempre igual gracias a la instrucción `while`.

Pero ¿de donde sale la lista?. La lista no está declarada en el anterior
código. La lista nos llegará cuando se invoque a la función `mayus`. En ese
momento, en el de la invocación o llamada, será cuando se asigne valor al
parámetro lista.

Veamos un ejemplo de como llamaríamos a esta función. Crearemos dos listas
diferentes y para convertirlas a ambas a mayúsculas usaremos la función
declarada previamente:

```
    animales = ["perro", "gato", "ratón", "tortuga"]
    personas = ["sergio", "luis", "marta", "josé", "maría"]

    mayus(animales)
    print (animales)

    mayus(personas)
    print (personas)
```

En ambos casos se convierte la lista a mayúsculas usando la función
`mayus`. Esta función se ejecutará dos veces y en cada caso, la variable o
parámetro `lista` se convertirá en una lista diferente. En la primera
invocación, `lista` será realmente `animales`. Mientras que en la segunda,
`lista` será `personas`.

Puedes ver todo este ejemplo completo en el fichero
[mayusculas.py](../src/mayusculas.py).

Podemos declarar funciones con un número mayor de parámetros y en ese caso, en
la invocación hemos de respetar el orden de esos parámetros para que la
asignación sea correcta:

```
def ejemplo(indice, palabra, bool):
    print ("El indice vale "+str(indice))
    print ("La palabra vale "+palabra)
    print ("El booleano vale "+str(bool))


// Ejemplos de declaración:

ejemplo (9, "hola", False)
ejemplo (-4, "adios", True)
ejemplo (321, "buenas", True)
```

## Valores de retorno

Una función, además de realizar una serie de operaciones puede retornar un valor
a quien la invoca. Este valor puede ser útil para saber como ha ido el trabajo
de la función o para recuperar un dato que ella ha generado. Este valor
retornado puede ser de cualquier tipo: entero, string, tupla, lista, ....

Para que una función retorne un valor usaremos la instrucción `return` y hemos
de tener en cuenta que cuando esta instrucción se ejecute, la ejecución de la
función finaliza. Nunca pongas ninguna instrucción que pertenezca a la función
bajo un `return` pues nunca será ejecutada. 

Veamos un ejemplo. Vamos a crear una instrucción que recibe un número entero
como parámetro y construye y retorna una lista de los números pares hasta ese
número:

```
def construyePares(limite):
    pares=[]
    for i in range(1, limite+1):
        if (i % 2 == 0):
            pares.append(i)
            
    return pares
```


Para recuperar el valor retornado por la lista usaremos una variable junto con
su invocación de la siguiente manera:

```
listaPares = construyePares(10)
```

Ahora tendremos una lista llamada `listaPares` construida dentro de la función y
retornada por esta que tiene la forma `[2, 4, 6, 8, 10]`





## Ejercicios

1. Crea una función que reciba un parámetro numérico e informe si es un número
   primo o no. Úsala para imprimir por pantalla los números primos hasta
   el 100. [Solución](../src/primos.py)
