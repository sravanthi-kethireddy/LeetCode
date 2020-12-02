# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
def printList(l):
    list = []
    # l1 = l.val
    while l:
        list.append(l.val)
        l = l.next
    print(' -> '.join(str(x) for x in list))

def removeNthFromEnd(head, n):
    """
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    """
    printList(head)
    first = head
    second = head
    for i in range(n):
        if (second.next == None):
            if (i == n-1):
                head = head.next
            return head
        second = second.next
    while(second.next!=None):
        second = second.next
        first = first.next
    first.next = first.next.next
    printList(head)
    

l1 = ListNode(2)
# l1.next = ListNode(4)
# l1.next.next = ListNode(3)
# l1.next.next.next = ListNode(6)
removeNthFromEnd(l1, 2)