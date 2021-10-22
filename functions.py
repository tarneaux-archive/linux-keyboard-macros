import pyautogui
from os import system
from get_window import wt


def write(text):
    pyautogui.write(text)

def as_user(command):
    system("sudo -u max " + command)

system("chmod +x /home/max/.tmuxwindows/*")

class Handler:
    def __init__(self):
        self.ctrl_pressed = False
        self.commands = {
            458832: "tmux select-pane -L",
            458831: "tmux select-pane -R",
            458833: "tmux select-pane -D",
            458834: "tmux select-pane -U",
            458778: "tmux splitw -bv",
            458756: "tmux splitw -bh",
            458774: "tmux splitw -v",
            458759: "tmux splitw -h",
            458766: "tmux kill-pane",
            458769: "tmux new-window",
            458796: "tmux next-window",
            458793: "tmux kill-window",
            458775: "tmux resize-pane -U 5",
            458761: "tmux resize-pane -L 5",
            458762: "tmux resize-pane -D 5",
            458763: "tmux resize-pane -R 5",
            458758: "tmux send-keys -t \"$pane\" C-z 'source ~/.tmuxwindows/p10kwithoutsegments && clear' Enter",
            458777: "tmux send-keys -t \"$pane\" C-z 'source ~/.p10k.zsh && clear' Enter"
        }
        self.minecraft_macros = {
            458766: "!kill SassukeNew\n"
        }
    
    def on_press(self, code):
        if code == 458976:
            self.ctrl_pressed = not self.ctrl_pressed
        elif not self.ctrl_pressed:
            if wt() == b'~ : bash' and code in self.commands.keys():
                as_user(self.commands[code])
            elif wt().startswith(b'Minecraft*') and code in self.minecraft_macros.keys():
                write(self.minecraft_macros[code])
            else:
                print(code, wt())
        elif self.ctrl_pressed:
            pass
    
    def on_release(self, code):
        if code == 458976:
            self.ctrl_pressed = not self.ctrl_pressed
