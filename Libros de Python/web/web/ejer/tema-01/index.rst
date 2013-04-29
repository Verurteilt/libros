
==========
Ejercicios
==========

---------------------------------
 *Tema 1:* Programación Funcional
---------------------------------

Funciones como valores
======================

#. Implementa una función ``flip (fn)`` recibe una función binaria
   ``fn`` que devuelve otra función igual que ``fn`` pero con los
   parámetros intercambiados.

   .. hint:: Define una función dentro de la función ``flip`` que
      invoca a ``fn`` con los parámetros en orden inverso.

   `Solución <flip.py.txt>`__

#. Implementa una función ``trace (fn)`` que recibe una función ``fn``
   y devuelve otra que hace lo mismo que ``fn`` pero antes de
   ejecutarla escribe por pantalla: ``Ejecutando "fn
   (...)"``. Idealmente, en los `...` aparecen los parámetros con los
   que ha sido ejecutada.

   .. hint:: Recuerda que puedes acceder al nombre de una función con
      ``fn.__name__``.

   .. hint:: Define una función dentro de la función ``trace`` que
      es la que imprime el nombre de la función y la ejecuta.

   .. hint:: Esa función recibe un número variable de parámetros y se
      los pasa idénticos a ``fn``.

   `Solución <trace.py.txt>`__

#. Implementa una función ``compose (f1, f2, ..., fn)`` que devuelve una
   nueva función equivalente a la composición *f1 · f2 · ... · fn*
   matemática, sean *fi* funciones unarias. Es decir, sea::

     f = compose (f1, f2, ..., fn)

   Se cumple para todo *x* que::

     f (x) == f1 (f2 (... fn (x)))
   
   .. hint:: Recoge las funciones como una lista.

   .. hint:: Itera sobre las funciones de atrás hacia adelante
      aplicándolas sucesivamente ``reversed`` o ``lista[::-1]``.

   `Solución <compose1.py.txt>`__

Funciones de alto orden
=======================

#. Implementa la famosa función que aplicada sobre dos listas devuelve
   otra lista con los productos de cada par de números. Es decir, como
   la de la relación anterior, pero sin usar bucles.

   .. hint:: Usa la función ``map``

   .. hint:: Mezcla las dos listas con la función ``zip``

   .. hint:: Usa ``operator.mul`` para mayor eficiencia.

   `Solución <product.py.txt>`__

#. Escribe una función que compruebe si una lista contiene algún
   número impar, sin utilizar bucles.
 
   `Solución <tieneimpar.py.txt>`__

#. Escribe una función `intersec (l1, l2)` que dadas dos listas
   devuelve otra con los elementos que están en las dos, sin utilizar
   ``set`` ni bucles ``for``.

   .. hint:: Usa la función ``filter``

   `Solución <intersec.py.txt>`__

#. Implementa la función ``compose`` anterior sin utilizar bucles
   `for`.

   .. hint:: Utiliza la función ``reduce``.

   .. hint:: Pasa como valor inicial a la función ``reduce`` el
      valor ``x``, la función de reducción recibe por la izquierda el
      valor que se está reduciendo y por la derecha la siguiente
      función de la lista.

   `Solución <compose2.py.txt>`__

#. Escribe una calculadora por consola en notación polaca (notación
   prefijo) que efectúe las operaciones suma, resta, multiplicación,
   división, exponenciación.

   Ejemplo de sesión con el programa::

     Operación: + 3 2
     Resultado: 5
     Operación: / 4 2
     Resultado: 2
     ...
   
   La entrada basta que la hagas con ``raw_input``, pero si te sobra
   tiempo echale un vistazo al módulo `readline
   <http://docs.python.org/library/readline.html>`__

   .. hint:: Usa un diccionario que asocie cada operación con la
      función que la ejecuta.

   .. hint:: Haz un bucle que llama a ``raw_input``. Extrae de la
      cadena la operación y los parámetros.

   `Solución <calcu.py.txt>`__

#. Añade al programa anterior una función ``exit`` sin parámetros y otra
   función ``sqrt`` que hace la raiz cuadrada de un número.

   .. hint:: Para comprobar que el número de parámetros es correcto,
      guarda en el diccionario tuplas *(funcion, numero de
      argumentos)* en vez de sólo la función. Otra opción más general
      es usarndo::

         nargs = len (inspect.getargspp (fn).args)

      Otra opción más general, aunque hay que tener cuidado, es
      capturar el `TypeError` que lanza invocar una operación con
      número incorrecto de parámetros.

   `Solución <calcu.py.txt>`__

#. Escribe una función que lea un fichero de esta forma::

      equipo-1 0 0 0 3 0 0
      equipo-2 0 1 0 0 0 1 3

   Es decir, cada linea empieza por el identificador de un equipo de
   futbol, sin espacios, y le sigue una lista de números con los
   puntos que obtenido en los sucesivos partidos de la liga.

   Queremos calcular el resultado de la liga. El programa debe
   producir una salida de la forma::

      equipo-2 5
      equipo-1 3
      
   En el que cada linea empieza por el identificador de un equipo y tras
   cuantos espacios quiera le sigue el total de puntos que ha obtenido.
   correspondiente. El fichero de salida tiene que estar ordenado de
   mayor a menor. Aquí tienes un `fichero de prueba <result-liga.txt>`__.

   .. hint:: Lee el fichero con ``file.readlines ()`` y separa los
      campos de cada linea con la función ``str.split ()``
  
   .. hint:: Recuerda que puedes ordenar con la función
      ``list.sort()``. Pasale una ``lambda`` al parámetro ``key``.

   `Solución <liga.py.txt>`__

#. Escribe tres funciones con el comportamiento de la función
   ``reduce``, ``map`` y ``filter`` respectivamente sin usar bucles
   ``for`` ni listas por comprensión. 

   Esta es la implementación típica en un lenguaje funcional, pero es
   ineficiente a no ser que usemos las herramientas que veremos en el
   tema 3, ¿por qué?

   .. hint:: Usa recursividad.

   .. hint:: En cada iteración procesa ``lista[0]`` y pasa
             ``lista[1:]`` a la siguiente iteración hasta que esté
             vacía.
	     
   `Solución <funcional.py.txt>`__
