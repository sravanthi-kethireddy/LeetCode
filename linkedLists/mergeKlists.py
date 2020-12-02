class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
import heapq
def printList(l):
    value = []
    while(l):
        value.append(l.val)
        l = l.next
    print(' -> '.join(map(str, value)))

def mergeKLists(lists):
    for i in lists:
        printList(i)
    node, head, pointer = [], None, None
    
    for each in lists:
        while each:
            heapq.heappush(node, each.val)
            each = each.next
    while node:
        if head == None:
            head = ListNode(heapq.heappop(node))
            pointer = head
        else:
            pointer.next = ListNode(heapq.heappop(node))
            pointer = pointer.next
    printList(head)

    
    
    

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(5)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(7)

l3 = ListNode(2)
l3.next = ListNode(4)
l3.next.next = ListNode(5)

kLists = [l1, l2, l3]

mergeKLists(kLists)