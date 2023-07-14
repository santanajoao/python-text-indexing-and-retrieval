class DoublyLinkedNode:
    def __init__(self, value, prev=None, next=None) -> None:
        self.value = value
        self.next: DoublyLinkedNode | None = next
        self.prev: DoublyLinkedNode | None = prev

    def __repr__(self) -> str:
        prev_val = self.prev.value if self.prev else None
        next_val = self.next.value if self.next else None
        return f"(value={self.value}, prev={prev_val}, next={next_val})"
