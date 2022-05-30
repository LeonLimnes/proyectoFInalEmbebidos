#!/usr/bin/sudo /usr/bin/python3
import os

pfile = '/etc/xdg/lxsession/LXDE-pi/autostart'

text = """#@lxpanel --profile LXDE-pi
#@pcmanfm --desktop --profile LXDE-pi
@python3 /path/your_program
"""

with open(pfile, 'w+') as file:
    file.write(text)
    file.close()