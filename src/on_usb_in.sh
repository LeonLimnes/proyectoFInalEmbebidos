#!/bin/sh
# ## ###############################################
#
# on_usb_in.sh
# 
#
# Autor: César Augusto Martínez Franco
#        Lisset Noriega Domínguez
#        Rodolfo Quiroz Hernandez 
#        Jesús Arturo Vázquez Zaragoza
# License: MIT
#
# ## ###############################################
set -x
xhost local:pi
export DISPLAY=:0.0

su pi -c '/usr/bin/python3 ./transfer.py &'

