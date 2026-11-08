class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def tambah(self, data):
        baru = Node(data)
        if self.head is None:
            self.head = baru
        else:
            semasa = self.head
            while semasa.next:
                semasa = semasa.next
            semasa.next = baru

    def papar(self):
        semasa = self.head
        while semasa:
            print(semasa.data)
            semasa = semasa.next

senarai = LinkedList()
senarai.tambah("Aiman")
senarai.tambah("Siti")
senarai.tambah("Raj")
senarai.papar()
