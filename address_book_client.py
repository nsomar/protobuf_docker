__author__ = 'omarsubhiabdelhafith'

import addressbook_pb2

_TIMEOUT_SECONDS = 10


def add_person(stub, name, id, email):
    person = addressbook_pb2.Person()

    person.name = name
    person.id = id
    person.email = email

    # Add a person
    response = stub.AddAddressEntry(addressbook_pb2.AddressAddRequest(person=person), _TIMEOUT_SECONDS)
    print response.message


def get_all_people(stub):
    response = stub.DisplayAllAddresses(addressbook_pb2.DisplayAllAddressesRequest(), _TIMEOUT_SECONDS)
    for person in response.items:
        print "Found contact with name = %s, id = %d" % (person.name, person.id)

def search_for_person(stub, name="", email=""):
    response = stub.SearchForAddress(addressbook_pb2.SearchForAddressRequest(name=name, email=email), _TIMEOUT_SECONDS)
    for person in response.items:
        print "Found contact with name = %s, id = %d" % (person.name, person.id)

def clear_contacts(stub):
    stub.DeleteAll(addressbook_pb2.DeleteAllRequest(), _TIMEOUT_SECONDS)

def run():
  with addressbook_pb2.early_adopter_create_Address_stub('localhost', 50052) as stub:
    # response = stub.SayHello(addressbook_pb2.HelloRequest(name='you'), _TIMEOUT_SECONDS)
    # print "Greeter client received: " + response.message

    print("\nAdding contacts ====")
    add_person(stub, "omar", 1, "omar@me.com")
    add_person(stub, "john", 2, "john@me.com")
    add_person(stub, "jack", 3, "jack@me.com")
    add_person(stub, "lucy", 4, "lucy@me.com")

    print("\n\nSearching for name:jack name ====")
    search_for_person(stub, "jack")

    print("\n\nSearching for email:omar@me.com name ====")
    search_for_person(stub, email="omar@me.com")

    print("\n\nGetting all contacts ====")
    get_all_people(stub)

    clear_contacts(stub)


if __name__ == '__main__':
  run()