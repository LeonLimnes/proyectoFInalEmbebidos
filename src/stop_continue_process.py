#!/usr/bin/sudo /usr/bin/python3

import os
tmpFile = "/tmp/id_mednafen.txt"

def get_id():
    os.system("touch {}".format(tmpFile))
    os.system('pgrep "mednafen" > {}'.format(tmpFile))
    
def kill_mednafen():
    with open(tmpFile, 'r') as file:
        id_mednafen = file.read()
        os.system('kill -STOP {}'.format(id_mednafen))
       
def continue_mednafen():
    with open(tmpFile, 'r') as file:
        id_mednafen = file.read()
        os.system('kill -CONT {}'.format(id_mednafen))

get_id()