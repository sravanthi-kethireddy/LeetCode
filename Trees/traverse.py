from queue import Queue 

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data)
        if self.right:
            self.right.printTree()
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            if data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
    def levelTraverse(self):
        
        q = Queue()
        levelList = []
        if self.data is None:
            return
        q.put(self)
        while q.qsize() != 0:       
            count  = q.qsize()
            val = []
            while count>0:
                temp = q.get()
                # print(temp.data, end = ' ')
                val.append(temp.data)
                if temp.left:
                    q.put(temp.left)
                if temp.right:
                    q.put(temp.right)
                count -=1
            levelList.append(val)
            # print(' ')
        return (levelList)

root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
root.insert(4)
root.insert(7)
root.insert(13)
root.insert(19)
# root.printTree()
levelList = root.levelTraverse()
def leftView(levelOrder):
    print("Left View")
    for each in levelOrder:
        print(each[0])
def rightView(levelOrder):
    print("Right View")
    for each in levelOrder:
        print(each[-1])

leftView(levelList)
rightView(levelList)
