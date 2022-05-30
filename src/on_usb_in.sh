#!/bin/sh
set -x
xhost local:pi
export DISPLAY=:0.0
LOG_FILE=/home/pi/Desktop/proyectoFInalEmbebidos/src/hola.log


su pi -c '/usr/bin/python3 /home/pi/Desktop/proyectoFInalEmbebidos/src/transfer.py &'

