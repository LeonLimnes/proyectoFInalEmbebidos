#!/bin/sh
set -x
xhost local:pi
export DISPLAY=:0.0
LOG_FILE=/home/pi/Desktop/proyectoFInalEmbebidos/src/hola.log
id_rom=$(pgrep mednafe)
kill -STOP $id_rom
/usr/bin/python3 /home/pi/Desktop/proyectoFInalEmbebidos/src/transfer.py
kill -CONT $id_rom
su pi -c '/usr/bin/python3 /home/pi/Desktop/proyectoFInalEmbebidos/src/listRoms.py &'