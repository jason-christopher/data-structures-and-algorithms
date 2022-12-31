from data_structures.linked_list import LinkedList


def zip_lists(a, b):
    # if a.head exists, create a pointer for "current" and "start". If not, return a Linked List with b.head
    if a.head:
        cur = start = a.head
        a.head = a.head.next
    else:
        return LinkedList(b.head)

    # require both a.head and b.head to exist
    while a.head and b.head:
        # b.head stuff happens first since you start with a.head above
        cur.next = b.head
        b.head = b.head.next
        cur = cur.next

        # a.head stuff follows
        cur.next = a.head
        a.head = a.head.next
        cur = cur.next

    # after reaching the end of one list, the rest is filled with the remaining list
    cur.next = a.head or b.head

    # use the "start" pointer to initiate
    return LinkedList(start)



# def zip_lists(a, b):
#     new_list = LinkedList()
#
#     while a.head or b.head:
#         if a.head:
#             new_list.append(a.head.value)
#             a.head = a.head.next
#         if b.head:
#             new_list.append(b.head.value)
#             b.head = b.head.next
#
#     return new_list





