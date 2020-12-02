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


def removeDups(l):
    if l == None:
        return
    currentNode = l
    print("Before: ")
    printList(l)
    while currentNode:
        runnerNode = currentNode
        while runnerNode.next != None:
            if runnerNode.next.val == currentNode.val:
                runnerNode.next = runnerNode.next.next
            else:
                runnerNode = runnerNode.next
        currentNode = currentNode.next
    print("After: ")
    printList(l)
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(8)
l1.next.next.next = ListNode(6)
l1.next.next.next.next = ListNode(2)
l1.next.next.next.next.next = ListNode(2)
l1.next.next.next.next.next.next = ListNode(8)
removeDups(l1)
