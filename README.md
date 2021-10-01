# linux-keyboard-macros
A program to use macros on ANY keyboard on Linux

## Setup
1) Install `evtest` and `xdotool` on your Linux system.
2) Change the used device in `main.py` (the `keyboard_name` should match your keyboard's name in `sudo evtest`: copy from start to end of name!)
3) Configure functions in `functions.py`. Remember: For testing, you have to use `sudo ./main.py`.
4) Add run main.py to /etc/rc.local.

## How it works
It uses `evtest --grab /dev/input/event<id>` to disable the keyboard and map its presses.
Easy!