from typing import Callable, Generic, TypeVar, Generator
from ting_file_management.abstract_queue import AbstractQueue
from ting_file_management.linked_list import DoublyLinkedList

T = TypeVar('T')


class Queue(AbstractQueue, Generic[T]):
    def __init__(self) -> None:
        self._lista = DoublyLinkedList[T]()

    def __len__(self) -> int:
        return self._lista._length

    def __iter__(self) -> Generator[T, None, None]:
        return iter(self._lista)

    def enqueue(self, value: T) -> None:
        self._lista.add_last(value)

    def dequeue(self) -> T:
        return self._lista.remove_first()

    def search(self, index: int) -> T:
        return self._lista.get(index)

    def find(self, value: T, *, key: Callable | None = None) -> T | None:
        return self._lista.find(value, key=key)
