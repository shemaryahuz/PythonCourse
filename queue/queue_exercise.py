"""Queue Exercise"""

from class_exercises import QueueImplementation

"""exercise 1"""

def len_queue(queue):
    q = QueueImplementation()
    counter = 0
    while not queue.queue_is_empty():
        q.enqueue(queue.dequeue())
        counter += 1

    while not q.queue_is_empty():
        queue.enqueue(q.dequeue())

    return counter

# qu = QueueImplementation()
# qu.enqueue(1)
# qu.enqueue(2)
# qu.enqueue(3)
#
# print(len_queue(qu))


"""exercise 2"""

def differences(queue):
    dif_q = QueueImplementation()
    save_q = QueueImplementation()
    while not queue.queue_is_empty():
        x = queue.dequeue()
        if not queue.queue_is_empty():
            y = queue.head()
            dif = x - y
            dif_q.enqueue(dif)
        save_q.enqueue(x)

    while not save_q.queue_is_empty():
        queue.enqueue(save_q.dequeue())

    return dif_q


qu = QueueImplementation()
qu.enqueue(7)
qu.enqueue(2)
qu.enqueue(6)
qu.enqueue(9)
qu.enqueue(5)
qu.enqueue(3)

differences = differences(qu)

# while not differences.queue_is_empty():
#     print(differences.dequeue())
while not qu.queue_is_empty():
    print(qu.dequeue())

"""exercise 3"""

def replace(queue, old, new):
    save_q = QueueImplementation()
    while not queue.queue_is_empty():
        element = queue.dequeue()
        if element == old:
            save_q.enqueue(new)
        else:
            save_q.enqueue(element)

    while not save_q.queue_is_empty():
        queue.enqueue(save_q.dequeue())

# qu = QueueImplementation()
# qu.enqueue(6)
# qu.enqueue(3)
# qu.enqueue(5)
# qu.enqueue(-1)
# qu.enqueue(3)
# qu.enqueue(-3)
# replace(qu, 3, 5)
#
# while not qu.queue_is_empty():
#     print(qu.dequeue())

"""exercise 4"""

def sort_negatives_after_positives(queue):
    save_q = QueueImplementation()
    save_qp = QueueImplementation()
    save_qn = QueueImplementation()
    while not queue.queue_is_empty():
        elm = queue.dequeue()
        if elm >= 0:
            save_qp.enqueue(elm)
            save_q.enqueue(elm)
        else:
            save_qn.enqueue(elm)
            save_q.enqueue(elm)

    while not save_q.queue_is_empty():
        queue.enqueue(save_q.dequeue())

    new_q = QueueImplementation()
    while not save_qp.queue_is_empty():
        new_q.enqueue(save_qp.dequeue())

    while not save_qn.queue_is_empty():
        new_q.enqueue(save_qn.dequeue())

    return new_q

# qu = QueueImplementation()
# qu.enqueue(-2)
# qu.enqueue(3)
# qu.enqueue(-5)
# qu.enqueue(1)
# qu.enqueue(-3)
# qu.enqueue(3)
#
# sorted_qu = sort_negatives_after_positives(qu)
#
# while not qu.queue_is_empty():
#     print(qu.dequeue())
#
# while not sorted_qu.queue_is_empty():
#     print(sorted_qu.dequeue())

"""exercise 7"""
from stack.stack_by_linked_list import StackByLinkedList

# class QueueByStacks:
#     def __init__(self):
#         self.stack1 = StackByLinkedList()
#         self.stack2 = StackByLinkedList()
#
#     def queue_is_empty(self):
#         return self.stack1.is_empty() and self.stack2.is_empty()
#
#     def enqueue(self, value):
#         pass
#
#     def dequeue(self):
#         return
#
#     def head(self):
#         return
