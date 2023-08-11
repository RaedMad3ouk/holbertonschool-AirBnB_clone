#!/usr/bin/python3

""" console for AirBnb """
import cmd
import ast
from datetime import datetime as dt
from models.__init__ import storage
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

classes = {"BaseModel": BaseModel,
           "Amenity": Amenity,
           "City": City,
           "Place": Place,
           "Review": Review,
           "State": State,
           "User": User}


class HBNBCommand(cmd.Cmd):
    """ entry point of the command interpreter """

    prompt = "(hbnb) "

    def do_quit(self, args):
        """ Quits the program """
        return True

    def emptyline(self):
        """ handles empty lines """
        pass

    def do_EOF(self, args):
        """ Reads EOF and exits """
        return True

    def do_create(self, args):
        """ creates a new instance of BaseModel """
        if not args:
            print("** class name missing **")
        elif args in classes.keys():
            new = classes[args]()
            new.save()
            storage.reload()
            print(new.id)
        else:
            print("** class doesn't exist **")
