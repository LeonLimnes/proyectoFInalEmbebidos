#!/bin/sh
sleep 10
mv /home/pi/Desktop/proyectoFInalEmbebidos/src/Rasp.lyt /home/pi/.qjoypad3
rm /tmp/lockUSB.lock
qjoypad "Rasp"