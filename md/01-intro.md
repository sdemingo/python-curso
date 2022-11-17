


# 1. Introducción a Python


Python es un lenguaje de alto nivel de programación interpretado cuya filosofía
hace hincapié en la legibilidad de su código. Su curva de aprendizaje es muy
amigable y por eso se hace ideal para enseñar a programar a gente que nunca ha
tenido contacto con ningún otro lenguaje de programación. Surge a finales de los
años 80 en un centro de investigación de Países Bajos. Creado por Guido van
Rossum y, como muchos sospecharán, su nombre viene del archiconocido grupo de
cómicos británicos, Monty Python.


## Sobre el entorno

Este curso está preparado para ser impartido y seguido a través del servidor
Hipatia. En el servidor encontrarás los recursos necesarios para realizar el
curso. No necesitas instalar ningún software o recurso en tu máquina local al
margen de la aplicación para conectarte a Hipatia: PuTTy u otra similar.

Para seguir de forma apropiada este curso te recomendamos que tengas, en todo
momento accesible tanto este texto junto con un editor de texto con vuestros
códigos de pruebas y una consola del sistema donde poder ir probándolo
todo. Para conseguir este entorno puede resultarte muy útil usar la herramienta
`tmux` instalada en el sistema. Te recomendamos encarecidamente que si no
estás familiarizado con esta herramientas acudas al manual del servidor y
aprendas a usarla para poder tener abiertos estos tres recursos permanentemente
durante tu sesión en Hipatia. Puedes informarte sobre esta herramienta en:

    http://hipatia.iesjovellanos.org/tmux.html

Respecto al editor que puedes usar para escribir tu código, te recomendamos
`nano` si no tienes experiencia con otro editor. 

Para leer cómodamente estos apuntes en formato HTML puedes usar cualquier
navegador en entorno de terminal pero en Hipatia tienes instalado uno llamado
`w3m`. Dentro del directorio principal del curso encontrarás un fichero llamado
`index.html`. Ábrelo con este navegador y podrás empezar a navegar por el curso:

```
$ cd /var/publico/sdemingo/python-curso
$ w3m index.html
```

Si no estás familiarizado con `w3m` puedes ojear nuestra página de manual con la
información más básica sobre este navegador en:

    http://hipatia.iesjovellanos.org/w3m.html

Durante el curso se supondrá que el usuario conoce los aspectos básicos del uso
de Linux y de la consola de comandos del sistema. Si crees que no tienes todavía
habilidad suficiente para manejarte por el sistema a través del uso de la
terminal te recomendamos que pospongas este curso y dediques unos días a
manejarte por Hipatia usando los comandos básicos. En el manual online que
tenemos publicado en nuestra web podrás encontrar información útil para este
aprendizaje:

    http://hipatia.iesjovellanos.org/ayuda-index.html
    

Todo el código con las soluciones de los ejercicios planteados y de los ejemplos
propuestos se encuentra bajo el directorio `src` en este mismo directorio. 




## Licencia de uso y distribución

Todo el material de este curso se encuentra licencia bajo las condiciones de la
GNU General Public License Versión 3. El texto y la descripción de la licencia
puede encontrarse en este mismo directorio, dentro del fichero llamado
`LICENSE`.




## Primeros pasos

Python es un lenguaje interpretado. Esto quiere decir que el programa que tu
escribirás en un fichero de texto no será transformado por ningún programa
externo sino que será leído y procesado por un intérprete de Python. Para que el
sistema ejecute las instrucciones de tu programa no vale con indicarle que
quieres ejecutarlo. A quien realmente ejecutas es al intérprete de Python, y es
a el, a quien le dices que lea tu programa. Ahora veremos como hacer esto.

Vamos a crear nuestro primer programa en Python. Utiliza tu editor de textos
favorito para crear el fichero `hola.py`. Por ejemplo, ejecuta sobre un
directorio en el que tengas permisos (por ejemplo tu directorio personal) el
comando `nano hola.py` y escribe dentro la instrucción:

```
print ("hola mundo!")
```

Guarda los cambios y sal del editor de nuevo a tu consola. Para lanzar tu
programa deberás lanzar el intérprete y pasarle como argumento el nombre de tu
programa:

```
$ python3 hola.py
hola mundo!
```

El resultado se mostrará inmediatamente. Tu programa o *script* ha sido
ejecutado con éxito. Ya eres programador de Python ;)



