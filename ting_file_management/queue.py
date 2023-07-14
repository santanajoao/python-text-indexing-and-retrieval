from ting_file_management.abstract_queue import AbstractQueue
from .linked_list import DoublyLinkedList


class Queue(AbstractQueue):
    def __init__(self):
        self._lista = DoublyLinkedList()

    def __len__(self):
        return self._lista._length

    def enqueue(self, value):
        self._lista.add_last(value)

    def dequeue(self):
        return self._lista.remove_first()

    def search(self, index):
        return self._lista.get(index)
