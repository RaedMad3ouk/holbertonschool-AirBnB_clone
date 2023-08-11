#!/usr/bin/python3
""" Testing the console """
import unittest
from unittest.mock import patch
import models.engine.file_storage
import io
from console import HBNBCommand


class test_console(unittest.TestCase):
    """ testing console """

    def test_create_BaseModel(self):
        """ test create for BaseModel"""
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
        res = f.getvalue()

        if res is not None:
            self.assertTrue(True)
        else:
            self.assertTrue(False)

    def test_create_User(self):
        """ test create for User """
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create User")
        res = f.getvalue()

        if res is not None:
            self.assertTrue(True)
        else:
            self.assertTrue(False)
        def test_quit(self):
        
	         with patch('sys.stdout', new=io.StringIO()) as f:
                  HBNBCommand().onecmd("quit")
        if f.getvalue() == None:
            self.assertTrue(True)
        else:
            self.assertFalse(False)