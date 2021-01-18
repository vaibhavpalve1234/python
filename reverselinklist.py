class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
 
 
# Function to print given linked list
def printList(head):
 
    ptr = head
    while ptr:
        print(ptr.data, end=" -> ")
        ptr = ptr.next
 
    print("None")
 
 
# Recursive function to reverse linked list.
# It reverses given linked list by fixing the head pointer first and
# then .next pointers of very node in reverse order
def reverse(head):
 
    # empty list base case
    if head is None:
        return head
 
    first = head                # suppose first = [1, 2, 3]
    rest = first.next           # rest = [2, 3]
    
 
    # empty rest base case
    if rest is None:
        return head
 
    rest = reverse(rest)        # Recursively reverse the smaller 2, 3 case
    # after: rest = [3, 2]
 
    first.next.next = first     # put first elem on the end of the list
    first.next = None           # (tricky step -- make a drawing)
    head = rest                 # fix the head pointer
 
    return head
 
 
# Reverse linked list using Recursion
if __name__ == '__main__':
 
    head = None
    for i in reversed(range(6)):
        head = Node(i + 1, head)
 
    head = reverse(head)
    printList(head)
