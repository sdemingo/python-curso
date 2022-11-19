

# 6. Entrada/Salida

Las funciones y operaciones que se agrupan dentro de este capítulo son las que
nos permitirán meter datos a nuestros programas y sacar datos de estos. Ya
conocemos dos de estas funciones: `input` y `print`.

Vamos ahora a conocer formas para leer y escribir información en ficheros del
sistema. Algo que puede sernos muy útil para conseguir que nuestros programas
tengan información perdurable sobre el sistema de ficheros.

Antes de trabajar con ficheros hemos de conocer dos instrucciones que debemos
utilizar, antes de empezar a usarlos y tras terminar de utilizar estos:

* `open()`: Indica al sistema operativo que quieres utilizar un fichero y de que
  manera vas a utilizarlo: si vas a leerlo, a escribirlo, etc.
  
* `close()`: Indica al sistema que quieres dejar de utilizar un fichero.

La función `open` nos devuelve una variable de tipo `File` que nos ayudará a
manejar el fichero. Esta variable u objeto guarda en su interior la última
posición leída u escrita. Para invocar correctamente `open` necesitamos, al
menos, dos argumentos: uno es la ruta del fichero sobre el sistema (relativa a
donde estamos situados o absoluta desde la raíz del sistema) y dos es el modo en
el que vamos a trabajar. Hemos de seleccionar uno de los siguientes modos:

* `r`: Abrir el fichero para leerlo.
* `w`: Abrir el fichero para escribirlo. Si este existe, su contenido anterior
  será eliminado y sino existe, se creará.
* `a`: Abrir el fichero para escribirlo pero añadiendo el contenido a lo que ya
  teníamos en su interior
* `+`: Abrir el fichero para leerlo y para escribirlo simultáneamente.


## Leer de ficheros

Para leer un fichero con Python debemos primero indicar al sistema nuestra
intención para luego proceder a leerlo. Una vez lo hayamos abierto, sobre el
fichero podemos realizar diferentes operaciones de lectura. A continuación listo
las más comunes:

* `read(n)`: Lee del fichero `n` bytes y retorna esos bytes como un string. Si
  omites este valor provocas que retorne todo el contenido del fichero en un
  solo string.
  
* `readline()`: Lee una sola línea del fichero.

* `readlines()`: Lee toda las líneas del fichero y las retorna como una lista de
  string, donde cada miembro de esta lista es una de estas líneas.
  


Veamos dos ejemplos. En este primero leeremos todo el fichero de golpe
guardándolo en un solo string:

```
    fichero = open("nombre.txt","r")
    texto = fichero.read()
    fichero.close()
```


Ahora leeremos todo el fichero pero separado en líneas y nos quedaremos solo con
las dos últimas:

```
    fichero = open("nombre.txt", "r")
    lineas = fichero.readlines()[-2:]
    fichero.close()
```




## Escribir en ficheros

Para escribir un fichero, las operaciones previas son similares a la
lectura. Necesitamos ejecutar `open` con el modo adecuado. Una vez hecho esto
podemos elegir dos funciones para escribir en el:

* `write(text)`: Escribe el string sobre el fichero.
* `writelines(list)`: Escribe en el fichero una lista de strings.

Si queremos escribir manualmente un salto del línea para separar dos líneas
hemos de escribir el caracter `\n`. Veamos un ejemplo:

```
    fichero = open("salida.txt","w")
    fichero.write("Esta será la primera línea del fichero")
    fichero.write("\n")
    fichero.write("Esta será la segunda línea")
    fichero.close()
```







