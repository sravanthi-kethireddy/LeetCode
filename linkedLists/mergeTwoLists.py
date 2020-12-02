# Definition for singly-linked list.
class ListNode(object):
    def __init__(self,x):
        self.val = x
        self.next = None
def printList(l):
    value = []
    while(l):
        value.append(l.val)
        l = l.next
    print(' -> '.join(map(str, value)))
def mergeTwoLists(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    
    printList(l1)
    printList(l2)
    head_ptr = temp_ptr = ListNode(-1)
    while l1 or l2:
        if l1 and (not l2 or l1.val <= l2.val):
            temp_ptr.next = ListNode(l1.val)
            l1 = l1.next
        else:
            temp_ptr.next = ListNode(l2.val)
            l2 = l2.next
        temp_ptr = temp_ptr.next
    printList(head_ptr.next)


  

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(5)

l2 = ListNode(2)
l2.next = ListNode(6)
l2.next.next = ListNode(6)


mergeTwoLists(l1, l2)
