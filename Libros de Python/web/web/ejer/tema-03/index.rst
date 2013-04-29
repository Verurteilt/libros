
==========
Ejercicios
==========

--------------------------------
 *Tema 3:* Cuestiones Avanzadas
--------------------------------

Iteradores y Generadores
========================

#. Implementa nuestra amada función que calcula la lista con los
   productos de los elementos de dos listas sin utilizar el operador
   corchete, ni bucles ``for`` ni comprensión de listas, ni ``zip``.

   .. hint:: Obtén un iterador de por cada lista con la función
      ``iter``. Avanza los iteradores con ``next ()``.

   .. hint:: Comprueba que ha terminado el bucle capturando la
      excepción ``StopIteration``.

   `Solución <productoiter.py.txt>`__

#. Implementa un generador ``sucesos (probabilidad)`` que produce una
   secuencia infinita de valores booleanos pseudoaletoreos con
   ``probabilidad`` de que sean ``True``.

   .. hint:: Utiliza la función ``random.random ()`` para generar un
      número pseudo-aleatoreo entre 0.0 y 1.0 una distribución uniforme.

   `Solución <sucesos.py.txt>`__

#. Implementa el ejercicio 2 del apartado *Funciones de Alto Orden*
   del tema 1 utilizando las funciones de ``itertools``. Esa función,
   recordemos, devolvía ``True`` si algún elemento contiene algún
   número par y ``False`` en caso contrario.

   `Solución <tienepar.py.txt>`__

#. Implementa un generador ``fibonacci`` que produce los diferentes de
   la secuencia de Fibonacci, que tiene la forma::

      0, 1, 1, 2, 3, 5, 8, 13, ...

   Cuyos dos primeros valores son 0 y 1 por definición y el resto se
   calculan sumando los dos últimos valores de la sucesión.

   `Solución <fib.py.txt>`__

#. Compara la eficiencia de la función del ejercicio 3 con la
   desarrollada en el tema 1. Para ello, será útil definir una función
   ``algunospares (n, p)`` que devuelve una lista de *n* números dónde
   cada número tiene una probabilidad *p* de ser par, basándote en la
   función ``sucesos``.

   .. hint:: Te será de útil usar la función ``itertools.imap`` para
      convertir los sucesos en enteros.

   .. hint:: Te será útil la función ``itertools.islice``.

   `Solución <algunospares.py.txt>`__

#. Implementa un generador ``primos`` que genere todos los números
   primos. Por eficiencia, el generador debe ir almacenando los primos
   encontrados hasta el momento en una lista.

   `Solución <primos.py.txt>`__

Decoradores
===========

#. Implementa un decorador ``unarygen``, que convierte cualquier
   función unaria *f* en un generador que recibe como parámetro un
   valor inicial ``inic`` y modele la secuencia::

      inic, f(inic), f(f(inic)), f(f(f(inic))), ...

   Por ejemplo, el siguiente código::

      @unarygen
      def dedosendos (n):
          return n + 2

      for x in dedosendos (0):
          print x

   Produce la salida:

      0
      2
      4
      ...

   .. hint:: Define un generador dentro de ``unarygen``` que llama a
      la función de fuera en un bucle infinito, haciendo ``yield`` de los
      sucesivos valores que va produciendo.

   `Solución <unarygen.py.txt>`__

#. Define una operación ``potencia (op, val, n)`` que calcula la
   *n*-ésima potencia de un valor *val* sobre la operación *op*.

   .. hint:: Se recomienda usar el decorador anterior.

   .. hint:: Se recomienda usar función ``itertools.islice`` para
      avanzar un generador a la posición que quieres.

   `Solución <potencia.py.txt>`__

#. Define un decorador ``memoize`` que añade ``memoización`` a
   cualquier función. Esto significa, que para unos parámetros dados
   la función real sólo se ejecuta una vez, y el resto de veces
   consulta el resultado desde una tabla. 

   Como no puedes meter un diccionario como clave en un diccionario,
   sólo se podrán decorar así funciones que no tengan parámetros por
   clave.

   .. hint:: Crea un diccionario dentro del decorador, pero fuera de
      la función que implementa el envoltorio. Cada vez que se ejecute
      el envoltorio, comprueba si la tabla contiene alguna clave con
      los parámetros que ha recibido.

   `Solución <memoize.py.txt>`__

#. Define un decorador ``memoizegen`` que decora un generador de tal
   forma que los valores del generador decorado se computan realmente
   sólo la primera vez que se itere sobre alguna instancia del
   generador, el resto de veces se sacan de una lista.

   `Solución <memoizegen.py.txt>`__

Gestión de Recursos
===================

#. Escribe un gestor de contexto ``onexit (func)`` que ejecuta se
   asegura de que se ejecuta la función ``func`` al salir del bloque.

   `Solución <onexit.py.txt>`__

#. Escribe un gestor de contexto ``fastmap`` que al entrar en el
   bloque substituye la función ``map`` por la versión de
   ``itertools`` y al salir lo deja como estaba.

   .. hint:: Para asignar a la variable global ``map`` tienes que
      indicar ``global map`` antes de hacer la asignación.

   .. hint:: Si lo haces como en la pista anterior la substitución
      sólo afectará a las funciones del módulo actual, para que afecte
      globalmente, puedes asignar la función ``imap`` en
      ``__builtins__.map``.

   `Solución <fastmap.py.txt>`__
