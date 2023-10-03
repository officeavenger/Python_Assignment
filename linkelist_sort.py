class ListNode:
    def _init_(self, value):
        self.value = value
        self.next = None

def selection_sort_linked_list(head):
    if not head or not head.next:
        return head

    current = head

    while current:
        # Find the minimum value node in the remaining part of the list
        min_node = current
        runner = current.next

        while runner:
            if runner.value < min_node.value:
                min_node = runner
            runner = runner.next

        # Swap the values of the current node and the minimum node
        current.value, min_node.value = min_node.value, current.value

        current = current.next

    return head

# Example usage:
# Create a sample linked list
head = ListNode(3)
head.next = ListNode(1)
head.next.next = ListNode(4)
head.next.next.next = ListNode(2)

# Sort the linked list
sorted_head = selection_sort_linked_list(head)

# Print the sorted linked list
while sorted_head:
    print(sorted_head.value, end=" -> ")
    sorted_head = sorted_head.next