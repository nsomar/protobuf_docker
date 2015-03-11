import time

import addressbook_pb2

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class AddressBookServer(addressbook_pb2.EarlyAdopterAddressServicer):

    def __init__(self):
        self.addresses = []

    def AddAddressEntry(self, request, context):
        self.addresses.append(request.person)
        return addressbook_pb2.AddressAddReply(message='Address added, %s! we now have %d items' % (request.person.name, len(self.addresses)))

    def DisplayAllAddresses(self, request, context):
        return addressbook_pb2.DisplayAllAddressesReply(items=self.addresses)

    def DeleteAll(self, request, context):
        self.addresses = []
        return addressbook_pb2.DeleteAllReply()

    def SearchForAddress(self, request, context):
        filtered = []

        for person in self.addresses:
            test1 = True if request.name == "" else person.name == request.name
            test2 = True if request.id == 0 else person.id == request.id
            test3 = True if request.email == "" else person.email == request.email

            if test1 and test2 and test3:
                filtered.append(person)

        return addressbook_pb2.SearchForAddressReply(items=filtered)


def serve():
    server = addressbook_pb2.early_adopter_create_Address_server(
        AddressBookServer(), 50052, None, None)
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop()

if __name__ == '__main__':
    serve()