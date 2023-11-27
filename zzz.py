class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def merge_sorted_lists(headA, headB):
    merged_head = ListNode()  # Dummy node to simplify code
    current = merged_head

    while headA is not None and headB is not None:
        if headA.value < headB.value:
            current.next = headA
            headA = headA.next
        else:
            current.next = headB
            headB = headB.next
        current = current.next

    # If one of the lists is not empty, append the remaining nodes
    if headA is not None:
        current.next = headA
    elif headB is not None:
        current.next = headB

    return merged_head.next  # Skip the dummy node

# Function to print the linked list
def print_linked_list(head):
    current = head
    while current is not None:
        print(current.value)
        current = current.next

# Get input from the user
n1 = int(input())
list1 = [int(input()) for _ in range(n1)]

n2 = int(input())
list2 = [int(input()) for _ in range(n2)]

# Create linked list nodes for the two lists
headA = ListNode(list1[0])
currentA = headA
for value in list1[1:]:
    currentA.next = ListNode(value)
    currentA = currentA.next

headB = ListNode(list2[0])
currentB = headB
for value in list2[1:]:
    currentB.next = ListNode(value)
    currentB = currentB.next

# Merge the sorted lists and print the result
merged_head = merge_sorted_lists(headA, headB)
print()
print_linked_list(merged_head)
