from typing import Any, Callable
from ting_file_management.abstract_queue import AbstractQueue
from ting_file_management.linked_list import DoublyLinkedList


class Queue(AbstractQueue):
    def __init__(self):
        self._lista = DoublyLinkedList()

    def __len__(self):
        return self._lista._length

    def __iter__(self):
        return iter(self._lista)

    def enqueue(self, value) -> None:
        self._lista.add_last(value)

    def dequeue(self):
        return self._lista.remove_first()

    def search(self, index) -> Any:
        return self._lista.get(index)

    def find(self, value, *, key: Callable):
        return self._lista.find(value, key=key)
