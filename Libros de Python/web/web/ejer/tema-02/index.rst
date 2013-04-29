==========
Ejercicios
==========

---------------------------------
 *Tema 2:* Orientación a Objetos
---------------------------------

Clases y herencia
=================

#. Tenemos una base de datos de personas de la universidad. En la base
   de datos hay ``personas``, ``profesores`` y ``alumnos``. De las
   personas sabes su ``nombre_y_apellidos``. De profesores además
   su ``departamento``, y de los alumnos su ``curso``.

   Escribe un programa que lee un fichero de esta forma::

     numero-de-personas
     tipo-de-persona
     dato-persona-1
     dato-persona-2
     ...

   Ejemplo::

     3
     persona
     Pepito Grillo
     alumno
     Ramon Ramirez
     4
     profesor
     Don Importante
     Semiótica Aplicada

   Escribe un programa que recibe como argumentos de la linea de
   comandos el nombre del fichero y un tipo de persona y lista por
   pantalla las personas de ese tipo de la base de datos. Puedes usar
   el siguiente `fichero de ejemplo <ejemplo-personas.txt>`__.

   .. hint:: Recuerda que los parámetros de consola están en una lista
      en ``sys.argv``

   .. hint:: Crea tres clases ``Persona``, ``Alumno`` y ``Profesor``,
      cada una con una funcion ``lee_datos`` que lee sus datos. Leemos
      el fichero creando una gran lista.

   .. hint:: Una buena forma de organizar el código es que las clases
      ``Alumno`` y ``Profesor`` hereden de ``Persona``. Su función
      ``lee_datos`` delegará parte del trabajo a través de ``super``

   .. hint:: Para decidir qué tipo de objeto tienes que crear, puedes
      hacer un diccionario que asocie a cada tipo de persona como
      cadena de texto la clase que lo implementa.

      Si eres valiente, puedes ahorrarte ese diccionario usando
      `globals ()`, que devuelve un diccionario con todas las
      variables globales del programa, incluidas clases.

   .. hint:: Puedes filtrar el fichero con ``isinstance`` o mirando el
      ``__class__`` según la semántica que le quieras dar.

   `Solución <personas.py.txt>`__

#. El fichero `error_jerar.py <error_jerar.py.txt>`__ contiene una
   jerarquía que da el siguiente error al importarlo o ejecutarlo::

     Traceback (most recent call last):
       File "error_jerar.py", line 14, in <module>
         class D (AB, BA):
     TypeError: Error when calling the metaclass bases
         Cannot create a consistent method resolution
     order (MRO) for bases A, B

   ¿Se te ocurre por qué?

   .. hint:: Intenta calcular en que orden irían los ``super``, es
      decir, el *MRO (Method Resolution Order)* con las reglas que
      hemos dado en el curso.

Encapsulación, Slots y Funciones especiales
===========================================

#. Implementa un esquema de clase ``Racional`` que tenga dos
   atributos, ``numerador`` y ``denominador`` e implemente algunas
   operaciones matemáticas, como los operadores ``+``, ``-``, ``*`` y,
   ``/``. Recuerda que en la vida real, usaríamos la clase `Fractional
   <http://docs.python.org/library/fractions.html>`__.

   .. hint:: Recuerda que esos operadores son ``__add__``,
      ``__mul__``, etc...
  
   .. hint:: Recuerda que devuelven un nuevo objeto, no modidifican el
      ``self``.

   `Solución <racional.py.txt>`__

#. Añade una propiedad de sólo lectura ``entero`` que devuelva el valor
   entero de la clase racional y tire una excepción de tipo
   ``ValueError`` si el ``Racional`` en cuestión no es un número
   entero.

   .. hint:: Define el comportamiento de la propiedad como un método y
      usa ``property (nombre_metodo)`` para convertirlo en un
      atributo.

   .. hint:: La sintaxis básica para tirar excepciones es ``raise
      TipoDeExcepción``

   .. hint:: La función ``divmod`` puede hacer tu código ligeramente
      más eficiente.

   `Solución <racional2.py.txt>`__

#. Cambia la clase ``Racional`` para que use ``slots`` para que sea
   y así sea más ligera.

   `Solución <racional3.py.txt>`__

#. Comprueba con ``%timeit`` si ademas tiene alguna ventaja de
   eficiencia temporal el uso de ``__slots__``

#. Implementa una clase ``partial`` que se pueda usar igual que la
   función ``partial`` del módulo ``functools`` de la biblioteca
   estándar de Python.

   .. hint:: En esta clase no hace falta tener en cuenta lo que
      dijimos sobre el constructor ``__init__``, ya que no esperamos
      que nadie herede de ella.

   .. hint:: Tendrás que definir el la función especial ``__call__``.
   
   .. hint:: El constructor de la clase debe recibir como parámetros
      la función y los parámetros a fijar, y guardar toda esta
      información.

   .. hint:: Para recibir y pasar los parámetros necesitarás utilizar
      funciones variádicas, recuerda lo que comentamos de los operadores
      especiales ``*`` y ``**``. Tendrás que unir los parámetros
      guardados en la clase con los recibidos en ``__call__``.

   .. hint:: Puedes unir tuplas sumándolas. Puede unir diccionarios
      con la función ``dict1.update (dict2)``.

   `Solución <partial.py.txt>`__
