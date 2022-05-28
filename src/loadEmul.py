#!/usr/bin/sudo /usr/bin/python3
def startupConfig(emulName):
    with open("/home/pi/.xsessionrc","w+") as file_emul:
        file_emul.write("STARTUP=")
        file_emul.close()
    config = """#!/bin/sh
xset s off     # NO activar salvapantallas
xset -dpms     # Deshabilitar DPMS
xset s noblank # NO poner en negro la pantalla
{}
""".format(emulName)
    with open("/home/pi/.Xsession","w+") as file_emul:
        file_emul.write(config)
        file_emul.close()
    
def loadEmul(emulName):
    startupConfig(emulName)
    
loadEmul("mednaffe")
    