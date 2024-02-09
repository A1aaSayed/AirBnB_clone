#!/usr/bin/python3
"""Entry point of the command interpreter"""

import cmd


class HBNBCommand(cmd.Cmd):
    """Command interpreter for hbnb"""

    prompt = '(hbnb) '

    def do_quit(self, line):
        """Exit the program"""
        return True

    def do_EOF(self, line):
        """Exit the program"""
        return True
    
    def emptyline(self):
        """Execute anything when press Enter"""
        pass

   
    

if __name__ == '__main__':
    HBNBCommand().cmdloop()
