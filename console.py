#!/usr/bin/python3
"""Entry point of the command interpreter"""

import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class HBNBCommand(cmd.Cmd):
    """Command interpreter for hbnb"""

    prompt = '(hbnb) '
    classes = ['BaseModel', 'User', 'State', 'City',
               'Amenity', 'Place', 'Review']

    def do_create(self, line):
        """Creates a new instance of BaseModel"""
        if not line:
            print('** class name missing **')
        else:
            command = line.split()
            class_name = command[0]
            if command[0] not in self.classes:
                print("** class doesn't exist **")
            else:
                instance = eval(class_name)()
                instance.save()
                print(instance.id)

    def do_show(self, line):
        """Prints the string representation of an instance"""
        if not line:
            print('** class name missing **')
        else:
            command = line.split()
            if command[0] not in self.classes:
                print("** class doesn't exist **")
            if len(command) < 2:
                print('** instance id missing **')
            else:
                instances = storage.all()
                key = f'{command[0]}.{command[1]}'
                if key in instances:
                    print(instances[key])
                else:
                    print('** no instance found **')

    def do_destroy(self, line):
        """Deletes an instance"""
        if not line:
            print('** class name missing **')
        else:
            command = line.split()
            if command[0] not in self.classes:
                print("** class doesn't exist **")
            if len(command) < 2:
                print('** instance id missing **')
            else:
                instance = storage.all()
                key = f'{command[0]}.{command[1]}'
                if key in instance:
                    del instance[key]
                    storage.save()
                else:
                    print('** no instance found **')

    def do_all(self, line):
        """Prints all string representation"""
        command = line.split()
        instance = storage.all()
        instances = []
        for value in instance.values():
            instances.append(str(value))
        if line:
            if line not in self.classes:
                print("** class doesn't exist **")
            else:
                print(instances)
        else:
            print(instances)

    def do_update(self, line):
        """Updates an instance"""
        if not line:
            print('** class name missing **')
        else:
            command = line.split()
            if command[0] not in self.classes:
                print("** class doesn't exist **")
            if len(command) < 2:
                print('** instance id missing **')
            else:
                instance = storage.all()
                key = f'{command[0]}.{command[1]}'
                if key not in instance:
                    print('** no instance found **')
                if len(command) < 3:
                    print('** attribute name missing **')
                if len(command) < 4:
                    print('** value missing **')
                setattr(instance[key], command[2], command[3])
                instance[key].save()

    def do_quit(self, line):
        """Exit the program"""
        return True

    def do_EOF(self, line):
        """Exit the program"""
        print()
        return True

    def emptyline(self):
        """Execute anything when press Enter"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
