
==========
Ejercicios
==========

-------------------------------
 *Tema 7:* Interfaces software
-------------------------------

Ctypes
======

#. Realiza en C o Fortran una función que calcula el máximo común
   divisor de dos números. Utiliza el sencillo Algoritmo de Euclides,
   e implementa una interfaz con Ctypes. El código en C que puedes
   utilizar es este::

        int mcd (int a, int b)
        {
          if (a < 0)
            a = -a;
          if (b < 0)
            b = -b;
        
          a = a % b;
          if (a > 0)
            return mcd (b, a);
          else
            return b;
        }

   `Solución <mcd.tar.gz>`__

#. Implementa una clase ``MyArray`` que es un vector de enteros que
   utiliza C para manejar los datos. La clase debe reservar la memoria
   con ``malloc`` de la biblioteca estándar y liberarlo con
   ``free``. La liberación de la memoria debe ser transparente al
   usuario. La clase puede proveer un método ``zero`` que pone a 0
   todos los datos usando ``memset``. Puedes hacerla usando los
   envoltorios de ``numpy`` o los estándar de ``ctypes``.

   .. hint:: Reserva la memoria en el constructor y libera la memoria
      en el finalizador de la clase, es decir, ``__del__``.

   .. hint:: Es posible que en tu implementación tengas que utilizar
      casting de C desde Python (por ejemplo, para convertir entre
      ``void*`` e ``int*``), puedes utilizar la función
      ``ctypes.cast(valor, tipo_destino)``.

   `Solución <myarray.py.txt>`__

Numpy
=====

#. Programa en C o Fortran una función que calcula la norma de un
   vector de ``float`` de ``n`` componentes. Realiza una interfaz con
   ``ctypes`` y ``numpy`` para utilizarla en Python. La función en C
   puede ser algo así::
   
     float norm (float* data, size_t size)
     {
       float* end = data + size;
       float  res = 0;
     
       while (data < end)
         {
           res += *data * *data;
           ++ data;
         }
     
       return sqrtf (res);
     }
 

   .. hint:: Crea una función que envuelva la llamada a la biblioteca
      en C para extraer el tamaño del ``array`` y pasarlo al segundo
      argumento.

   `Solución <norm.tar.gz>`__

#. Escribe una función que ordene un ``array`` unidimensional de
   ``numpy`` utilizando la función ``qsort ()`` de C. La función debe
   funcionar para cualquier tipo de datos.

   .. hint:: Tienes que definir el tipo de la función comparadora
      dentro de un envoltorio que de la función ``qsort`` para poder
      adaptarla al tipo del ``array`` en concreto.

   .. hint:: La función ``numpy.ctypeslib.as_ctypes`` puede ser de
      utilidad. El tipo del objeto que devuelve no puede ser usado
      directamente en una signatura de *ctypes*, pero podemos acceder
      al tipo de los objetos apuntados a través del atributo
      ``_type_``.

   `Solución <sort.py.txt>`__
