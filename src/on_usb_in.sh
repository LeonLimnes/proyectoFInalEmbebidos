#!/bin/sh
set -x
xhost local:pi
export DISPLAY=:0.0

su pi -c '/usr/bin/python3 ./transfer.py &'

