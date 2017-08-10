#https://pypi.python.org/pypi/linkedlist
# from linkedlist import LinkedList

#https://pypi.python.org/pypi/llist
from llist import sllist, sllistnode


ll = sllist([1, 4, 5, 3, 6, 4, 1, 3, 7, 2, 8])

head = ll.first

#Remove all the duplicates from a singlely linked list that is not sorted

values = set()
prev_node = None
current_node = ll.first

for value in ll:                            # O(n)
    current_value = current_node.value
    if current_value not in values:         # O(1)
        values.add(current_value)
        prev_node = current_node
    else:
        prev_node.next = current_node.next
        
    current_node = current_node.next



# Solution is O(n log n)