#! /bin/bash

cd /home/max/Desktop/Projects/linux-keyboard-macros/
export DISPLAY=:0
export XAUTHORITY=/home/max/.Xauthority
python3 main.py
# tmux new-session -c /home/max/Desktop/Projects/linux-keyboard-macros/ -s macros -d python3 main.py
