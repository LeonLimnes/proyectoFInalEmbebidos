from time import sleep
import os
import re
from copyRoms import copyFiles
from listRoms import guiListRoms
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
        copyFiles(path,"/home/pi/Desktop/proyectoFInalEmbebidos/ROMS/GBC")
        os.system(unmount_command)
    except Exception as e:
        print(e)
lock_path="/tmp/lockUSB.lock"
if(not os.path.isfile(lock_path)):
     open(lock_path,"x")
     guiListRoms()
     os.remove(lock_path)