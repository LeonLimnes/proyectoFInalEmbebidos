import os
import shutil as sh

def copyFiles(sourceDir, destDir):
    fileExt = ".gbc"
    ROMS = []
    for file in os.listdir(sourceDir):
        if file.endswith(fileExt):
            ROMS.append(file)
    
    for rom in ROMS:
        src = "{}/{}".format(sourceDir,rom)
        dst = "{}/{}".format(destDir,rom)
        sh.copyfile(src,dst)
if __name__ == "_main_":
    copyFiles("/home/pi/Desktop/proyectoFInalEmbebidos/ROMS/GBC","/home/pi/Desktop")