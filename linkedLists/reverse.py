class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
def printList(l):
    value = []
    while(l):
        value.append(l.val)
        l = l.next
    print(' -> '.join(map(str, value)))

def reverselist(l):
    prev = None
    current = l
    while current:
        nextVal = current.next
        current.next = prev
        prev = current
        current = nextVal
    l = prev
    printList(l)
    

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(6)
l1.next.next.next = ListNode(8)
printList(l1)
reverselist(l1)