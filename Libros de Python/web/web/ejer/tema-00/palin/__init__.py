# -*- coding: utf-8 -*-

"""

Módulo para la evaluación de palíndromos.

"""

def es_palindromo (seq):
    """

    Comprueba que una secuencia es una palíndromo, es decir, que puede
    leerse igual hacia adelante o hacia atrás.
    
      :param seq: Secuencia a comprobar si es palíndromo.
      
      :return: ``True`` si la secuencia es un palíndromo y ``False``
               en caso contrario.
    
    """

    total = len (seq)
    for x in range (len (seq) / 2):
        if seq [x] != seq [total - x - 1]:
            return False
    return True

def palindromos (frase):
    """
    
    Comprueba que una frase y sus palabras son palíndromos.
    
      :param seq: La secuencia a comprobar.
    
      :return: Una pareja dónde el primer elemento indica si la frase
               es un palíndromo, y el segundo elemento es un
               diccionario que indica si cada palabra de la frase lo
               es.
    
    """

    palabras = frase.split (' ')
    palin_palab = dict ()
    for x in palabras:
        if x not in palin_palab:
            palin_palab [x] = es_palindromo (x)
    return es_palindromo (palabras), palin_palab
