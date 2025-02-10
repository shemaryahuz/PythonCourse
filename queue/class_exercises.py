

from advanced_linked_list import AdvancedLinkedList

class QueueImplementation:

    def __init__(self):
        self.__linked_list = AdvancedLinkedList()

    def queue_is_empty(self):
        return self.__linked_list.len_list() == 0

    def enqueue(self, value):
        self.__linked_list.append_last(value)

    def dequeue(self):
        return self.__linked_list.pop_first()

    def head(self):
        return self.__linked_list.get_value(0)



# queue = QueueImplementation()

# queue.enqueue(4)
# queue.enqueue(10)
# queue.enqueue(7)
# print(queue.queue_is_empty()) # False
# print(queue.head()) # 4
# print(queue.dequeue()) # 4
# print(queue.head()) # 10
# print(queue.dequeue()) # 10
# print(queue.head()) # 7
# print(queue.dequeue()) # 7
# print(queue.queue_is_empty()) # True

# def negative_queue(lst):
#     q = QueueImplementation()
#     for x in lst:
#         if x < 0:
#             q.enqueue(x)
#     return q
#
# a = [3, -5, 9, 0, -3, -4]
# nq = negative_queue(a)
# while not nq.queue_is_empty():
#     print(nq.dequeue())



















