# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def sumOfLinkedLists(linkedListOne, linkedListTwo):
    num1 = listToNum(linkedListOne)
    num2 = listToNum(linkedListTwo)
    num3 = num1 + num2
    str3 = str(num3)[::-1]
    pointer = 0
    current = result = LinkedList(0)
    for pointer in range(len(str3)):
        current.next = LinkedList(int(str3[pointer]))
        current = current.next
    return result.next


def listToNum(linkedList):
    pointer = linkedList
    num2str = []
    while pointer is not None:
        num2str.append(str(pointer.value))
        pointer = pointer.next
    return int("".join(num2str[::-1]))
