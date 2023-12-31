from typing import Callable, Generator, Generic, TypeVar, Optional
from ting_file_management.node import DoublyLinkedNode

T = TypeVar('T')


class DoublyLinkedList(Generic[T]):
    def __init__(self) -> None:
        self.head: Optional[DoublyLinkedNode[T]] = None
        self.tail: Optional[DoublyLinkedNode[T]] = None
        self._length = 0

    def __len__(self) -> int:
        return self._length

    def __repr__(self) -> str:
        return f"(len={self._length}, head={self.head}, tail={self.tail})"

    def __iter__(self) -> Generator[T, None, None]:
        pointer = DoublyLinkedNode(None, next=self.head)
        while pointer.next:
            pointer = pointer.next
            yield pointer.value

    def add_last(self, value: T) -> None:
        node = DoublyLinkedNode[T](value)

        if self.head is None and self.tail is None:
            self.head = self.tail = node
        else:
            node.prev = self.tail
            node.prev.next = node
            self.tail = node

        self._length += 1

    def remove_first(self) -> T:
        if self.head is None:
            raise IndexError("Não é possível remover de uma sequência vazia")

        if self._length == 1:
            self.tail = None

        removed_value = self.head.value

        self.head = self.head.next
        if self.head:
            self.head.prev = None

        self._length -= 1

        return removed_value

    def get(self, index: int) -> T:
        if index < 0 or index >= self._length:
            raise IndexError("Índice Inválido ou Inexistente")

        pointer = self.head
        for _ in range(index):
            pointer = pointer.next

        return pointer.value

    def some(self, value: T, *, key: Callable | None = None) -> bool:
        for pointer_value in self:
            _value = key(pointer_value) if key else pointer_value
            if _value == value:
                return True
        return False
