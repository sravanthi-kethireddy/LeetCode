# class Node:
#     def __init__(self, data=None):
#         self.data = data
#         self.next =None
# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.last_node = None
#     def append(self, data):
#         if (self.last_node) is None:
#             self.head = Node(data)
#             self.last_node = self.head
#         else:
#             self.last_node.next = Node(data)
#             self.last_node = self.last_node.next
#     def get_prev_node(self, ref_node):
#         current = self.head
#         while (current and current.next != ref_node):
#             current = current.next
#         return current
#     def printList(self):
#         self.curr = self.head
#         while(self.curr):
#             print(self.curr.data)
#             self.curr = self.curr.next

# def isPalindrome(llist):
#     start = llist.head
#     end = llist.last_node
#     print(">>",end.data)
#     while(start!= end and end.next !=start):
#         if start.data != end.data:
#             return False
#         start = start.next
#         end = llist.get_prev_node(end)
#     return True

# list1 = LinkedList()
# nodes = input("enter the nodes, separate by space: ")
# nodes = nodes.split(' ')
# for each in nodes:
#     list1.append(each)

# list1.printList()
# print(isPalindrome(list1))

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None
    def append(self, data):
        if (self.last_node is None):
            self.head = Node(data)
            self.last_node = self.head
        else:
            self.last_node.next = Node(data)
            self.last_node = self.last_node.next
    def get_prev_node(self, ref_node):
        current = self.head
        while(current and current.next != ref_node):
            current = current.next
        return current
    def printList(self):
        curr = self.head
        while(curr):
            print(curr.data)
            curr = curr.next
    def isPalindrome(self):
        curr = self.head
        start = self.head
        end = self.last_node
        while (start!=end and end.next !=start):
            if start.data != end.data:
                return False
            start = start.next
            end = self.get_prev_node(end)
            curr = curr.next
        return True



ll = LinkedList()
ll_data = input("Enter the nodes: ")
for i in ll_data.split(' '):
    ll.append(i)


# ll.printList()
print(ll.isPalindrome())            
        
