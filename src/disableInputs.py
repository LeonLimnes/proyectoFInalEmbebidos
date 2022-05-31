#!/usr/bin/sudo /usr/bin/python3
# ## ###############################################
#
# disableInputs.py
# 
#
# Autor: César Augusto Martínez Franco
#        Lisset Noriega Domínguez
#        Rodolfo Quiroz Hernandez 
#        Jesús Arturo Vázquez Zaragoza
# License: MIT
#
# ## ###############################################
"""Disable TouchPad, keyboard and mouse
"""
import os
from time import sleep

tmpFile = "/tmp/disable_inputs.txt"
os.system("touch {}".format(tmpFile))
os.system('xinput | grep "keyboard" > {}'.format(tmpFile))
os.system('xinput | grep "Mouse" >> {}'.format(tmpFile))

with open(tmpFile,"r") as file:
    data = file.read()
    idList = []
    tokens = data.split()
    for token in tokens:
        if token.startswith("id="):
            idList.append(token[3:])
    for id_device in idList:
        os.system("xinput disable {}".format(id_device))
    file.close()
    #sleep(60)
    #for id_device in idList:
        #os.system("xinput enable {}".format(id_device))