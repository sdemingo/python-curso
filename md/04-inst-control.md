
# 4. Instrucciones de control


En la primera parte del curso hemos dicho que los programas son conjuntos de
instrucciones que se ejecutan de forma secuencial y esto no es del todo
cierto. Un programador puede incluir ciertas instrucciones en su código que
permitan alterar este flujo secuencial. Este tipo de instrucciones se agrupan
normalmente en dos familias:

* Instrucciones selectivas: Son aquellas que crean varias ramas o bloques de
  instrucciones. En cada ejecución, según a valores internos del programa, se
  optará por ejecutar la rama de instrucciones correcta.

* Instrucciones iterativas: Son aquellas que permiten repetir varias veces un
  mismo bloque de instrucciones sin necesidad de tener que escribirlo más que
  una vez.


## Instrucciones selectivas

La principal instrucción selectiva de Python es `if`. Esta instrucción no
permite crear una bifurcación en el recorrido secuencial de nuestro código en
base al valor de una expresión *booleana* (es una expresión que se debe de
evaluar como cierta o falsa). 

Vamos a ver un ejemplo sencillo de uso de una instrucción de este tipo:

```
    num = input("Introduce un número: ")
    mul = int(num) * 3

    if (mul > 200):
        print ("Has introducido un número muy grande!!")
        
    print (mul)
```

Lo primero que vemos en el código anterior (este código está en el fichero
[multi_if.py](../src/multi_if.py) es que tenemos dos datos numéricos: uno que
pedimos por teclado al usuario llamado `num` y otro que generamos nosotros
llamado `mul` multiplicando el valor de `num` por tres.

Tras esto lo que queremos es evaluar el valor de mul y compararlo con 200. Sea
como sea impriremos por pantalla el valor de `mul` pero además, si este es mayor
que 200 imprimiremos un mensaje de advertencia.

Esto lo hemos conseguido con la instrucción `if`. Tras ella hemos escrito la
expresión booleana entre paréntesis. Esta expresión, usa un operador de
comparación (`>` en este caso) y se evaluará siempre como `True` o `False`.
Tras la expresión indicamos cual será el bloque de instrucciones primario del
`if`. Este será el bloque que se ejecute si la expresión se evalúa como cierta o
`True`.


>**Nota sobre la tabulación**:
>Es importante notar que el bloque de instrucciones que sigue al `if` no está
>alineado por la izquierda con este sino que está desplazado hacia la
>derecha. En Python **muy importante** usar esta identación o tabulación para
>separar los bloques de código. La última instrucción de `print` sabemos que
>está fuera del bloque del `if` porque no tiene esta tabulación previa y está
>alineada con el resto de instrucciones previas del `if`.



A la instrucción `if` podemos añadirle una rama de código opcional a través de
la instrucción `else`. El código que se inicia tras el `else` será ejecutado si
la expresión booleana que acompaña al `if` se evalúa como `False`. Veamos un
ejemplo:


```
    num = input("Introduce un número: ")
    mul = int(num) * 3

    if (mul > 200):
        print ("Has introducido un número muy grande!!")
    else:
        print (mul)
```

Con esta variación ahora, si el valor de `mul` sobrepasa los 200 solo se
mostrará el mensaje de advertencia y no el valor de la multiplicación.




## Instrucciones iterativas

La otra familia de instrucciones de control de flujo son las iterativas. También
llamadas comúnmente *bucles*. Estas instrucciones nos permite crear bloques de
código que se ejecutarán varias veces.

La primera de estas instrucciones es `while`. Esta instrucción permite ejecutar
el bloque de código asociado en base a verdad o falsedad de una expresión
booleana. Veamos un ejemplo:

```
    num = input("Introduce un número: ")
    mul = int(num)

    while (mul < 200):
        mul = mul * int(num)
        print (mul)
    
    print ("Ya hemos acabado")
```

El código anterior toma un  número por teclado y lo va multiplicando por si
mismo. Vemos que la expresión booleana es `(mul < 200)`. Esto significa que
cuando el resultado sobrepase ese número se saldrá de ese bucle y se continuará
con el resto de instrucciones bajo el.


Otra instrucción iterativa muy usada en Python es `for`. El bucle `for` no se
basa en una expresion booleana sino en *pivotar* el valor de una variable entre
los diferentes valores de una lista a la que acompaña. Por ejemplo, partimos de
una lista llamada `animales`. Vamos a imprimir por pantalla un mensaje por cada
animal de la lista:

```
    animales = ["perros", "gatos", "pajaros", "zorros", "burros"]

    for animal in animales:
        print ("Me gustan los "+animal)
```

Tras ejecutar el código anterior veremos una salida similar a la que se muestra
a continuación. La variable `animal` ha ido pivotando su valor entre los valores
de la lista siguiendo su orden y valiendo ese valor en cada iteración o vuelta
del bucle. El bucle termina cuando ya no hay mas miembros de la lista sobre los
que pivotar.

```
    Me gustan los perros
    Me gustan los gatos
    Me gustan los pajaros
    Me gustan los zorros
    Me gustan los burros
```

¿Qué tipos de dato pueden ser recorridos con un bucle for? Bien, de los que
hemos visto, las colecciones (listas, tuplas y diccionarios) y las cadenas
(entendidas como una colección de caracteres). Puede sernos útil conocer la
instrucción `range` que genera una lista con números sobre de un rango. Esta
instrucción resulta una gran compañera de `for` cuando queremos iterar a través
de una lista numérica:

```
    for i in range(10,30):
        print (i)
```


## Ejercicios

1. Pide al usuario dos números e imprime cual de ellos es el
   mayor. [Solución](../src/mayor.py)
   
2. Genera una lista de nombres que sigan el siguiente patrón:
   "doc1","doc2","doc3", ... hasta "doc20". [Solucion](..src/listaRango.py)
