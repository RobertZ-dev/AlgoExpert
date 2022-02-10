# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# O(n) time | O(1) space, n is the total length of the linked list
def removeKthNodeFromEnd(head, k):
	counter = 1
	first = head
	second = head
	while counter <= k:
		second = second.next
		counter += 1
	if second is None: # 2nd pointer reaches tail, 1st is head now
		head.value = head.next.value # update the head value
		head.next = head.next.next # update the head.next pointer
		return
	# when we jump out of this while loop, the second pointer
	# points to the final value of the linked list
	while second.next is not None: 
		second = second.next
		first = first.next
	first.next = first.next.next
		