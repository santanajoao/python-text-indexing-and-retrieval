from typing import TypeVar, Generic, Optional

T = TypeVar("T")


class DoublyLinkedNode(Generic[T]):
    def __init__(
        self,
        value: T,
        prev: Optional["DoublyLinkedNode[T]"] = None,
        next: Optional["DoublyLinkedNode[T]"] = None
    ) -> None:
        self.value = value
        self.next = next
        self.prev = prev

    def __repr__(self) -> str:
        prev_val = self.prev.value if self.prev else None
        next_val = self.next.value if self.next else None
        return f"(value={self.value}, prev={prev_val}, next={next_val})"
