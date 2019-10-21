class Heap(object):
	def __init__(self):
		self.capacity = 10
		self.size = 0
		self.items = [None]*10

	#Getters ----------------
	def getLeft(self, parent):
		return self.items[(parent * 2) + 1]

	def getRight(self, parent):
		return self.items[(parent * 2) + 2]

	def getParent(self, child):
		return self.items[(child - 1) / 2]

	def getLeftChildIndex(self, parentIndex):
		return (parentIndex * 2) + 1

	def getRightChildIndex(self, parentIndex):
		return (parentIndex * 2) + 2

	def getParentIndex(self, childIndex):
		return (childIndex - 1) / 2

	def show(self):
		print "Items----------------------------------------" 
		print self.items
		print "---------------------------------------------"
		print "Size " + str(self.size)

	def printMenu(self):
		print "Command Menu----------------------\n" + "s to show\n" + "i <value> to insert\n" + "p to poll\n" + "peek to peek the heap\n" + "e to exit\n" + "----------------------------------"
	#-------------------------

	#Checkers-----------------
	def hasLeftChild(self, index):
		return (getLeftChildIndex(index) < self.size)

	def hasRightChild(self, index):
		return (getRightChildIndex(index) < self.size)

	def hasParent(self, index):
		return (getParentIndex(index) >= 0)
	#--------------------------

	def checkCapacity(self):
		if self.size >= self.capacity:
			print "Reached capacity"
		else:
			print "There are " + str(self.capacity - self.size) + " empty entries." 



	def swap(self, i1, i2):
		if self.items[i1] == None or self.items[i2] == None:
			print "Swapping value with null entry"
		else:
			temp = self.items[i1]
			self.items[i1] = self.items[i2]
			self.items[i2] = temp


	def insert(self, value):
		self.items[self.size] = value
		self.size += 1
		self.heapifyUp()


	#returns the min element in heap
	def peek(self): 
		return self.items[0]

	#returns and removes the min element from the heap
	def poll(self):
		polled = self.items[0]
		self.items[0] = self.items[self.size - 1]
		self.items[self.size - 1] = None
		self.size -= 1
		self.heapifyDown()
		return polled

	def heapifyDown(self):
		index = 0
		while self.items[index] > self.getLeft(index) and index < (self.size):
			if self.getLeft(index) == None:
				return
			if self.items[index] > self.getLeft(index):
				self.swap(index, self.getLeftChildIndex(index))
				index = self.getLeftChildIndex(index)
			elif self.items[index] > self.getRight(index):
				self.swap(index, self.getRightChildIndex(index))
				index = getRightChildIndex(index)

	def heapifyUp(self):
		index = self.size - 1
		while self.items[index] < self.getParent(index) and index > 0:
			self.swap(index, self.getParentIndex(index))
			index = self.getParentIndex(index)