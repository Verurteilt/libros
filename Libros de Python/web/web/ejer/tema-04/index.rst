
==========
Ejercicios
==========

------------------------------
 *Tema 4:* Introducción a GTK
------------------------------

Interfaces Gráficas
===================

#. Escribir un programa gráfico con GTK para jugar al juego en el que
   se esconde una moneda bajo uno de tres vasos opacos. El programa,
   inicialmente, debe mostrar tres botones con el texto "1", "2", y
   "3" y una etiqueta que invite al usuario a pulsar uno de los
   botones. Si la elección del usuario coincide con un valor
   pseudoaleatoreo la etiqueta debe mostrar un mensaje de éxito, o
   indicar el fallo en caso contrario. Para simplificar el programa,
   se puede asumir que el usuario puede hacer tantos intentos como sea
   necesario.

   .. hint:: Usa un ``gtk.Button`` para los botones y un ``gtk.Label``
      para mostrar los mensajes.

   .. hint:: Para realizar el *layout*, puedes crear una ``VBox`` y
      una ``HButtonBox``. La jerarquía de *widgets* puede ser algo
      así::

        * Win
          - VBox
            - Label
            - HButtonBox
              - Button
	      - Button
	      - Button

   .. hint:: Conecta una señal a cada botón que cambie el mensaje de
      la etiqueta. En la conexión puedes fijar un parámetro que le
      indique al manejador si ese botón es la opción correcta para que
      sepa que texto establecer en la etiqueta. Otra opción es tener
      dos manejadores diferentes para establecer si se ha ganado o se
      ha perdido, y conectar uno a la opción correcta y el otro
      manejador con los botones que reciben la opción incorrecta.

   `Solución <juego.py.txt>`__

#. Reescribir el programa de la calculadora que desarrollamos en el
   tema de programación funcional utilizando una interfaz en GTK. El
   widget `gtk.TextEntry
   <http://www.pygtk.org/docs/pygtk/class-gtkentry.html>`__ que no
   hemos visto en las diapositivas puede ser de utilidad.

   .. hint:: La ``gtk.Entry`` tiene señal ``activate`` que es emitida cuando
      el usuario pulsa la tecla *intro*, puedes usarla para disparar
      el cálculo.

   .. hint:: Establece un manejador que realizar el cálculo conectado
      al cálculo. El código para realizar el cálculo muy parecido a la
      versión por consola, sólo que el texto debe extraerse de la
      propiedad ``text`` del ``gtk.Entry``, y el resultado debe
      almacenarse en el ``label`` de la ``gtk.Label``.

   `Solución <calcu.py.txt>`__

#. Modifica el programa anterior para que calcule con cualquier
   expresión válida de Python. Utiliza para ello la función `eval
   <http://docs.python.org/library/functions.html#eval>`__ de
   Python. Esta función puede ocasionar problemas usada
   descuidadamente, `este artículo
   <http://lybniz2.sourceforge.net/safeeval.html>`__ puede darte
   pistas de cómo utilizar esa función de forma segura.

   .. hint:: Aunque normalmente está contraindicado capturar
      ``Exception``, porque podríamos ocultar errores de programación,
      es correcto capturar ``Exception`` justo alderredor de la
      llamada a ``eval`` para 

   .. hint:: Toma directamente la cadena del usuario y envíasela a
      ``eval``, el resultado lo conviertes en una cadena con ``str``.

   .. hint:: Pasale a ``eval`` un segundo parámetro con un diccionario
      asociando los nombres de funciones permitidas a las funciones
      que las ejecutan. De lo contrario el usuario podría invocar a
      funciones peligrosas.

   `Solución <calcu2.py.txt>`__

