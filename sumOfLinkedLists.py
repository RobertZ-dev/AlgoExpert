# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# O(max(n,m)) time | O(max(n,m)) space
def sumOfLinkedLists(linkedListOne, linkedListTwo):
    dummy = LinkedList(0)
	current = dummy
	carrier = 0
	
	nodeOne = linkedListOne
	nodeTwo = linkedListTwo
	while nodeOne is not None or nodeTwo is not None or carrier != 0:
		valueOne = nodeOne.value if nodeOne is not None else 0
		valueTwo = nodeTwo.value if nodeTwo is not None else 0
		sumOfValue = valueOne + valueTwo + carrier
		newValue = sumOfValue % 10
		newNode = LinkedList(newValue)
		current.next = newNode
		current = newNode
		carrier = sumOfValue // 10
		nodeOne = nodeOne.next if nodeOne is not None else None
		nodeTwo = nodeTwo.next if nodeTwo is not None else None
    return dummy.next
