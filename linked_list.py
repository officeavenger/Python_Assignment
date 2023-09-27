class Node:
    def _init_(self, value=None):
        self.value = value
        self.next_node = None

class LinkedList:
    def _init_(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            self.tail.next_node = new_node
        self.tail = new_node
        self.size += 1

    def insert(self, value, position):
        new_node = Node(value)
        if position == 0:
            new_node.next_node = self.head
            self.head = new_node
        else:
            prev_node = self.get_node(position - 1)
            if prev_node:
                new_node.next_node = prev_node.next_node
                prev_node.next_node = new_node
                self.size += 1

    def get_value(self, position):
        node = self.get_node(position)
        return node.value if node else None

    def get_node(self, position):
        if position < 0 or position >= self.size:
            return None
        current_node = self.head
        for _ in range(position):
            current_node = current_node.next_node
        return current_node

    def set_value(self, value, position):
        node = self.get_node(position)
        if node:
            node.value = value

    def size(self):
        return self.size

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.value, end=' ')
            current_node = current_node.next_node
        print()

    def info(self):
        print('List elements:', end=' ')
        self.print_list()
        print(f'Size: {self.size}')

    def remove(self, position):
        if position < 0 or position >= self.size:
            return None

        if position == 0:
            removed_node = self.head
            self.head = self.head.next_node
            if not self.head:
                self.tail = None
        else:
            prev_node = self.get_node(position - 1)
            removed_node = prev_node.next_node
            prev_node.next_node = removed_node.next_node
            if removed_node == self.tail:
                self.tail = prev_node

        self.size -= 1
        return removed_node

    def clear(self):
        while self.head:
            self.remove(0)