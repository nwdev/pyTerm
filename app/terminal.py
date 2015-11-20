import os
from shell import Shell


class Terminal():

    def __init__(self):
        self.curdir = os.path.dirname(os.path.realpath(__file__))

    def three_level_dir_repr(self):
        pretty_dir_repr = ''
        dir_levels = self.curdir.split('/')
        if len(dir_levels) > 3:
            pretty_dir_repr = "%s/%s/%s$ " %\
            (dir_levels[-3], dir_levels[-2], dir_levels[-1])
        return pretty_dir_repr

    def run(self):
        shell = Shell()
        print(self.three_level_dir_repr(), end='')
        command = input().strip()
        while(command != 'exit'):
            ret_msg = shell.process_command(command)
            print(ret_msg)
            print(self.three_level_dir_repr(), end='')
            command = input().strip()

if __name__ == "__main__":
    terminal = Terminal()
    terminal.run()
