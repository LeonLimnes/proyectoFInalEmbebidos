# ## ###############################################
#
# transfer.py
#
#
# Autor: César Augusto Martínez Franco
#        Lisset Noriega Domínguez
#       Quiroz hernandez Rodolfo
#       Jesús Arturo Vázquez Zaragoza
# License: MIT
#
# ## ###############################################

from time import sleep
import os
import re
from copyRoms import copyFiles
from listRoms import guiListRoms
from stop_continue_process import get_id
from stop_continue_process import kill_mednafen
from stop_continue_process import continue_mednafen
sleep(3)
devices = os.popen('sudo blkid').readlines()
usbs = []
for u in devices:
    loc = [u.split(':')[0]]
    if '/dev/sd' not in loc[0]: 
          continue # skip 
    loc+=re.findall(r'"[^"]+"',u)
    columns = ['loc']+re.findall(r'\b(\w+)=',u)
    
    usbs.append(dict(zip(columns,loc)))
for u in usbs:
    print ("Device {} is located at {} with UUID of {}".format(u["LABEL"],u["loc"],u["UUID"]))
    path = "/media/usb"
    mount_command = "sudo mount -t {} {} {}".format(u["TYPE"].replace('"',""),u["loc"],path)
    unmount_command = "sudo unmount {}".format(path)
    try:
        os.system(mount_command)
        copyFiles(path,"../ROMS/GBC")
        os.system(unmount_command)
    except Exception as e:
        print(e)
    finally:
        lock_path="/tmp/lockUSB.lock"
        if(not os.path.isfile(lock_path)):
            open(lock_path,"x")
            try:
                get_id()
                kill_mednafen()
                guiListRoms()
                continue_mednafen()
            finally:
                os.remove(lock_path)
