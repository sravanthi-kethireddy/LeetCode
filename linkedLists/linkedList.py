class Node:
    def __init__(self, dataVal=None):
        self.dataVal = dataVal
        self.nextVal = None

class LinkedList:
    def __init__(self):
        self.headVal = None
    def atBeginning(self, data):
        NewNode = Node(data)
        NewNode.nextVal = self.headVal
        self.headVal = NewNode
        return NewNode
    def atEnd(self, data):
        NewNode = Node(data)
        NewNode.nextVal = None
        if self.headVal is None:
            self.headVal = NewNode
            return NewNode
        last = self.headVal
        while(last.nextVal):
            last = last.nextVal
        last.nextVal = NewNode
        return NewNode
    
    def inBetween(self, n1, n2, data):
        NewNode = Node(data)
        n1.nextVal = NewNode
        NewNode.nextVal = n2
        return NewNode

    def deleteNode(self,node):
        last = self.headVal
        if self.headVal == node:
            self.headVal = node.nextVal 
            return
        else:
            while(last):
                if (last.nextVal.dataVal) == (node.dataVal):
                    if last.nextVal is not None:
                        last.nextVal = node.nextVal
                        return
                    else:
                        self.headVal.nextVal = None

                last = last.nextVal
        
    def printList(self):
        self.printVal = self.headVal
        while self.printVal is not None:
            # print(self.printVal.dataVal)
            print(self.printVal.dataVal)
            self.printVal = self.printVal.nextVal
    # def isPalindrome(self):
    def deleteNthNode(self, n):
        last = self.headVal
        i=2
        while(last):
            if i == n:
                prevNode = last
                nextNode = last.nextVal.nextVal
                prevNode.nextVal = nextNode
                return
            i+=1
            last = last.nextVal
    def getNthNode(self, n):
        curr = self.headVal
        i=1
        while(curr):
            if i == n:
                print (curr.dataVal)
                return
            i+=1
            curr = curr.nextVal
        
    def reverse(self, node):
        print("2:", node.dataVal)
        if node.nextVal == None:
            self.headVal = node
            return
        print("3:", node.dataVal)
        self.reverse(node.nextVal)
        tmp = node.nextVal
        tmp.nextVal = node
        node.nextVal = None

    def reverseLinkedList(self):
        curr = self.headVal
        print("1:", curr.dataVal)
        while(curr):
            self.reverse(curr)
            curr = curr.nextVal
    
    def checkPalindrome(self):
        curr = self.headVal
        firstNode = self.headVal
        nextNode = curr.nextVal
        ans = False
        while(curr.dataVal is None):
            if curr.dataVal == firstNode.dataVal:
                ans = True
                



        

            

list1 = LinkedList()
list1.headVal = Node(1)
e2 = Node(2)
e3 = Node(3)
e4 = Node(4)
list1.headVal.nextVal = e2
e2.nextVal = e3
e3.nextVal = e4
e4.nextVal = None
# list1.headVal = Node('Sunday')
# e2 = Node('Monday')
# e3 = Node('Tuesday')
# e4 = Node('Wednesday')
# e5 = Node('Thursday')
# e6 = Node('Friday')
# e7 = Node('Saturday')

# list1.headVal.nextVal = e2
# e2.nextVal = e3
# e3.nextVal = e4
# e4.nextVal = e5
# e5.nextVal = e6
# e6.nextVal = e7
# e8 = list1.atBeginning('MyTestJanuary')
# e9 = list1.atEnd('MyTestDecember')
# e10 = list1.inBetween(list1.headVal, e2, 'I hate this')
# e11 = list1.inBetween(e6, e7, 'I love this')
# list1.deleteNode(e2)
# list1.printList()

# list1.deleteNode(list1.headVal)
# list1.printList()


# print(">>>>>>>>>",type(e6), type(e8), type(e10))
# list1.deleteNode(e9)
# print("Deleting the last node>>>>>>")

# list1.deleteNthNode(3)
# list1.getNthNode(3)
# list1.printList()
list1.reverseLinkedList()
# list1.printList()
# e10 = list1.atBeginning('1')
# e8.nextVal = None





