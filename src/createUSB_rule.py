#!/usr/bin/sudo /usr/bin/python3
data="""ACTION=="add", SUBSYSTEM="usb", RUN+="./on_usb_in.sh"
"""
with open("/usr/lib/udev/rules.d/10-myDevice.rules", "w+") as file_rule:
    file_rule.write(data)
    file_rule.close()