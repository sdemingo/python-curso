
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

**Nota sobre la tabulación**:

Es importante notar que el  bloque de instrucciones que sigue al `if` no está
alineado por la izquierda con este sino que está desplazado hacia la derecha. En
Python **muy importante** usar esta identación o tabulación para separar los
bloques de código. La última instrucción de `print` sabemos que está fuera del
bloque del `if` porque no tiene esta tabulación previa y está alineada con el
resto de instrucciones previas del `if`.



## Instrucciones iterativas
