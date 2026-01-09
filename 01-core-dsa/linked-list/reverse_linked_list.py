class Node:
    def __init__(self, val=0, nxt=None):
        self.val = val
        self.next = nxt

def reverse_list(head):
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev

if __name__ == '__main__':
    n3 = Node(3)
    n2 = Node(2, n3)
    n1 = Node(1, n2)
    r = reverse_list(n1)
    while r:
        print(r.val)
        r = r.next