
def isPrime(n):

	if n <= 1:
		return False
	if n <= 3:
		return True

	if n % 2 == 0 or n % 3 == 0:
		return False
	
	i = 5
	while i * i <= n:
		if n % i == 0 or n % (i + 2) == 0:
			return False
		i += 6

	return True

class Node:
	
	def __init__(self, data, next):
		self.data = data
		self.next = next
		
class LinkedList:
	
	def __init__(self):
		self.head = None
	
	
	def push(self, new_data):
		new_node = Node(new_data, self.head)
		self.head = new_node

	def countEven(self):
	
		count = 0
		ptr = self.head
	
		while ptr != None:
			
			
			if(ptr.data % 2 == 0):
				
				count += 1
				print(ptr.data,sep=" ")
			
			ptr = ptr.next
				
		return count

	def countPrime(self):
	
		count = 0
		ptr = self.head
	
		while ptr != None:
			
			
			if isPrime(ptr.data):
				
				count += 1
				print(ptr.data,sep=" ")
			
			ptr = ptr.next
			
	
		return count

    
def sort_linkedlist(self):
  if self.head is None:
     return

  swapped = True
  while swapped:
   swapped = False
   prev = None
   current = self.head

   while current.next is not None:
        if current.data > current.next.data:
                if prev is None:
                    self.head = current.next
                else:
                    prev.next = current.next
                    current.next = current.next.next
                    prev.next.next = current
                    prev = prev.next
                    swapped = True
               else:
                    prev = current
                    current = current.next



    

if __name__ == "__main__":


	linkedlist = LinkedList()

	
	linkedlist.push(17)
	linkedlist.push(10)
	linkedlist.push(6)
	linkedlist.push(5)
	linkedlist.push(15)

	
	print("Count of prime nodes =",
		linkedlist.countPrime())
	print("Count of even nodes =",
		linkedlist.countEven())
	print("Original Linked List:")
    # Print the original linked list
    ptr = linkedlist.head
    while ptr is not None:
     print(ptr.data, end=" -> ")
     ptr = ptr.next
    print("None")

    linkedlist.sort_linkedlist()

    print("Sorted Linked List:")
    # Print the sorted linked list
    ptr = linkedlist.head
    while ptr is not None:
     print(ptr.data, end=" -> ")
    ptr = ptr.next
    print("None")

