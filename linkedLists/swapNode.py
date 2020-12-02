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

def swapNodes(l):
    """
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    """
    temp = (l)
    if temp is None:
        return 
    while (temp is not None and temp.next is not None):
        temp.val, temp.next.val = temp.next.val, temp.val
        temp = temp.next.next
    printList(temp)


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(6)
swapNodes(l1)