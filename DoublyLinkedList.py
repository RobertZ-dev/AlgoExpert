# This is an input class. Do not edit.
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

# Feel free to add new properties and methods to the class.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
		
	# O(1) time | O(1) space
    def setHead(self, node):
		if self.head is None:
			self.head = node
			self.tail = node
			return
		self.insertBefore(self.head, node)
	
	# O(1) time | O(1) space
    def setTail(self, node):
        if self.tail is None:
			self.setHead(node)
			return
		self.insertAfter(self.tail, node)

	# O(1) time | O(1) space
    def insertBefore(self, node, nodeToInsert):
		if nodeToInsert == self.head and nodeToInsert == self.tail:
			return
		self.remove(nodeToInsert)
		nodeToInsert.prev = node.prev
		nodeToInsert.next = node
		if node.prev is None:
			self.head = nodeToInsert
		else:
			node.prev.next = nodeToInsert
		node.prev = nodeToInsert
		
	# O(1) time | O(1) space
    def insertAfter(self, node, nodeToInsert):
		if nodeToInsert == self.head and nodeToInsert == self.tail:
			return
		self.remove(nodeToInsert)
		nodeToInsert.next = node.next
		nodeToInsert.prev = node
		if node.next is None:
			self.tail = nodeToInsert
		else:
			node.next.prev = nodeToInsert
		node.next = nodeToInsert
		
	# O(p) time | O(1) space, p is the position, and p=n when it is the last one.
    def insertAtPosition(self, position, nodeToInsert):
        if position == 1: # if we are inserting a head node
			self.setHead(nodeToInsert)
			return
		node = self.head
		currentPosition = 1
		while node is not None and currentPosition != position:
			node = node.next
			currentPosition += 1
		if node is not None:
			self.insertBefore(node, nodeToInsert)
		else: 
			self.setTail(nodeToInsert)
	
	# O(n) time | O(1) space
    def removeNodesWithValue(self, value):
		node = self.head
		while node is not None:
			nodeToRemove = node # setup a temporary node to remember
			node = node.next # start sweeping
			if nodeToRemove.value == value: # decide whether the current node is target node
				self.remove(nodeToRemove) # to avoid losing the pointer (removebinding) use temporary node

	# O(1) time | O(1) space
    def remove(self, node):
		if (node == self.head): # if we are removing the head
			self.head = self.head.next # seek the head.next and assign as the head
		if (node == self.tail): # if we are removing the tail
			self.tail = self.tail.prev # seek the tail.prev and assign as the tail
        self.removeNodeBindings(node)
	
	# O(n) time | O(1) space
    def containsNodeWithValue(self, value):
		node = self.head
		while node is not None and node.value != value:
			node = node.next
		return node is not None
	
	# O(n) time | O(1) space
	def removeNodeBindings(self, node):
		if node.prev is not None:
			node.prev.next = node.next # before removing node.prev, assign next to its prev.next
		if node.next is not None:
			node.next.prev = node.prev # before removing node.next, assign prev to its next.prev
		node.prev = None # assign completed, remove prev
		node.next = None # assign completed, remove next
		