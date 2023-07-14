from .node import DoublyLinkedNode


class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self._length = 0

    def __len__(self) -> int:
        return self._length

    def __repr__(self) -> str:
        return f"(len={self._length}, head={self.head}, tail={self.tail})"

    def add_last(self, value) -> None:
        node = DoublyLinkedNode(value)

        if self.head is None and self.tail is None:
            self.head = self.tail = node
        else:
            node.prev = self.tail
            node.prev.next = node
            self.tail = node

        self._length += 1

    def remove_first(self):
        if self.head is None:
            raise IndexError("Não é possível remover de uma sequência vazia")

        if self._length == 1:
            self.tail = None

        removed_value = self.head.value

        self.head = self.head.next
        self.head.prev = None
        self._length -= 1

        return removed_value

    def get(self, index: int):
        if index < 0 or index >= self._length:
            raise IndexError("Índice Inválido ou Inexistente")

        pointer = self.head
        for _ in range(index):
            pointer = pointer.next

        return pointer.value
