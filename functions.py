from pynput.keyboard import Controller

keyboard = Controller()

def write(text):
    keyboard.type(text)


# In this file, you should have a run option to be run each time the user will press a button. The argument is the int of the keycode.
def run(code):
    if code == 458762:
        write("linux-keyboard-macros github page: https://github.com/tarneaux/linux-keyboard-macros\n")
    else:
        print(code)
