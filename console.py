#!/usr/bin/python3
"""Console module"""
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Console class"""
    prompt = '(hbnb)'
    class_map = [
        "BaseModel",
        "User",
        "State",
        "Review",
        "Place",
        "City",
        "Amenity"
    ]

    def do_quit(self, line):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, line):
        """End of File to exit file."""
        return True

    def emptyline(self):
        """method so it should not execute anything"""
        pass

    def do_create(self, line):
        """Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id"""
        if not line:
            print('** class name missing **')
            return
        if line not in self.class_map:
            print("** class doesn't exist **")
            return
        else:
            x = eval("{}()".format(line))
            storage.save()
            print('{}'.format(x.id))

    def do_show(self, line):
        """Prints the string representation of an instance
        based on the class name and id"""
        linesplit = line.split()
        if not line:
            print('** class name missing **')
            return
        if linesplit[0] not in self.class_map:
            print("** class doesn't exist **")
            return
        if len(linesplit) == 1:
            print('** instance id missing **')
            return
        try:
            line = line.replace(' ', '.')
            all_obj = storage.all()
            obj = all_obj[line]
            print(obj)
        except Exception:
            print('** no instance found **')

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        linesplit = line.split()
        if not line:
            print('** class name missing **')
            return
        if linesplit[0] not in self.class_map:
            print("** class doesn't exist **")
            return
        if len(linesplit) == 1:
            print('** instance id missing **')
            return
        try:
            line = line.replace(' ', '.')
            all_obj = storage.all()
            del all_obj[line]
            storage.save()
        except Exception:
            print('** no instance found **')

    def do_all(self, line):
        """Prints all string representation of all instances
        based or not on the class name"""
        if not line:
            obj_list = []
            all_obj = storage.all()
            for items in all_obj.values():
                obj_list.append(str(items))
            print(obj_list)
            return
        if line in self.class_map:
            obj_list = []
            all_obj = storage.all()
            for items in all_obj.values():
                if line in str(items):
                    obj_list.append(str(items))
            print(obj_list)
            return
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """Updates an instance based on the class name and id
        by adding or updating attribute"""
        linesplit = line.split()
        if not line:
            print('** class name missing **')
            return
        if linesplit[0] not in self.class_map:
            print("** class doesn't exist **")
            return
        if len(linesplit) == 1:
            print('** instance id missing **')
            return
        if len(linesplit) == 2:
            print('** attribute name missing **')
            return
        if len(linesplit) == 3:
            print('** value missing **')
            return
        try:
            line = line.replace(' ', '.', 1)
            linesplit = line.split()
            all_obj = storage.all()
            obj = all_obj[linesplit[0]]
            setattr(obj, linesplit[1], linesplit[2])
            storage.save
        except Exception:
            print('** no instance found **')


if __name__ == '__main__':
    HBNBCommand().cmdloop()
