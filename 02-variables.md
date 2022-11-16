

# 2. Variables

En este tema vamos a tratar el uso de las variables de un programa. Una variable
es un dato que se almacena en la memoria de nuestro equipo junto con una
etiqueta o identificador que usaremos para recuperarlo.

El dato que guardaremos en memoria y al que asignaremos un identificador puede
ser de múltiples tipos (enteros, caracteres, etc.) y, tal y como veremos. Según
el tipo que sea puede ocupar más o menos memoria.

Una vez que asignemos el dato a este identificador, al que llamaremos a partir
de ahora nombre, nos referiremos a este dato en nuestro código a través de este
siempre. Por ejemplo, vamos a guardar dos datos numéricos en sendas variables y
luego mostraremos el resultado de su suma:

```
variable1 = 8
variable2 = 9
print (variable1 + variable2)
```

Si guardamos este código en un fichero llamado `variables.py` y lo ejecutamos
obtendremos por pantalla el resultado de esa suma:

```
$ python3 variables.py
17
```

Como se ve, una vez que hemos asignado los valores numéricos a sus respectivos
nombres, hemos operado con dichos valores utilizando estos nombres.



## Tipos de datos

En Python podemos manejar datos de muchos tipos diferentes pero, por ahora,
vamos a centrarnos solo en los llamados tipos básicos o primitivos. Estos son:

* **Enteros**: Representan números enteros (sin parte decimal).
* **Reales**: Representan números con parte decimal. Requieren indicar ambas
  partes, la decimal y la entera separada por el caracter `.`.
* **Booleanos**: Representan los dos tipos de valores lógicos propios de la lógica
  booleana (`True` y `False`).
* **Cadenas de caracteres** (o strings): Como su nombre indica son cadenas de
  caracteres alfanuméricos. Sus valores literales deben encerrarse entre comillas.

Más adelante trabajaremos además con algún otro tipo de dato más. Tipos algo más
complejos como son las listas, las tuplas y los diccionarios. A continuación
vemos un ejemplo de creación de una variable de cada uno de los tipos descritos
arriba.

```
varEntera=784
varReal=345.23
varBooleana=False
varCadena="esto es una cadena"
```

Para operar con variables será necesario que estas sean del mismo tipo. Para
conseguir esto tendremos que realizar conversiones de tipo. Para convertir una
variable de un tipo en otro usaremos el nombre del tipo y entre paréntesis el
nombre de la variable que queremos convertir.

Por ejemplo, imagina que hemos declarado una variable de tipo string con la
cadena de caracteres `"834"` y la queremos sumar un valor numérico de `9`.

```
entero=9
cadena="834"
print (entero + cadena)
```

Si ejecutamos el código anterior el intérprete nos lanzará un error a la
pantalla que termina con el texto:

```
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

Nos está indicando que no podemos operar usando el operador aritmético de suma
con valores de diferente tipo. Hemos de convertir la variable `entero` a cadena
de caracteres o bien convertir la variable `cadena` a un número entero. Usaremos
la primera opción usando la expresión `str(entero)` para convertir el `9` en una
cadena de caracteres.

```
entero=9
cadena="834"
print (str(entero) + cadena)
```

Ejecutamos el código anterior y obtenemos:

```
9834
```

¿Como? Esa no es la suma que esperábamos. Realmente el código anterior es
perfectamente correcto. Al convertir la variable con valor `9` a cadena de
caracteres y usar la suma, estamos operando con dos cadenas de
caracteres. Python, suma las cadenas de caracteres concatenando una a la otra,
por lo que el resultado es el esperado.

```
    "9" + "834"   ->  "9834"
```

Si ahora probamos a la inversa y convertimos la variable `cadena` a un valor
numérico veremos que el resultado es la suma aritmética que esperábamos
inicialmente, esto es el valor numérico `843`.

```
entero=9
cadena="834"
print (entero + int(cadena))
```

## Operadores 

Los operadores nos permitirán operar con variables. Normalmente usaremos otras
variables para guardar el resultado de estas operaciones. 

Para realizar operaciones arítmeticas con numéros usaremos los operadores
clásicos: +, -, * y /. El operador '%' nos servirá para calcular resto de
una división. En relación a la división hemos de tener en cuenta también que la
operación de división o '/' siempre nos retornará un valor de tipo real nunca un
entero.

Para comparar valores primitivos podemos usar los operadores:

* `==`: Indica si los valores son iguales
* `!=`: Indica si son diferentes

Para comparar el valor de dos variables usaremos los operadores comunes
`>`,`>=`,`<`,`<=` que retornan un valor boolean y se leen respectivamente mayor,
mayor o igual, menor y menor o igual. Revisa el fichero `src/operadores.py`,
ejecutalo y analiza su resultado para entender los operadores en un caso práctico.



## El tipo string

Las cadenas de caracteres o strings forman parte de un  tipo especial en
Python. Son un *objeto*. Python posee tipos objetos predefinidos dentro de el y
permite también que definamos nuestros propios objetos. Algo que aprenderemos
más adelante.

En Python, para operar con un objeto podemos usar funciones asociadas con el y
que podremos invocar usando el nombre del objeto en si mismo seguido de la
función que queremos invocar sobre el. 

Para entender vamos a imaginarnos que tenemos una cadena definida en nuestro
código y queremos convertirla toda entera a mayúsculas. Para conseguir esto
usaremos la función `upper()`. La invocaremos sobre la variable de tipo string y
guardaremos el resultado en una segunda variable:

```
cadena1="Esto es una cadena"
cadena2 = cadena.upper()
print (cadena1)
print (cadena2)
```

Existen muchos métodos para trabajar con string que podemos invocar sobre
ellos. Os pongo a continuación una lista con los principales.

|---------------------|------------------------------------------------------------------|
| count()             | Returna el número de caracteres                                  |
| endswith(sufijo)    | Retorna True si el sring termina por ese sufijo                  |
| index(cadena)       | Retorna la posición de la primera aparición de la cadena buscada |
| lower()             | Convierte el string a minúsculas                                 |
| replace(cad1, cad2) | Remplaza las apariciones de la cadena cad1 por cad2              |
| startswith()        | Retorna True si la cadena comienza por ese prefijo               |
| strip(prefijo)      | Returns a trimmed version of the string                          |
| upper()             | Convierte a mayúsculas                                           |




## Pedir datos al usuario

Pedir un dato al usuario para que este nos lo introduzca por teclado es algo
básico para que nuestros programas cobren sentido de utilidad. Esto podemos
hacerlo fácilmente usando la instrucción `input`. Con esta instrucción podemos
adjuntar además un mensaje con el que indicar al usuario que queremos que nos
introduzca. 

Luego recogeremos el valor introducido en una variable tal y como se muestra en
el ejemplo siguiente:

```
numero = input("Introduce un número cualquiera: ")
```

Es importante indicar que la función `input` siempre retorna un string y si
queremos tratar esta variable de otra manera hemos de realizar una conversión
para evitar errores de tipos.

El siguiente programa pide un número al usuario y le suma otro que aporta el
propio programa:

```
numero = input("Introduce un número cualquiera: ")
otro = 8
print (int(numero) + otro)
```



## Ejercicios

1. Pide un número al usuario y calcula el triple mostrándolo por pantalla
   [Solución](src/triple.py)

2. Pide al usuario que te introduzca su nombre y envía un mensaje a la pantalla
   saludándole. Algo como "Hola Sergio, ¿qué tal estás?"
   [Solución](src/saludo.py)
   
3. Pide al usuario que te introduzca una frase y cambia todas las apariciones de
   las letras 'e' por 'E' y 'a' por 'A'.
   [Solución](src/cambio_letras.py)
