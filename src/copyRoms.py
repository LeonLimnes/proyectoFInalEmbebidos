# ## ###############################################
#
# copyRoms.py
# 
#
# Autor: César Augusto Martínez Franco
#        Lisset Noriega Domínguez
#        Rodolfo Quiroz Hernandez 
#        Jesús Arturo Vázquez Zaragoza
# License: MIT
#
# ## ###############################################
import os
import shutil

def copyFiles(sourceDir, destDir):
    """copy roms, from sourceDir to distDir

    Args:
        sourceDir (String): source directory
        destDir (_type_): destiny directory
    """

    fileExt = ".gbc"
    ROMS = []
    for file in os.listdir(sourceDir):
        if file.endswith(fileExt):
            ROMS.append(file)
    for rom in ROMS:
        src = "{}/{}".format(sourceDir,rom)
        dst = "{}/{}".format(destDir,rom)
        try:
            shutil.copy(src, dst)
        except shutil.SameFileError:
            print('Ya se encuentra el archivo')
        except PermissionError:
            print('Permiso denegado')
        except:
            print('Ocurrió un error al copiar los archivos')

#copyFiles("/home/pi/Desktop/proyectoFInalEmbebidos/ROMS/GBC","/home/pi/Desktop")