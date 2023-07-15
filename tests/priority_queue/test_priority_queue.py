import pytest
from ting_file_management.priority_queue import PriorityQueue

regular_priority_file = {"qtd_linhas": 23}
high_priority_file = {"qtd_linhas": 4}


def test_basic_priority_queueing():
    queue = PriorityQueue()
    assert len(queue) == 0

    assert queue.is_priority(regular_priority_file) is False
    assert queue.is_priority(high_priority_file) is True

    queue.enqueue(regular_priority_file)
    assert len(queue.regular_priority) == 1

    queue.enqueue(high_priority_file)
    assert len(queue.high_priority) == 1

    assert queue.search(0) == high_priority_file
    assert queue.search(1) == regular_priority_file

    with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
        queue.search(5)

    with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
        queue.search(-2)

    queue.dequeue()
    assert len(queue.regular_priority) == 1
    assert len(queue.high_priority) == 0

    queue.dequeue()
    assert len(queue.regular_priority) == 0
    assert len(queue.high_priority) == 0
