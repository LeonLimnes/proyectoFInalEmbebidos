#!/usr/bin/sudo /usr/bin/python3
# ## ###############################################
#
# createUSB_rule.py
# 
#
# Autor: César Augusto Martínez Franco
#        Lisset Noriega Domínguez
#        Rodolfo Quiroz Hernandez 
#        Jesús Arturo Vázquez Zaragoza
# License: MIT
#
# ## ###############################################

"""Create the USB rules
"""
data="""ACTION=="add", SUBSYSTEM="usb", RUN+="/home/pi/Desktop/proyectoFInalEmbebidos/src/on_usb_in.sh"
"""
with open("/usr/lib/udev/rules.d/10-myDevice.rules", "w+") as file_rule:
    file_rule.write(data)
    file_rule.close()
