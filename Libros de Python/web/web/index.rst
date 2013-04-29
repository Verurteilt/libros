========================
Curso de Python Avanzado
========================

.. image:: python-logo.png
   :alt: Logo de Python
   :scale: 75%
   :align: right

.. contents:: \

`Descargar todo el contenido completo <web.tar.gz>`__

Información
===========

Este *Curso en Python Avanzado* pretende completar el contenido del
`Curso de Iniciación`_, introduciendo
técnicas más complejas y enfatizando en las buenas prácticas para la
construcción de software orientado a la producción.

¿Cuando?
--------

Todos los días del **9 al 14 de Mayo**, de 9 a 14:30 de la mañana. 25
horas en total.

¿Dónde?
-------

En la sala de juntas del `Instituto Andaluz de Astrofísica`_.

Tutorías
--------

Podéis realizar consultas sobre los contenidos del curso al profesor
en su dirección de correo electrónico: **raskolnikov@gnu.org**

Pizarra Virtual
---------------

Vamos utilizar una pizarra virtual online para facilitar la
interacción en la corrección de ejercicios.

`Accede aquí a la pizarra virtual <http://piratepad.net/iaa-python-avanzado>`__

Requisitos
==========

Para realizar el curso es recomendable utilizar un ordenador para
seguir los ejemplos y ejercicios.

Especialmente durante el cuarto día de clase será necesario utilizar
**una distribución basada en** Debian_ , como Ubuntu_ o la
completamente libre Trisquel_.

Máquina virtual
---------------

Si no disponéis de una distribución de GNU/Linux basada en Debian lo
más fácil es que os instaléis la máquina virtual basada en VirtualBox_
que hemos preparado.

Os podéis `descargar la máquina virtual aquí
<http://www.iaa.es/python/avanzado>`__. Las instrucciones para
instalarla las podéis encontrar en la web del `Curso de Iniciación`_.

Contenidos
==========

*Bloque 0:* El lenguaje en profundidad
--------------------------------------

Materiales
~~~~~~~~~~

- *Tema 0:* Introducción

  - `Diapositivas (PDF) <slides/tema-00.pdf>`__
  - `Código y Ejemplos (tar.gz) <code/tema-00.tar.gz>`__
  - `Ejercicios <ejer/tema-00/index.html>`__

- *Tema 1:* Programación Funcional

  - `Diapositivas (PDF) <slides/tema-01.pdf>`__
  - `Código y Ejemplos (tar.gz) <code/tema-01.tar.gz>`__
  - `Ejercicios <ejer/tema-01/index.html>`__

- *Tema 2:* Orientación a Objetos

  - `Diapositivas (PDF) <slides/tema-02.pdf>`__
  - `Código y Ejemplos (tar.gz) <code/tema-02.tar.gz>`__
  - `Ejercicios <ejer/tema-02/index.html>`__

- *Tema 3:* Cuestiones Avanzadas

  - `Diapositivas (PDF) <slides/tema-03.pdf>`__
  - `Código y Ejemplos (tar.gz) <code/tema-03.tar.gz>`__
  - `Ejercicios <ejer/tema-03/index.html>`__

*Bloque 1:* Interfaces Gráficas
-------------------------------

Materiales
~~~~~~~~~~

- *Tema 4:* Introducción a GTK

  - `Diapositivas (PDF) <slides/tema-04.pdf>`__
  - `Código y Ejemplos (tar.gz) <code/tema-04.tar.gz>`__
  - `Ejercicios <ejer/tema-04/index.html>`__

- *Tema 5:* Diseñando aplicaciones con Glade

  - `Diapositivas (PDF) <slides/tema-05.pdf>`__
  - `Código y Ejemplos (tar.gz) <code/tema-05.tar.bz2>`__
  - `Ejercicios <ejer/tema-05/index.html>`__

Requisitos
~~~~~~~~~~

Para este tema hacen falta Glade_, GTK_ y sus *bindings* para Python,
PyGTK_. Se pueden instalar en un sistema basado en Debian con el
comando::

  sudo apt-get install python-gtk2-dev glade

Si usáis el entorno Gnome, es mejor instalar::

  sudo apt-get install glade-gnome

Este software está preinstalado en la máquina virtual que se describe
más arriba.

*Bloque 2:* Producción de Software
----------------------------------

Materiales
~~~~~~~~~~

- *Tema 6:* Pruebas de calidad

  - `Diapositivas (PDF) <slides/tema-06.pdf>`__
  - `Código y Ejemplos (tar.gz) <code/tema-06.tar.gz>`__
  - `Ejercicios <ejer/tema-06/index.html>`__

- *Tema 7:* Bibliotecas externas

  - `Diapositivas (PDF) <slides/tema-07.pdf>`__
  - `Código y Ejemplos (tar.gz) <code/tema-07.tar.gz>`__
  - `Ejercicios <ejer/tema-07/index.html>`__


- *Tema 8:* Distribución del software

  - `Diapositivas (PDF) <slides/tema-08.pdf>`__
  - `Código y Ejemplos (tar.gz) <code/tema-08.tar.gz>`__
  - `Ejercicios <ejer/tema-08/index.html>`__

Requisitos
~~~~~~~~~~

En este bloque es necesario el software PyFlakes_, PyLint_ y
PyChecker_, en el tema 6. Además, hace falta el
compilador GCC_ en tema 7. En el tema 8 es necesario Stdeb_ y
Setuptools_.

Todo esto puede instalarse en una distribución basada en Debian con el
comando::

  $ sudo apt-get install pyflakes pylint pychecker build-essential \
                         python-stdeb python-setuptools

*Bloque 3:* Sistemas Web
------------------------

Para este bloque, que finalmente no dio tiempo a dar, no llegamos a
preparar materiales específicos. Sin embargo, os dejo los siguientes
enlaces y materiales que pueden ser útiles para guiar vuestro estudio.

#. `Diapositivas de curso de introducción a Django
   <http://django.es/blog/diapositivas-curso-introduccion-django/>`__

   Estas diapositivas son de un curso de introducción a Django que
   cubre todo y más de lo que pensábamos dar en nuestro curso. Buena
   parte de las diapositivas están organizadas a modo de tutorial y
   puede ser útil seguirlas paso a paso para realizar una primera
   aproximación a Django.

#. `Documentación oficial de Django <http://docs.djangoproject.com/en/1.3/>`__

   La documentación oficial de Django es muy extensiva. A parte de la
   documentación de referencia, es muy recomendable `seguir el
   tutorial
   <http://docs.djangoproject.com/en/1.3/intro/tutorial01/>`__ paso a
   paso para realizar una primera incursión en el sistema.

#. `Código fuente del proyecto YAAS <code/yaas.tar.gz>`__

   El año pasado programé el proyecto *Yet Another Auction Service*
   como parte de un curso de desarrollo web. Es una página de subastas
   muy sencilla, que puede servir de ejemplo. Como apuntes
   interesantes, tiene una API web basada en `REST
   <http://es.wikipedia.org/wiki/Representational_State_Transfer>`__,
   pruebas de unidad usando el sistema específico de Django y presenta
   gráficas usando Matplotlib.

Material adicional
==================

Configuración de Emacs
----------------------

A algunos alumnos os ha gustado las facilidades que ofrece Emacs_ el
como editor de Python. Os indico aquí los trucos especiales de nuestra
configuración configuración personal de Emacs_.

Integración de IPython
~~~~~~~~~~~~~~~~~~~~~~

Lo primero que necesitáis es el ``python-mode`` avanzado mantenido por
la comunidad de Emacs, que sustituye al que viene por defecto con el
paquete. El módulo ``pymacs`` además permite extender Emacs en lenguaje
de programación Python. Los instalamos en Debian y derivados con::

  $ sudo apt-get install pymacs python-mode ipython

Para integrar IPython_ correctamente es necesario un módulo adicional
para Emacs, que podéis descargar aquí: `ipython.el <ipython.el>`__

Una vez hecho esto, debéis indicar a Emacs la carpeta dónde tenéis
instalado el módulo y que lo cargue. Por ejemplo, yo lo tengo
instalado en ``~/.emacs.d/lisp/ipython.el``, y mi fichero de
configuración de Emacs ``~/.emacs`` incluye estas lineas::

  (add-to-list 'load-path (expand-file-name "~/.emacs.d/lisp"))
  
  (require 'ipython)

Una vez hecho esto, ya podéis lanzar el intérprete IPython dentro de
Emacs ejecutando ``M-x py-shell`` o directamente con ``C-c !``. Cuando
está abierta, podéis enviar el fichero de Python actual entero al
intérprete de Python ejecutando ``C-c C-c``. Además, mi fichero de
configuración de Emacs contiene::

  (eval-after-load "python-mode"
  '(progn
     (add-hook 'python-mode-hook 
	       (lambda () 
		 (local-set-key (kbd "C-c C-e") 'py-execute-region)))))

Una vez configurado así Emacs permite enviar al intérprete sólo la
región seleccionada actualmente con el comando ``C-c C-e``.

Integración de PyFlakes
~~~~~~~~~~~~~~~~~~~~~~~

Como veremos en el tema 7 del curso, el programa PyFlakes_ permite
realizar algunas comprobaciones de errores de programación en Python,
como comprobar que las variables que usamos han sido declaradas, o que
los `import` que realizamos se usan realmente en el código.

Podemos hacer que Emacs muestre automáticamente en rojo las lineas
erróneas detectadas por PyFlakes_ integrándolo con el módulo
``flymake``, que viene de serie con Emacs desde su versión 23. En
concreto, las lineas de configuración necesarias son::

  (require 'flymake)

  (defun flymake-pyflakes-init () 
    ;; Make sure it's not a remote buffer or flymake would not work
    (let* ((temp-file (flymake-init-create-temp-buffer-copy 
  		     'flymake-create-temp-inplace)) 
  	 (local-file (file-relative-name 
  		      temp-file 
  		      (file-name-directory buffer-file-name)))) 
      (list "pyflakes" (list local-file))))

  (setq flymake-allowed-file-name-masks '(("\\.py\\'"  flymake-pyflakes-init)))


FlyMake es una herramienta muy potente, nos permite además integrar el
resaltado de errores en muchos otros formatos, como LaTeX, o incluso
otros compilados como C. Tenéis `más información aquí
<http://www.emacswiki.org/emacs/FlyMake>`__.

Parece que FlyMake no se lleva muy bien con IPython, pero las
siguientes lineas de configuración solucionan el problema::

  (add-hook 'python-mode-hook 
	  (lambda ()
	    (unless (eq buffer-file-name nil) (flymake-mode t))))

¡A disfrutar programando en Python con Emacs!

.. _`Curso de Iniciación`: http://www.iaa.es/python
.. _`Instituto Andaluz de Astrofísica`: http://www.iaa.es
.. _Debian: http://www.debian.org
.. _Ubuntu: http://www.ubuntu.com
.. _Trisquel: http://www.trisquel.info
.. _VirtualBox: http://www.virtualbox.org
.. _Emacs: http://www.gnu.org/software/emacs
.. _IPython: http://ipython.scipy.org/
.. _PyFlakes: https://launchpad.net/pyflakes
.. _GTK: http://www.gtk.org/
.. _PyGTK: http://www.pygtk.org/
.. _Glade: http://glade.gnome.org/
.. _PyLint: http://www.logilab.org/857
.. _PyFlakes: https://launchpad.net/pyflakes
.. _PyChecker: http://pychecker.sourceforge.net/
.. _GCC: http://gcc.gnu.org/
.. _Stdeb: https://github.com/astraw/stdeb
.. _Setuptools: http://pypi.python.org/pypi/setuptools

---------

*(c) Juan Pedro Bolívar Puente 2011* — `Código fuente ReStructuredText <index.rst>`__
