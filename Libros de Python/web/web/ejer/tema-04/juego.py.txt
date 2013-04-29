# -*- coding: utf-8 -*-

import pygtk
pygtk.require('2.0')
import gtk

import random

def handle_click (obj, good, label):
    label.props.label = "¡Ganaste!" if good else "Frío frío..."

def juego ():
    win = gtk.Window ()
    win.connect ('destroy', gtk.main_quit)
    win.props.title = "El juego más divertido"
    win.props.allow_grow = False
    
    vbox = gtk.VBox (False, 0)
    win.add (vbox)

    label = gtk.Label ("¡Elige una opción!")
    vbox.pack_start (label)

    hbox = gtk.HButtonBox ()
    vbox.pack_start (hbox)
    
    buttons = [ [gtk.Button ("Vaso " + str (i)), False]
                for i in range (1, 4) ]
    random.choice (buttons) [1] = True
    for but, good in buttons:
        hbox.pack_start (but)
        but.connect ("clicked", handle_click, good, label)
    
    win.show_all ()
    gtk.main ()

if __name__ == '__main__':
    juego ()
