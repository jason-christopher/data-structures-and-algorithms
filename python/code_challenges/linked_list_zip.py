from data_structures.linked_list import LinkedList


def zip_lists(a, b):
    list1 = a.head
    list2 = b.head
    new_list = LinkedList()

    while list1 and list2:
        new_list.append(list1.value)
        list1 = list1.next
        new_list.append(list2.value)
        list2 = list2.next

    while list1:
        new_list.append(list1.value)
        list1 = list1.next

    while list2:
        new_list.append(list2.value)
        list2 = list2.next

    return new_list
