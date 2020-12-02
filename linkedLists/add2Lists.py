# Definition for singly-linked list.
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
def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    
    printList(l1)
    printList(l2)
    sum = l1.val + l2.val
    carry = int(sum/10)
    l3 = ListNode(sum%10)
    p1 = l1.next
    p2 = l2.next
    p3 = l3
    if l1.next == None and l2.next ==None:
        if carry > 0:
            l3 = ListNode(sum%10)
            l3.next = ListNode(carry)
            printList(l3)
        else:
            l3 = ListNode(sum)
            printList(l3)
    while p1 != None or p2 !=None:
        sum = carry + (p1.val if  p1 else 0) + (p2.val if p2 else 0)
        carry = int(sum/10)
        p3.next = ListNode(sum % 10)
        p3 = p3.next
        p1 = p1.next if p1 else None
        p2 = p2.next if p2 else None
        if carry > 0:
            p3.next = ListNode(carry)
    printList(l3)


# l1 = ListNode(2)
# l1.next = ListNode(4)
# l1.next.next = ListNode(3)

# l2 = ListNode(5)
# l2.next = ListNode(6)
# l2.next.next = ListNode(4)
l1 = ListNode(0)
l2 = ListNode(0)

addTwoNumbers(l1, l2)
