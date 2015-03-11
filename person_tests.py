import unittest
from addressbook_pb2 import *

class PersonTests(unittest.TestCase):

    def test_i_can_create_a_stream(self):
        person = Person()
        person.name = "Omar Abdelhafith"
        person.id = 123

        phone = person.phone.add()
        phone.number = "0831871340"
        phone.type = Person.HOME

        print (person.SerializeToString())